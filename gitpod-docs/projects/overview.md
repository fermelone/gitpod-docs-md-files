# Projects

Projects in Gitpod allow you to create standardized development environments across your organization. By defining consistent settings for repositories, runners, and environments, projects enable team members to create fully configured environments with just one click.

## What are Projects?

A project in Gitpod serves as a blueprint for development environments, connecting a specific repository with predefined configurations. This ensures all team members work with the same standardized setup, eliminating "works on my machine" problems.

Projects provide several key benefits:

* **One-click environment creation** with consistent configuration
* **Standardization** of development environments across your organization
* **Automatic secret and environment variable management**
* **Time savings** by eliminating manual environment setup
* **Team collaboration** through shared project configurations

## Prerequisites

Before creating a project, ensure you have:

* Organization administrator permissions
* At least one runner set up in your organization

## Creating a Project

To create a new project:

1. Navigate to your organization dashboard at [https://app.gitpod.io](https://app.gitpod.io)
2. If you have no existing projects, you'll see the "No projects" screen
3. Click **Create project**

<Frame caption="No projects screen">
  <img src="https://www.gitpod.io/images/docs/flex/projects/no-projects.png" alt="No projects screen showing a Create project button" />
</Frame>

4. Enter the repository URL for your project
5. Provide a descriptive project name
6. Click **Continue**

<Frame caption="Create project - Initial setup">
  <img src="https://www.gitpod.io/images/docs/flex/projects/create-project.png" alt="Project creation screen with repository URL and name inputs" />
</Frame>

7. Configure your project settings:
   * Select an **Environment Class** (determines the compute resources)
   * Choose a **Dev Container configuration** or set up **Automations**
   * Click **Create project**

<Frame caption="Configure project settings">
  <img src="https://www.gitpod.io/images/docs/flex/projects/configure-project.png" alt="Project configuration screen with environment class selection" />
</Frame>

## Project Configuration Options

### Repository URL

The Git repository that will be cloned when an environment is created from this project.

### Environment Class

Defines the compute resources (CPU, memory, storage) allocated to environments. Each runner can have multiple environment classes configured, but a project can currently only use one environment class.

### Dev Container Configuration

Specifies how the development container should be configured, including:

* Base image
* Extensions
* Environment variables
* Port forwarding rules

### Automations

Powerful tools that go beyond Dev Container configuration to define, automate, and share common workflows:

* Run services (long-running processes) and tasks (one-off actions)
* Automate database provisioning, test runs, or cloud authentication
* Define complex workflows in YAML configuration files
* Update via the Gitpod CLI

## Managing Existing Projects

After creating a project, you can modify its configuration at any time:

1. Navigate to your organization's projects list
2. Select the project you want to modify
3. Use the settings panel to update configuration options including:
   * Dev Container configuration
   * Automations
   * Secrets and environment variables

You can also activate projects (to share with your organization) or deactivate them when they're no longer relevant.

## Limitations and Troubleshooting

* Projects currently support only one environment class. If you need a project to run in different regions (on different runners), you must set up multiple projects
* Projects don't yet have built-in support for multi-repo configurations, though they are supported through custom configurations

## Next Steps

After creating a project, you can:

* Create an environment from your project
* Share the project with your team
* Configure additional automations
* Add project-specific secrets

For more detailed information on specific project features, refer to the [Dev Container Configuration](/flex/configuration/devcontainer/overview) and [Automations](/flex/configuration/automations/overview) documentation.
