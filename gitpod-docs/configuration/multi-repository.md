# Multi-Repository Environments

> Learn how to work with multiple repositories in a single Gitpod environment

Gitpod supports working with multiple repositories in a single environment, enabling you to work on projects that span across different repositories. This guide explains how to set up multi-repository environments using either Dev Container configuration or Gitpod Automations.

## Using Dev Container Configuration

The Dev Container `onCreateCommand` allows you to clone additional repositories when your environment starts. This method is particularly useful when you want to maintain the repository setup as part of your Dev Container configuration.

Add an `onCreateCommand` entry to your `.devcontainer/devcontainer.json` file:

```json
{
  "name": "One extra repository",
  "image": "mcr.microsoft.com/devcontainers/base:ubuntu",
  "onCreateCommand": "git clone https://github.com/organization/second-repo.git"
}
```

For multiple repositories:

```json
{
  "name": "Multiple repositories",
  "image": "mcr.microsoft.com/devcontainers/base:ubuntu",
  "onCreateCommand": "git clone https://github.com/organization/second-repo.git && git clone https://github.com/organization/third-repo.git"
}
```

## Using Gitpod Automations

Alternatively, you can use Gitpod's [Automations](/flex/configuration/automations/overview) to clone additional repositories. This approach offers more flexibility and can be combined with other automation tasks.

Add a task to your `automations.yaml` file:

```yaml
tasks:
    build:
        name: Clone additional repositories
        command: |
            git clone https://github.com/organization/second-repo.git
            git clone https://github.com/organization/third-repo.git
        triggeredBy: ['postDevcontainerStart']
```

## Best Practices

When working with multiple repositories, consider the following best practices:

* Use SSH keys or personal access tokens for authentication with private repositories
* Organize repositories in a consistent directory structure
* Configure Git identity globally to ensure consistent commits across repositories

## Troubleshooting

Common issues you might encounter:

* **Authentication failures**: Ensure you have the correct permissions and authentication method
* **Path issues**: Use absolute paths when necessary
* **Repository not found**: Verify repository URLs and access permissions

## Working with Multiple Repositories

Once your environment is set up:

1. Navigate between repositories using the file explorer or terminal
2. Make changes in each repository independently
3. Commit and push changes to each repository separately

Example workflow:

```bash
cd ~/workspace/second-repo
# Make changes
git add .
git commit -m "Update feature X"
git push

cd ~/workspace/third-repo
# Make changes
git add .
git commit -m "Fix bug Y"
git push
```
