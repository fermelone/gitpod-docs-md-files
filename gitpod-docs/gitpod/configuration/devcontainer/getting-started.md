# Getting started

> Explore Gitpod's Dev Container features. Learn about the benefits of using Dev Containers, how to create a devcontainer.json file, and how to use Gitpod's Dev Container support.

<Note>
  {' '}

  If you're configuring your Dev Container in **VS Code** also check out the [VS
  Code documentation](/flex/editors/vscode). Particularly for extra information
  on rebuilding your container, recovery mode and accessing logs.
</Note>

When you first create a development environment in Gitpod, it looks for a [devcontainer.json](https://containers.dev/implementors/spec/#devcontainerjson) file in your repository. This file acts as a blueprint for setting up a consistent, standardized environment for your project.

If you haven't created a devcontainer.json file yet and start an environment in Gitpod, your environment will automatically have a Dev Container created in the environment. This initial configuration should form a good basis for iterating further.

When refining your environment, you'll need to choose between two main scenarios for your Dev Container:

* **Single Container Setup**: This simplest scenario runs everything you need inside a single container. It's ideal for most projects where one environment can handle your entire development stack—for instance, a Node.js application with all dependencies and tools in one container.

* **Multi-Container Setup with Docker Compose**: For more complex projects involving multiple services—such as a web application with a separate database—Docker Compose allows you to define and orchestrate multiple containers. Each service operates in its own container, yet they function together as a unified environment.

## Starting with a custom Dockerfile

If you’re using a single container and already have a Dockerfile, you can base your Dev Container configuration on it. Here’s how you might set it up:

```json
{
	"name": "Node.js Dev Container",
	"build": {
		"context": "..",
		"dockerfile": "../Dockerfile"
	},
	"customizations": {
		"vscode": {
			"settings": {},
			"extensions": ["dbaeumer.vscode-eslint"]
		}
	},
	"remoteUser": "node"
}
```

* **build:** Builds the container from the Dockerfile in the parent directory.

* **vscode:** Installs the ESLint extension for JavaScript linting in VS Code.

* **remoteUser:** Specifies the user inside the container (set to **node**).

**.gitpod/automations.yaml:** For installing dependencies, use [automations](../automations):

```yaml
tasks:
    install-dependencies:
        name: Install dependencies
        command: npm install
        triggeredBy:
            - postDevcontainerStart
            - manual
```

## Starting with a Docker Compose

In this example, we set up a multi-container environment using Docker Compose. This setup includes two containers: one for the application (service container) and another for the PostgreSQL database.

> Beware that devcontainer's interaction with docker compose can quickly lead to broken environments, due to unforeseen interactions between your devcontainer and Docker services.

**devcontainer.json:** This file defines the development container configuration and ties it to the Docker Compose setup.

```json
{
	"name": "Node.js + PostgreSQL Dev Container",
	"dockerComposeFile": "../docker-compose.yml",
	"service": "app",
	"workspaceFolder": "/workspaces/${localWorkspaceFolderBasename}",
	"customizations": {
		"vscode": {
			"extensions": [
				"dbaeumer.vscode-eslint",
				"ms-azuretools.vscode-docker"
			]
		}
	},
	"remoteUser": "node"
}
```

* **dockerComposeFile:** Points to the Docker Compose file that defines the services.

* **service:** Specifies the main development container (**app**).

* **workspaceFolder:** Defines the working directory inside the container.

* **vscode:** Installs the necessary VS Code extensions.

* **remoteUser:** Specifies the user inside the container (set to node).

**.gitpod/automations.yaml:** For installing dependencies, use [automations](../automations):

```yaml
tasks:
    install-dependencies:
        name: Install dependencies
        command: npm install
        triggeredBy:
            - postDevcontainerStart
            - manual
```

**docker-compose.yml:** This file configures the multi-container setup, defining both the **app** and **db** services.

```yml
version: '3.8'
name: node-postgres-app
services:
    app:
        build:
            context: .
        dockerfile: Dockerfile
        volumes:
            - '..:/workspaces:cached'
        command: sleep infinity
        network_mode: 'service:db'
    db:
        image: 'postgres:latest'
        restart: unless-stopped
        volumes:
            - 'postgres-data:/var/lib/postgresql/data'
        environment:
            POSTGRES_USER: postgres
            POSTGRES_DB: postgres
            POSTGRES_PASSWORD: postgres
volumes:
    postgres-data: null
```

* **name:** Sets the name to ensure containers are properly identified under a specific project name.

* **app service:** This container is used for development. It builds from a Dockerfile and mounts the project directory as a volume. The command is overridden to keep the container alive (**sleep infinity**), and it shares the network stack with the **db** service (**network\_mode: service:db**), which simplifies access to the database.

* **db service:** This container runs PostgreSQL and is configured with environment variables for the user, password, and database name. The database data is persisted using a Docker named volume (**postgres-data**).

## Iterating and Rebuilding

After modifying the devcontainer.json file, you must rebuild your container to apply the changes. You can initiate a rebuild from VS Code using the **Gitpod Flex: Rebuild Container** command. During this process, Gitpod will disconnect your session, then automatically reconnect you once the rebuild is complete.

You can also rebuild your environment from the terminal using the Gitpod CLI. For instance, to trigger a rebuild from your environment, use:

```sh
gitpod environment devcontainer rebuild
```

### Recovery mode

If an errors occur when the devcontainer is started during a rebuild, Gitpod enters **recovery mode**. This allows you to examine environment logs (use the **Gitpod Flex: Show Environment Logs** command in VS Code), adjust the devcontainer.json file to resolve issues, and attempt the rebuild again.

## Environment Isolation Considerations

The Dev Container runs in an isolated Linux VM. Although the VM is part of the environment, the content and structure of the host is not customizable and may change at any time. Relying on the structure or contents of the underlying host impacts the portability and stability of your devcontainer configuration. It's crucial to respect this isolation to maintain portable and reliable Dev Container configurations:

* Use **initializeCommand** by avoiding adding dependencies to the VM.

* Opt for named volumes instead of bind mounts, as Docker controls them.

* Consider that "**localEnv**" in parameter expansion refers to the host VM, not your local machine, even when you are running locally.

### Host Network Stack

By default, the dev container network is isolated from the VM. However, you can configure the devcontainer to use the host's network stack, which is necessary for [port sharing](/flex/integrations/ports).

* For a single container, add `--network=host` in the `.devcontainer.json` file:
  ```json
  "runArgs": ["--network=host"]
  ```
* For multiple containers, use `network_mode: host` in the `docker-compose.yml` file:
  ```yml
  network_mode: host
  ```

## Using Private Container Images

<Warning>
  {' '}

  Currently, basic authentication (username/password) is supported for most registry types. AWS ECR is also supported only when using AWS EC2 runners.
</Warning>

If your Dev Container configuration uses private container images with basic authentication, you'll need to configure authentication credentials in your project's secrets:

1. Go to your Project Settings > Secrets
2. Create a new Container Registry secret with the appropriate registry URL and credentials. For detailed instructions, see the [Secrets documentation](/flex/secrets#types-of-secrets).
3. The environment will automatically authenticate with the registry using the credentials you provided.

<Note>
  {' '}

  If your workflow requires pulling additional private images from within your environment, your Dev Container image should include Docker CLI for most private registries, or Docker CLI and AWS CLI specifically for ECR registries. Without these tools, you may see a warning in your environment creation dashboard and won't be able to access the private registry from inside your environment.
</Note>

## References

* Refer to [containers.dev/implementors/json\_reference/](https://containers.dev/implementors/json_reference/) for the reference documentation of devcontainer.json format. This resource provides detailed information about attributes, lifecycle hooks, and other essential aspects of Dev Containers.

* For a comprehensive list of pre-built development container images that can be used as a starting point for your projects, visit [github.com/devcontainers/images](https://github.com/devcontainers/images). These images are maintained by the Dev Containers project and are designed to work well with VS Code and other Dev Container-compatible tools.

* While Gitpod doesn't allow opening a Dev Container using [the Dev Containers](marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension in VS Code, it leverages its editing experience and customizations. You can find more information about this, as well as generally applicable advice, at [code.visualstudio.com/devcontainers/containers](https://code.visualstudio.com/devcontainers/containers). Be aware that not everything is applicable given the isolated nature of Gitpod environments. For general best practices on working with Dev Containers, visit [containers.dev/guides](https://containers.dev/guides).
