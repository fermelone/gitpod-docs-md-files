# Gitpod Desktop

Gitpod Desktop is the fastest and easiest way to run and recreate cloud development environments locally. It is currently available for Apple silicon users.

<Frame caption="Getting Started">
  <img src="https://www.gitpod.io/images/docs/flex/desktop/getting_started.png" />
</Frame>

## Benefits

* Run Dev Containers locally, replacing Docker Desktop for local development optimized for Apple Silicon, providing native-like Linux development without the overhead.
* One-click setup, full workload isolation, and the ability to "break it, forget it" - iterate quickly without fear of polluting your system.
* Leverage your local machine's resources for free
* Easily share your configured environments across your team to benefit from the automation and standardization of cloud development environments on your own hardware.
* Through Automations, get an optimized developer experience to launch environments and common development workflows through Gitpod Automations.
* Stay productive with offline capability and built-in disaster recovery support, seamlessly switching between local and cloud development as needed.

## Setup

### Download

1. Download Gitpod Desktop for Apple Silicon [here](https://www.gitpod.io/gitpod-desktop/download)
2. Open `Gitpod.dmg` and drag `Gitpod.app` into the Applications folder
3. Launch Gitpod Desktop from the Applications folder

You can also find it in the Gitpod dashboard at [app.gitpod.io](https://app.gitpod.io).

<Frame caption="Download Gitpod Desktop">
  <img src="https://www.gitpod.io/images/docs/flex/getting-started/download-desktop-app.png" />
</Frame>

### Install Runner

When you first launch Gitpod Desktop, it will guide you through a simple setup process:

1. The app will verify and configure the macOS runner (used to run [environments locally](#local-environments))
2. Wait for the installation to complete
   * Note: The "Setting up file system" step may take several minutes
   * The progress will show you the current status

<Frame caption="Install macOS runner">
  <img src="https://www.gitpod.io/images/docs/flex/desktop/installation.png" />
</Frame>

<Tip>
  {' '}

  If you have trouble installing, please check the [troubleshooting guide](#runner-installation-failure).{' '}
</Tip>

## Authentication

To use Gitpod Desktop, you'll need to connect it with your Gitpod account:

1. When you first open the app, click **Sign into Gitpod** in the prompt window. This will open your default browser.
   <Frame caption="Authentication Prompt">
     <img src="https://www.gitpod.io/images/docs/flex/desktop/auth.png" />
   </Frame>

2. Sign in using your Gitpod account credentials.
   <Frame caption="Complete Authentication Page">
     <img src="https://www.gitpod.io/images/docs/flex/desktop/auth_complete.png" />
   </Frame>

3. Once signed in, you can close the browser window and return to Gitpod Desktop.

4. Gitpod Desktop should open or you should see a dialog asking you to open.
   <Frame caption="Gitpod Desktop Open Dialog">
     <img src="https://www.gitpod.io/images/docs/flex/desktop/open.png" />
   </Frame>

<Tip>
  {' '}

  If you have trouble signing in, try to [sign out completely and try again](#switching-accounts).{' '}
</Tip>

## Local Environments

Gitpod Desktop automatically starts a macOS runner for the current organization, managing local environments.

### Git Authentication

Local environments require Git access to clone repositories. Here's how authentication works:

1. **Git Credentials:** The runner automatically checks your local credential manager for an existing Git token. If found, it's used immediately. Tokens are automatically refreshed when environments restart to maintain access.
2. **Personal Access Token (PAT):** If no token exists, Gitpod will prompt you to provide a PAT when creating an environment first time. You can manage your PAT under `Settings` -> `Git Authentication`. Click `Authenticate and Create` to proceed.
   <Frame caption="Gitpod Desktop Open Dialog">
     <img src="https://www.gitpod.io/images/docs/flex/desktop/git_auth.png" />
   </Frame>
3. **Connect to Source Control:** Gitpod Desktop will initiate a connection to your source control provider (e.g., GitHub). Follow along the instructions to grant access to your repositories.
   <Frame caption="Connect to GitHub">
     <img src="https://www.gitpod.io/images/docs/flex/desktop/github_connect.png" />
   </Frame>
4. **Self-Hosted SCM Providers:** If you use a self-hosted source control provider, administrators must configure it in the organization settings. Members can then authenticate using PATs. See [Configuring Repository Access](#configuring-repository-access).

<Tip>
  {' '}

  If you encounter Git access issues, try to [invalidate Git authentication](#invalidate-git-authentication).{' '}
</Tip>

### Runner Lifecycle

Each macOS runner is tied to a single organization, and only one runner can be active at a time.

Here's how it works:

* **Stopping the Runner:** Stops all associated local environments.
* **Quitting Gitpod Desktop:** Automatically stops the runner.
* **Switching Organizations:** The current organization's runner is stopped. The new organization's runner is started.
* **Restarting Gitpod Desktop:** Starts the runner again.
* **Restarting Environments:** Upon restarting Gitpod Desktop, you can start local environments again.

### Shared Cache

Local environments use a shared cache for Docker images and builds stored on your local machine. This cache speeds up the creation of new environments and the rebuilding of existing ones.

To clear the cache, select "Help" > "Troubleshooting" > "Clear Cache and Restart" from the menu bar.

Clearing the cache can be useful if the caches are corrupted or you want to start fresh.

## Organization Settings

### Disabling Local Environments

Organization administrators can control the use of local runners (Gitpod Desktop) across their organization:

1. Navigate to Settings -> Runners -> Gitpod Desktop in your organization settings
2. Use the toggle to enable or disable local runners for your organization

<Tip>
  {' '}

  Disabling local runners will immediately stop all running environments on Gitpod
  Desktop and prevent members from starting new local environments. Before disabling,
  notify organization members as they will lose access to any active work in local
  environments.{' '}
</Tip>

### Configuring Repository Access

Administrators can configure repository access to source control providers for local runners:

1. Navigate to Settings -> Runners -> Gitpod Desktop
2. Configure authentication for source control providers:
   * `github.com` and `gitlab.com` are configured by default
   * For self-hosted SCM providers, administrators must add them here before members can authenticate
   * Members can then use **Personal Access Tokens** (PAT) to authenticate with configured providers, if they don't have existing Git credentials on their machine

See [Source Control](/flex/source-control) for more information on configuring source control providers.

<Frame caption="Desktop Settings">
  <img src="https://www.gitpod.io/images/docs/flex/desktop/desktop_settings.png" />
</Frame>

## Updating

Gitpod Desktop releases new versions weekly, delivering the latest improvements and features. While the application updates automatically, you can manually check for updates by selecting "Gitpod" > "Check for Updates..." from the menu bar.

<Frame caption="Check for Updates">
  <img src="https://www.gitpod.io/images/docs/flex/desktop/check_for_updates.png" />
</Frame>

After downloading a new version, Gitpod Desktop will prompt you to restart the application to apply the update.

### Checking Your Version

To check your current version, select "Gitpod" > "About Gitpod Desktop" from the menu bar.
Click "Copy" to save the version information to your clipboard, which can be helpful when [seeking support](#report-issue).

<Frame caption="About Gitpod Desktop">
  <img src="https://www.gitpod.io/images/docs/flex/desktop/about.png" />
</Frame>

### Switching to Insiders

<Warning>
  {' '}

  Switching to Insiders is an advanced feature that may cause instability or break
  your Gitpod Desktop installation. Only proceed if you understand the risks.{' '}
</Warning>

Gitpod Desktop provides nightly builds for testing and feedback purposes. While we recommend using the stable version, accessing Insiders builds can be useful when you want to preview upcoming features before their official release.

To switch to Insiders:

1. Quit Gitpod Desktop
2. Open your terminal and run: `echo "{\"quality\":\"insider\"}" > ~/Library/Gitpod/argv.json`
3. Launch Gitpod Desktop
4. Check for updates to install the latest version
5. Verify the installation by [checking your version](#checking-your-version). You should see "Insider" in the version information.

### Switching to Stable

To return to the stable version from Insiders, follow these steps:

1. Quit Gitpod Desktop
2. Open your terminal and run: `echo "{\"quality\":\"stable\"}" > ~/Library/Gitpod/argv.json`
3. Launch Gitpod Desktop
4. Check for updates to install the latest version
5. Verify the installation by [checking your version](#checking-your-version). You should not see "Insider" in the version information.

To switch back to the stable version, you must wait for a newer stable release to become available, as Gitpod Desktop does not support downgrading to previous versions.

To revert to a previous stable version:

1. [Uninstall](#uninstall) your current version of Gitpod Desktop
2. If experiencing compatibility issues, perform a [clean uninstall](#clean-uninstall)
3. [Setup](#setup) Gitpod Desktop again

## Uninstall

To uninstall Gitpod Desktop, select "Help" > "Troubleshooting" > "Uninstall" from the menu bar.
This action removes both the local runner and the application.
For a complete removal of all Gitpod Desktop data, including local environments and settings, perform a [clean uninstall](#clean-uninstall).

### Clean Uninstall

<Warning>
  {' '}

  Performing a clean uninstall will remove all Gitpod Desktop data, including your
  local environments and settings.{' '}
</Warning>

1. Begin by [resetting Gitpod Desktop data](#reset-data).
2. When Gitpod Desktop restarts, do not proceed with the installation. Instead, [uninstall](#uninstall) the application.

## Troubleshooting

### Report Issue

If you encounter any issues:

1. Ensure you are [up-to-date](#updating).
2. Restart Gitpod Desktop, as some errors may be temporary.
3. If you don't have any sensitive local environments, try to [reset the data](#reset-data). This can sometimes resolve issues.
4. If the issue persists, collect diagnostics using "Help" > "Troubleshooting" > "Collect Logs and Diagnostics". Review them for system-specific problems.
5. Start a support chat with us using the bubble icon in the bottom right corner of the application. If it's not available in Gitpod Desktop, use Gitpod from the browser.
   <Frame caption="Report Issue">
     <img src="https://www.gitpod.io/images/docs/flex/desktop/report_issue.png" />
   </Frame>
6. Describe what happened, what you did, and what you expected. Upload the logs and diagnostics, and include any relevant screenshots.

<Warning>
  {' '}

  Be cautious when sharing logs online, as they may contain sensitive information.{' '}
</Warning>

### Reset Data

Resetting data permanently removes all Gitpod Desktop data, including local environments and user settings.
This action is helpful when Gitpod Desktop is not functioning correctly or when you want to start with a clean installation.

To reset data, select "Help" > "Troubleshooting" > "Reset and Restart" from the menu bar.

### Runner Installation Failure

If you encounter installation errors:

1. Check the error message details
2. Make any required system adjustments
3. Restart the installation process
4. If problems continue, [submit an issue report](#report-issue)

<Frame caption="Installation Failure">
  <img src="https://www.gitpod.io/images/docs/flex/desktop/installation_failure.png" />
</Frame>

### Switching Accounts

To switch to a different Gitpod account, follow these steps:

1. Logout from Gitpod Desktop
2. Logout from your current Gitpod account in your default browser
3. Launch Gitpod Desktop and complete the authentication process with your new account credentials
4. If problems continue, [submit an issue report](#report-issue)

### Invalidate Git Authentication

If you're experiencing Git authentication issues, try these steps:

1. Verify if you are using a Personal Access Token (PAT) for runner authentication in `Settings` > `Git Authentication`.
2. If using PAT, invalidate it by clicking `Remove`. Remember to also revoke the PAT in your source control provider, e.g. GitHub.
   <Frame caption="Invalidate PAT">
     <img src="https://www.gitpod.io/images/docs/flex/desktop/git_auths.png" />
   </Frame>
3. If not using PAT, verify your Git credentials by attempting to clone the repository on your local machine. Update credentials if authentication fails.
4. Restart your local environment to apply the changes.

### Unexpected Runner Failure

If your runner unexpectedly fails:

1. Check the error message for specific details
2. Restart Gitpod Desktop to attempt automatic recovery
3. If the issue persists, try [resetting the data](#reset-data)
4. If problems continue, [submit an issue report](#report-issue)

<Frame caption="Unexpected Runner Failure">
  <img src="https://www.gitpod.io/images/docs/flex/desktop/unexpected_failure.png" />
</Frame>
