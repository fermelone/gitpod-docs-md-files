# Overview

Gitpod fully supports [Development Containers](https://containers.dev/), allowing you to standardize development environments across your team. Define your setup in a `devcontainer.json` file to ensure consistent tools, dependencies, and configurations for all developers.

## Benefits

Using Dev Containers with Gitpod provides several advantages:

* **Standardized environments** across all team members
* **Consistent tooling** with precisely defined dependency versions
* **Isolated Linux VM environments**, even when running locally
* **Support for both single and multi-container** development setups
* **Version-controlled configuration** that lives with your codebase
* **Integration with VS Code** and other supported editors
* **Separation** of development environment from local machine configuration

## Configuration

### File Location

Place your `devcontainer.json` file in one of these standard locations:

* `.devcontainer/devcontainer.json`
* `.devcontainer.json`

### Basic Configuration Example

```json
{
	"name": "My Project",
	"image": "mcr.microsoft.com/devcontainers/base:ubuntu",
	"features": {
		"ghcr.io/devcontainers/features/node:1": {
			"version": "lts"
		}
	},
	"customizations": {
		"vscode": {
			"extensions": ["dbaeumer.vscode-eslint", "esbenp.prettier-vscode"],
			"settings": {
				"editor.formatOnSave": true
			}
		}
	},
	"forwardPorts": [3000, 8080]
}
```

This configuration:

* Uses a base Ubuntu image
* Adds Node.js LTS
* Includes ESLint and Prettier VS Code extensions
* Configures auto-formatting on save
* Forwards ports 3000 and 8080

## Multiple Dev Container Configurations

You can manage multiple Dev Container configurations using Gitpod's project feature. This allows you to define different environments for:

* Different branches or repositories
* Various development scenarios
* Specialized tasks requiring specific tools

## Migration from .gitpod.yml

If you're already using a `.gitpod.yml` file, Gitpod provides tools to convert your existing configuration to the Dev Container format. See our [migration guide](/flex/configuration/migrate-from-classic) for step-by-step instructions. Dev Containers offer a more standardized approach that works across multiple platforms and tools.

## Known Limitations

When using Dev Containers with Gitpod, be aware of these limitations:

* Platform-specific features may not work with Gitpod Desktop
* Conflicting features can cause build failures (Gitpod will display an error message)
* Some Dev Container commands might behave differently in Gitpod's environment
* When build errors occur, recovery mode is engaged, requiring manual intervention

## Recommended Images

Microsoft provides well-maintained Dev Container base images for popular development stacks:

* `mcr.microsoft.com/devcontainers/base:ubuntu` - Ubuntu base image
* `mcr.microsoft.com/devcontainers/javascript-node` - Node.js development
* `mcr.microsoft.com/devcontainers/python` - Python development
* `mcr.microsoft.com/devcontainers/dotnet` - .NET development
* `mcr.microsoft.com/devcontainers/java` - Java development
* `mcr.microsoft.com/devcontainers/go` - Go development

## Advanced Configuration

### Multi-Container Development

For more complex setups, you can define multiple containers using Docker Compose:

```json
{
	"name": "Multi-container App",
	"dockerComposeFile": "docker-compose.yml",
	"service": "app",
	"workspaceFolder": "/workspace",
	"customizations": {
		"vscode": {
			"extensions": ["ms-azuretools.vscode-docker"]
		}
	}
}
```

### Adding Custom Features

[Dev Container Features](https://containers.dev/features) are self-contained, shareable units of installation code and configuration that let you quickly add tooling, runtimes, or libraries to your development container.

You can add features to your Dev Container by adding them to the `features` section of your `devcontainer.json` file:

```json
{
	"features": {
		"ghcr.io/devcontainers/features/docker-in-docker:2": {},
		"ghcr.io/devcontainers/features/github-cli:1": {}
	}
}
```

Gitpod works well with many Dev Container Features, especially official ones that are designed with remote development environments in mind. Linux-based runners generally provide best compatibility with most Dev Container Features. Here's what you should know:

* Community-supported features might require additional testing, as they may have been developed without specific consideration for compatibility.
* When using the Gitpod Desktop's Mac runner, some features might not work right away with the Rosetta virtualization layer. [See troubleshooting section](#troubleshooting)
* Feature behavior can vary depending on base images, other installed features, and specific configurations in your setup.

## Troubleshooting

If your Dev Container fails to build:

1. Check the Gitpod console for specific error messages
2. Verify that all specified features are compatible

   <Expandable title="features that require extra work on Gitpod Desktop's Mac runner">
     * ghcr.io/devcontainers/features/docker-in-docker:2

       Disabling `moby` can be required to build this features. Alternatively, you can provide Docker CE through the image of your dev container. [Learn more](https://github.com/devcontainers/features/tree/main/src/docker-in-docker#limitations)

     * ghcr.io/devcontainers/features/docker-outside-of-docker:1

       Disabling `moby` can be required to build this features. Alternatively, you can provide Docker CE through the image of your dev container. [Learn more](https://github.com/devcontainers/features/tree/main/src/docker-outside-of-docker#limitations)

     * ghcr.io/devcontainers/features/kubectl-helm-minikube:1

     * ghcr.io/devcontainers/features/nix:1

     * ghcr.io/devcontainers/features/oryx:1

     * ghcr.io/devcontainers/features/terraform:1

     * ghcr.io/devcontainers-contrib/features/yamllint:2

       The installation fails due to platform mismatch. It's possible to set `platform=linux/arm64` to build this feature, but the recommendation would be to install `yamllint` in you custom container image.
   </Expandable>
3. Ensure image versions are correctly specified
4. Try rebuilding in recovery mode to debug the issue

## Next Steps

* Explore the full [Dev Container specification](https://containers.dev/implementors/spec/) for advanced configurations
* Check out the [Dev Container Feature catalog](https://containers.dev/features) for additional tools and utilities
* Learn about [Gitpod projects](/flex/projects) to manage multiple environments
