# Gitpod Desktop

> Run Gitpod environments locally on your Apple silicon Mac with Gitpod Desktop

Gitpod Desktop is the fastest and easiest way to run and recreate cloud development environments locally on your Apple silicon Mac. It provides a seamless development experience with the benefits of local computing resources.

## Benefits of Gitpod Desktop

* **Local Performance:** Harness the full power of your Apple silicon Mac.
* **Cost Efficiency:** Use your local machine resources without incurring additional cloud computing costs.
* **Work Offline:** Continue working in already-running environments even when you lose internet connectivity.
* **Resource Isolation:** Run development environments in isolation from your host system for improved security and dependency management.
* **Easy Setup:** One-click environment setup without complex virtualization configuration.
* **Consistent Experience:** Enjoy the same reliable, reproducible environments whether working locally or in the cloud.

## Prerequisites

* **Operating System**: macOS Sonoma or later
* **CPU**: Apple M1 chip or newer (Apple silicon)
* **RAM**: 16GB or more
* **Architecture**: Apple silicon (ARM-based Macs)

## Download and Install

1. Visit [app.gitpod.io](https://app.gitpod.io/) and look for the download link in the navigation bar
2. Alternatively, download directly from [gitpod.io/gitpod-desktop/download](https://www.gitpod.io/gitpod-desktop/download)
3. Install the application on your Mac

<Frame caption="Download link in the app.gitpod.io navigation bar">
  <img src="https://www.gitpod.io/images/docs/flex/getting-started/download-desktop-app.png" />
</Frame>

## First-Time Setup

When you first launch Gitpod Desktop, the application will:

1. Verify and configure the macOS runner
2. Set up the file system (this may take several minutes)
3. Display installation progress
4. Prompt you to authenticate with your Gitpod account
5. Guide you through Git authentication setup

## Create Your Environment

Once the setup is complete:

1. In the sidebar, click **Create an environment**
2. Paste a public or private repository URL
3. Click **Create environment**

<Frame caption="Enter your repository URL to create a new environment">
  <img src="https://www.gitpod.io/images/docs/flex/getting-started/insert-repository-url.png" />
</Frame>

## Choose Gitpod Desktop

To run your environment locally:

1. When prompted to select an environment class, choose **Gitpod Desktop**
2. Your local Gitpod Desktop application will begin setting up the environment
3. The setup process will pull necessary container images and configure your workspace

<Frame caption="Select Gitpod Desktop as your environment class">
  <img src="https://www.gitpod.io/images/docs/flex/getting-started/select-environment-class.png" />
</Frame>

## Git Authentication

For accessing repositories (especially private ones), Gitpod Desktop provides several authentication options:

1. **Automatic detection**: The runner checks your local credential manager for existing Git tokens
2. **Manual token entry**: If no token exists, you'll be prompted to provide a Personal Access Token (PAT)
3. **Token management**: Manage your PATs under Settings → Git Authentication
4. **Token refresh**: Authentication tokens are automatically refreshed when environments restart

For self-hosted source control providers, organization administrators must configure them in organization settings first.

## Features and Limitations

### Key Features

* Uses your local machine resources at no additional cloud cost
* Built-in Linux virtualization optimized for Apple Silicon
* One-click setup with full workload isolation
* Limited offline capabilities for already-running environments
* Organization administrators can disable local runners

### Limitations

* No port sharing available (unlike cloud runners)
* Currently only available for Apple silicon Macs

## Troubleshooting

If you encounter issues with Gitpod Desktop:

* **Runner installation failures**: Verify system requirements and macOS version
* **Account switching issues**: Only one runner can be active at a time, tied to a single organization
* **Git authentication problems**: Check your credentials or generate a new PAT
* **Unexpected runner failures**: Restart the application or reset the runner

For persistent issues:

1. Collect logs through Help → Troubleshooting → Collect Logs and Diagnostics
2. Contact support through the support chat
3. If needed, perform a clean uninstall by following the instructions in the support documentation

## Advanced Configuration

* **Organization settings**: Administrators can control local runner usage through Settings → Runners → Gitpod Desktop
* **Repository access**: Administrators can configure repository access to source control providers
* **Git authentication**: Users can configure and manage Git authentication settings
* **Cache management**: Clear shared cache for Docker images and builds as needed
* **Preview builds**: Advanced users can switch between Stable and Insiders (preview) builds

## Next Steps

* Learn about [environment configuration](/flex/configuration) to customize your development setup
* Explore [VS Code extensions](/flex/vscode-extensions) to enhance your development environment
* Check out how to [switch between local and cloud environments](/flex/switching-environments) for different workflows

For additional help, visit the [Gitpod Community](https://community.gitpod.io/) or [contact support](https://www.gitpod.io/contact).
