# Development Containers

> Development Containers (or Dev Containers) allow you to use a container as a full-featured development environment. It can be used to run an application, separate tools, libraries, or runtimes needed for working with a codebase, and to aid in continuous integration and testing. Dev containers can be run locally or remotely, in a private or public cloud, in a variety of supporting tools and editors.

# Development Containers

<Info>
  {' '}

  "A Development Container (or Dev Container for short) allows you to use a container
  as a full-featured development environment. It can be used to run an application,
  separate tools, libraries, or runtimes needed for working with a codebase, and
  to aid in continuous integration and testing. Dev containers can be run locally
  or remotely, in a private or public cloud, in a variety of supporting tools and
  editors." - [containers.dev](https://containers.dev/)
</Info>

Gitpod offers seamless support for [Dev Containers](https://containers.dev/), allowing you to standardize and automate your development environment across teams and projects. By defining your environment in a devcontainer.json file, Gitpod ensures that everyone on your team works with the same configuration, regardless of their local setup.

## Configuration Locations

Gitpod will automatically detect your Dev Container configuration in standard locations:

* `.devcontainer/devcontainer.json`
* `.devcontainer.json`

You can also specify custom paths when configuring Projects through the Gitpod UI.

## Image build caching

Gitpod provides efficient Docker image build caching on a per-project basis to optimize development workflows and reduce build times. This caching mechanism stores built images securely and reuses them across environments, significantly speeding up workspace creation.

### How it works

When you start a new workspace, Gitpod follows an intelligent caching strategy:

1. **Check for cached image**: First looks for a previously built image that matches your devcontainer configuration
2. **Pull from cache**: If found, pulls the cached image instead of rebuilding from scratch
3. **Build and cache**: If no cache exists, builds the image and stores it for future use
4. **Automatic management**: Cached images are automatically managed and cleaned up over time

### Key features

* **Project-Based Caching**: Images are cached per project, ensuring team members benefit from shared builds
* **Security & Isolation**: Each project has its own secure cache, preventing cross-project access
* **Automatic Operation**: Works transparently without requiring any configuration
* **Docker Layer Optimization**: Reuses Docker layers efficiently to minimize storage and transfer time

The caching system is particularly effective for teams working with similar devcontainer configurations, where subsequent workspace launches can be significantly faster by leveraging previously built images.

## Integration with Automations

Building on Dev Containers, Gitpod adds a powerful framework for running [Automations](/flex/introduction/automations) in your development environments. While Dev Containers define your base environment, we recommend using Automations instead of Dev Container lifecycle commands for setup tasks and workflows.

Automations allow you to set up self-service actions like seeding databases, automating testing, managing external infrastructure lifecycle, or launching AI assistants securely within your development environment.

## Example Dev Container

```json
{
	"name": "Node.js Dev Container",
	"image": "mcr.microsoft.com/devcontainers/javascript-node:18",
	"customizations": {
		"vscode": {
			"extensions": ["dbaeumer.vscode-eslint"]
		}
	}
}
```

{/* For detailed information about Dev Container configuration options, best practices, migration from Gitpod Classic, and troubleshooting, see our [Dev Containers Guide](/flex/reference/dev-containers). */}
