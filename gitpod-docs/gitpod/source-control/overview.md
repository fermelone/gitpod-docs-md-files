# Overview

Gitpod seamlessly integrates with major source control providers, enabling you to work with your code repositories directly within your Gitpod environments.

## Key Features

* **Automated Repository Cloning**: Your repositories are automatically cloned when you start a Gitpod environment
* **Full Branch Management**: Create, switch, and manage branches directly within your environment
* **Commit and Push**: Make changes and push them back to your repository without leaving Gitpod

## Supported Providers

Gitpod integrates with the following source control providers:

* [GitHub](/flex/source-control/github)
* [GitLab](/flex/source-control/gitlab)
* [Bitbucket Cloud](/flex/source-control/bitbucket)
* [Azure DevOps](/flex/source-control/azuredevops)

## Authentication

You can authenticate with your source control provider using:

* **OAuth**: For a streamlined authentication experience
* **Personal Access Tokens (PAT)**: For more granular control over permissions

## Security Architecture

Gitpod follows a secure architecture for source control integration:

* All source control interactions occur **only through the runner** on your infrastructure
* Gitpod's management plane **never has access** to your credentials or source code
* Your code and credentials remain exclusively within your control

Visit the provider-specific pages for detailed setup instructions and best practices.
