# Optimizing your Environment

> Learn how to optimize your development environment for Gitpod. Discover tips and best practices for improving the startup time of your environment.

There are several ways to optimize the startup of your environment:

* **Place stable dependencies in the Dockerfile**: For tools that rarely change (e.g., build tools, system dependencies), include them directly in the custom Dockerfile.

* **Use prebuilt Docker images**: Build your image, and push it to a container registry. Reference this image in your devcontainer.json file to avoid rebuilding from scratch each time.

* **Enable dev container image cache**: For AWS runners, the [dev container image cache](/gitpod/runners/aws/devcontainer-image-cache) automatically caches built devcontainer images, significantly reducing startup times for environments with identical configurations.

* **Use [automations](../automations) for dynamic dependencies**: For frequently changing tools and dependencies, such as npm modules, use Automations to handle installations during the environment's startup process.

Gitpod environments may take some time to start initially, but they're quick to stop and restart after setup, and they automatically stop when disconnected. Here's how you can leverage these to speed up your workflows:

* **Reuse environments:** Accelerate recurring tasks by reusing environments. For instance, eliminate the need to repeatedly repopulate databases or download dependencies.

* **Use multiple environments:** Organize your work by maintaining separate environments for different tasks, such as code reviews and feature development for. This enables faster context switching within the same repository.
