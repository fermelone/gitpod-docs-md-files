# Configuring Automations

> Explore Gitpod's automation features: Services and Tasks. Learn how to configure long-running services and execute specific tasks to streamline your development workflow. Understand execution options, dependencies, and best practices for efficient environment management.

# Basic configuration

When an environment is created the system loads Automations from the default file: `.gitpod/automations.yaml` relative to your repository root. You can change this location using [Projects](/flex/projects). An `automations.yaml` consists of services and tasks defined at the root level, for example:

```yaml
services: ...

tasks: ...
```

Services and tasks are a map where the key serves as reference for the corresponding item. When looking at task dependencies their use becomes clear.

See [reference](/flex/configuration/automations#reference) for a full example.

## Services in the automations.yaml

Example workflow:

```yaml
services:
    database:
        name: PostgreSQL
        description: The backend database
        triggeredBy:
            - postEnvironmentStart
        commands:
            start: 'docker run --rm -t --name database postgres:latest'
    redis:
        name: Redis
        description: Our message bus
        triggeredBy:
            - postEnvironmentStart
        commands:
            start: >-
                docker run --rm -t --name redis -p 6379:6379
                redis/redis-stack-server:latest
    backend:
        name: Application Backend
        description: The application backend
        triggeredBy:
            - postEnvironmentStart
        commands:
            start: cd backend && go run main.go
```

## Tasks in the automations.yaml

Example workflow:

```yaml
tasks:
    buildAll:
        name: Build All
        description: builds all code
        command: go build .
    runUnitTests:
        name: Runs unit tests
        command: go test -v ./...
    validate:
        name: Validate
        description: Builds and tests the code
        triggeredBy:
            - postEnvironmentStart
        dependsOn:
            - buildAll
            - runUnitTests
```

## Iterating on Automations

You can iterate on Automations using the [CLI](/flex/cli) which is available by default in every Gitpod environment. The CLI can

* reload the Automations file using:

```sh
gitpod automations update [optional-path-to-automations.yaml]
```

* start a task or service:

```sh
gitpod automations service start ...
gitpod automations task start ...
```

## Using Automations outside of an environment

The CLI commands to interact with an environment’s Automations are also available outside of an environment. The following snippet brings up an environment, adds a task, runs it, waits for the task to complete and brings the environment back down again:

```sh
# gitpod env create will set the environment context to the newly created env
gitpod env create https://github.com/some/repo

# add the task to the environment
cat <<EOF | gitpod automations update -
tasks:
  build:
    command: go build ./...
EOF

# run it
gitpod automations task start build

# stop the environment
gitpod env stop
```
