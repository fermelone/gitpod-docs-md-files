# Configure a dev environment

With Gitpod, you have a fully configured development environment that starts in a single-click. We achieve this through configuring a Dev Container and Automations. This guide takes you through configuring your first environment.

<Note>
  {' '}

  **Pre-requisites** <br /> Install [Gitpod Desktop or the AWS Runner](/flex/getting-started)
  before completing this guide.
</Note>

{/* <!-- <Frame caption="">
  <img src="https://www.gitpod.io/images/docs/flex/projects/create-env.png" />
  </Frame> --> */}

{/* <!-- TODO: Image --> */}

**Steps**

* [Configure development environment](#configure-development-environment)
  * [Create an environment](#create-an-environment)
  * [Configure your Dev Container](#configure-your-dev-container)
  * [Configuring Automations](#configuring-automations)
  * [Publishing your project](#publishing-your-project)
  * [What next?](#what-next)

## Create an environment

Start by choosing a repository and environment class to launch your first environment. Once launched we'll then configure the environment and save it as a project. This will mean that you've created a blueprint so your team can also self-serve a one-click experience for their own fully prepared development environment.

<Frame>
  <img src="https://www.gitpod.io/images/docs/flex/getting-started/select-environment-class.png" />
</Frame>

## Configure your Dev Container

Let's get started with Dev Container to eliminate the need to manually install tools and dependencies. If you don't have an existing devcontainer in your repository Gitpod will create a basic example file for you in your environment.

A basic Dev Container example stored in `.devcontainer/devcontainer.json`

```json
{
	"name": "Node.js Dev Container",
	"image": "mcr.microsoft.com/devcontainers/javascript-node:0-18",
	"customizations": {
		"vscode": {
			"settings": {},
			"extensions": ["dbaeumer.vscode-eslint"]
		}
	},
	"remoteUser": "node"
}
```

As you make changes you can rebuild your environment by running:

`gitpod environment devcontainer rebuild`.

See [devcontainer](/flex/configuration/devcontainer) for more.

## Configuring Automations

Automations go beyond Dev Container and are a powerful way to define, automate and share common workflows that you perform with your development environment

Automations are defined in configuration YAML files and updated via the Gitpod CLI that comes preinstalled in your environment.

For example:

* Seeding a database
* Running a unit test.

See [automations - examples](/flex/configuration/automations/examples) for many more automation examples.

An example Automations file example stored in `.gitpod/automations.yaml`

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
    install-dependencies:
        name: Install dependencies
        command: npm install
        triggeredBy:
            - postDevcontainerStart
            - manual
```

When you’re done run `gitpod automations update` to register your Automations with Gitpod.

See [automations](/flex/configuration/automations) for more.

## Publishing your project

When done commit both your devcontainer and automation configuration files and hit publish on your project in Gitpod. You’ve now set up a fully-configured project that is your blueprint for a fully-configured development environment and it’s now shared with your team inside your Gitpod organization.

## What next?

Now that you're done, why not take a look at:

{/* <!-- TODO: Add link for Gitpod Desktop --> */}

* Setting up an [AWS Runnner](/flex/runners/aws) or [Gitpod Desktop]() (if you haven't already)
* Further [optimizing your devcontainer](/flex/configuration/devcontainer/optimizing-startup-times)
* Exploring an [integration](/flex/integrations)
