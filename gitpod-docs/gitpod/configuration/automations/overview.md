# Overview

> Explore Gitpod's automation features: Services and Tasks. Learn how to configure long-running services and execute specific tasks to streamline your development workflow. Understand execution options, dependencies, and best practices for efficient environment management.

Through [Dev Container](/flex/configuration/devcontainer) you specify your environment basics like base image and editor plugins. Automations go beyond Dev Container to provide **a powerful way to define, automate and share common tasks** you perform with your development environment, such as seeding databases or provisioning external infrastructure.

<Frame caption="Environment details with Automations">
  <img src="https://www.gitpod.io/images/docs/flex/getting-started/environment-details.png" />
</Frame>

Using Automations you can automate:

* **Setup** - Seed a database, provision infra or authenticate with a cloud account
* **Operations** - Turn your runbooks into one-click self-service actions
* **Editor interfaces** - Start up a server such as Jupyter notebook
* **Enforce policies** - Run security or scanning tools
* **AI workflows** - Configure AI agents or code assistants

See [examples](/flex/configuration/automations/examples) for more.

Automations are defined in configuration YAML files that can live alongside your source code, in another repo, or any location accessible from the development environment.

* [Automations](#automations)
  * [The two modes of Automations](#the-two-modes-of-automations)
  * [Services](#services)
    * [Service Configuration](#service-configuration)
  * [Tasks](#tasks)
  * [Triggers](#triggers)
    * [Available Triggers](#available-triggers)
    * [Runners vs. Gitpod Desktop behaviors](#runners-vs-gitpod-desktop-behaviors)
    * [Dependencies](#dependencies)
    * [Best Practices for Using Triggers](#best-practices-for-using-triggers)
  * [Reference](#reference)

## The two modes of Automations

Gitpod supports two primary types of Automations:

1. **[services](#services)** - for long-running processes like starting a server
2. **[tasks](#tasks)** - for performing one-off actions like executing unit tests

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

**Caption:** A minimal automation definition.

## Services

Services are **designed for long-running processes**. These are typically components that need to be continuously available throughout your development session.

Common examples include:

* Databases like PostgreSQL
* Caching systems such as Redis
* Your project's backend and frontend servers.

The key characteristic of a service is its persistent nature – it's not expected to terminate on its own but to remain active and ready for interaction as long as your development environment is running.

See [reference](#reference) for a full example.

### Service Configuration

Configuring a service involves defining up to three key commands:

* `start` (required) - The service itself. The process is expected to continue running until stopped. If this command fails (i.e. exits with a non-zero exit code), the service is considered failed.

* `ready` (optional) - Acts as a health check, determining when the service is fully operational and available for use. Gitpod executes this command periodically (once per second) until it exits with a status code of 0, indicating the service is ready. If you don't specify a `ready` command, Gitpod assumes the service is immediately available after the `start` command completes.

* `stop` (optional) - Defines a graceful shutdown procedure for your service. If omitted, Gitpod will send a `SIGTERM` signal to terminate the service when needed.

## Tasks

In contrast to services, **tasks are individual commands designed to perform specific, often one-off actions within your environment**.

Common examples include:

* Compiling code
* Executing test suites
* Populating a database with test data
* Authenticating with cloud services
* Resetting your local environment to a known state.

Tasks are typically short-lived, executing a defined set of operations and then terminating once complete. Tasks consist of a single command to be executed, however their power lies in their ability to be chained and dependent on other components of your environment.

Tasks will exit immediately if a command exits with a non-zero status code, and the task will be marked as failed. This behavior allows for proper error handling in automation pipelines and dependency chains. For example, if a task depends on another task that fails (exits with non-zero status), the dependent task will not be executed.

See [reference](#reference) for a full example.

### Stop a Task

A started task can be stopped prematurely, which will send a `SIGTERM` signal to the task's command (or any chained commands). Once the command has exited, the task will be marked as stopped.
If the command does not exit within 10 seconds, it will be forcefully terminated and the task run will be marked as failed.

## Triggers

Triggers are **the events that initiate the execution of Automations in your Gitpod environment**. This section covers the available triggers and explains their behavior.

### Available Triggers

Gitpod supports three main types of triggers for Automations:

* The `postEnvironmentStart` trigger activates every time the environment is started. This includes both the initial start of the environment and any subsequent restarts. It's particularly useful for operations that need to be performed consistently on every environment start, regardless of the underlying container state. For example, you might use this trigger to set up environment variables or check for updates to critical tools.

* The `postDevcontainerStart` trigger, on the other hand, is activated every time the devcontainer is started. This occurs during the first start of the environment and any subsequent devcontainer restarts, such as after a rebuild. This trigger is ideal for setup tasks that are specific to the devcontainer configuration, like initializing databases or compiling project-specific dependencies.

* The `manual` trigger provides a unique affordance in the user interface, allowing developers to start an action on demand. This trigger is particularly valuable for curating a set of actions that developers frequently perform. By using manual triggers, you can shape and refine the experience others will have in your Gitpod environment. For instance, you might create manual triggers for running tests, generating documentation, or deploying to a staging environment. This approach not only streamlines common tasks but also helps standardize processes across your team.

See [reference](#reference) for a full example.

### Runners vs. Gitpod Desktop behaviors

It's important to note that the behavior of these triggers can vary depending on the Gitpod runner being used. The AWS runner typically uses a suspend/resume model for environment management. When an environment is restarted on EC2, it usually resumes from a suspended state. In this scenario, `postDevcontainerStart` is not called on restart, but `postEnvironmentStart` is still triggered.

Gitpod Desktop takes a different approach. Instead of using suspend/resume, it reboots the entire environment on restart. This causes both `postDevcontainerStart` and `postEnvironmentStart` to run on every environment restart.

This intentional difference in behavior is designed to help recreate state that might be lost due to the lifecycle of individual elements in different environments. For AWS runners, the suspended state preserves most of the environment, so fewer reinitializations are needed. For Gitpod Desktop, the full reboot ensures a clean state each time, which may require more extensive reinitialization.

### Dependencies

Tasks can specify dependencies, allowing you to create sophisticated automation workflows. A task can depend on other tasks, ensuring that these dependencies are executed beforehand. This feature is particularly useful for setting up complex environments where certain operations must occur in a specific order.

It's important to note that task dependencies are re-evaluated and re-executed each time the main task runs. This ensures that your environment is always in the expected state before a task begins, even if it's run multiple times during a development session.

Each task execution is treated as an isolated event. This means that if you modify a task's definition while it's running, those changes won't affect the current execution. This isolation ensures consistency and predictability in your automation workflows.

### Best Practices for Using Triggers

When working with triggers, it's advisable to use `postEnvironmentStart` for tasks that should run on every start, regardless of the runner or whether it's a fresh start or a resume.

Use `postDevcontainerStart` for tasks specifically related to devcontainer setup or for operations that need to run after a full environment reboot. This could involve compiling dependencies or initializing databases.

The `manual` trigger is best used for discretionary tasks that developers might need to perform multiple times during a session, or for complex operations that don't need to run automatically. By thoughtfully implementing manual triggers, you can significantly improve the usability of your Gitpod environment for all team members.

## Reference

Automations are defined as YAML, in a [file](/flex/configuration/automations/basic-configuration) or [directly uploaded to the system](/flex/configuration/automations/generating-automations).

```yaml
# defines automation services (optional)
services:
    # serviceReference is an identifier for the service within the environment.
    # It is used when referencing the service, e.g. from the CLI.
    # It needs to only contain alphanumeric characters, underscores, and hyphens, and must be between 1 and 128 characters long.
    serviceReference:
        # Name is a required, human readable string.
        name: Human readable name
        description: Optional description providing more detail
        # triggeredBy lists all trigger that start the service. If none are provided the service isn't started automatically.
        # See below for a complete list of trigger.
        triggeredBy:
            - ...
        commands:
            # start is a mandatory command constitutes the service itself and is expected to continue running until stopped.
            # If this command fails (i.e. exits with a non-zero exit code), the service is considered failed.
            start: your-service-command
            # ready acts as a readiness check, determining when the service is fully operational and available for use.
            # Gitpod executes this command periodically (once per second) until it exits with a status code of 0, indicating the service is ready. # If you don't specify a ready command, Gitpod assumes the service is immediately available after the start command completes.
            ready: your-service-command --is-running
            # This optional command allows you to define a graceful shutdown procedure for your service.
            # If omitted, Gitpod will send a SIGTERM signal to terminate the service when needed.
            stop: killall your-service-command

# defines automation tasks (optional)
tasks:
    taskReference:
        # Name is a required, human readable string.
        name: Human readable name
        description: Optional description providing more detail
        # triggeredBy lists all trigger that start the service. If none are provided the service isn't started automatically.
        # See below for a complete list of trigger.
        triggeredBy:
            # postEnvironmentStart activates every time the environment is started, e.g. on first start
            - postEnvironmentStart
            # postDevcontainerStart activates every time the devcontainer is started, e.g. on first start or devcontainer rebuild
            - postDevcontainerStart
            # manual trigger provides a unique affordance in the user interface, allowing developers to start an action on demand.
            - manual
        # dependsOn expresses a dependency on another task which ensures that this other task runs before this one.
        dependsOn:
            - someOtherTask
        # command is the actual task command that gets executed. Gitpod will run this as a shell script, i.e. multiline input is possible
        command: |
            echo We are in the workspace directory: $PWD
            echo Let's go
```
