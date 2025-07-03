# Automations

Automations enable programmable tasks and services that integrate directly into your development environment. They let you create self-service actions for various development workflows:

* **Setup**: Seed databases, provision infrastructure, or authenticate with cloud accounts
* **Operations**: Transform runbooks into one-click self-service actions
* **Editor interfaces**: Start servers such as Jupyter notebooks
* **Policies**: Execute security or scanning tools
* **AI workflows**: Configure AI agents or code assistants

<Frame caption="Environment details with Automations">
  <img src="https://www.gitpod.io/images/docs/flex/introduction/environment-details.png" />
</Frame>

## Configuration

Automations are defined in a YAML file located at `.gitpod/automations.yaml` in your repository. This file can live alongside your source code, in another repository, or any location accessible from the development environment.

Automations are organized into two categories:

* **Services**: Long-running processes that provide functionality to your environment
* **Tasks**: One-off commands that perform specific actions

## Example Configuration

Here's a simple example of an Automations configuration file:

```yaml
services:
    database:
        name: PostgreSQL
        commands:
            start: docker run postgres
tasks:
    run-unit-tests:
        name: Runs unit tests
        command: go test -v ./...
```

## Triggering Automations

Automations can be triggered in three ways:

1. **Manually through the UI**: Click on the automation in the Gitpod interface
2. **Via command line**: Execute automations using the CLI
3. **Automatically**: Trigger based on environment lifecycle events (e.g., when a Dev Container starts)

Each automation type has a corresponding UI element in the Gitpod interface, making them easily discoverable and accessible.

## Access Control

Anyone with access to an environment can create and run automations within that environment. Administrators cannot access other users' environments and therefore cannot create or run automations in those environments.

See the [examples](/flex/configuration/automations/examples) section for more detailed use cases and implementation patterns for Automations.
