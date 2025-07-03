# Visual Studio Code

Gitpod seamlessly integrates with VS Code, allowing you to connect to your environments.
This guide will walk you through the setup process and provide tips for managing, troubleshooting, and recovering environments within VS Code.

<Frame caption="VS Code">
  <img src="https://www.gitpod.io/images/docs/flex/integrations/vs-code-desktop.png" />
</Frame>

## Prerequisites

Before starting, ensure that you have the following:

1. [VS Code](https://code.visualstudio.com/download) installed.
2. The [Gitpod Flex](https://marketplace.visualstudio.com/items?itemName=gitpod.gitpod-flex) extension for VS Code installed and enabled.
3. The [Remote - SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh) extension installed and enabled in VS Code.

> **Tip**: Keep your VS Code and extensions updated for the best experience.

## Opening an Environment

### VS Code

1. Start an environment in Gitpod

2. Open in **VS Code**

   * While the environment is starting, you can click the **Open in VS Code** button on the action bar. This button is available at any stage—even when the environment is not fully running yet.

     <Frame caption="Open from the Action Bar">
       <img src="https://www.gitpod.io/images/docs/flex/integrations/vscode/open_action_bar.png" />
     </Frame>

   * Alternatively, use the **VS Code** icon from the sidebar to launch the environment.

     <Frame caption="Open from the Side Bar">
       <img src="https://www.gitpod.io/images/docs/flex/integrations/vscode/open_sidebar.png" />
     </Frame>

3. VS Code should open or you should see a dialog asking you to open. See **Prerequisites** if you cannot open VS Code.

   <Frame caption="VS Code Open Dialog">
     <img src="https://www.gitpod.io/images/docs/flex/integrations/vscode/open_dialog.png" />
   </Frame>

### VS Code Insiders

You can select **VS Code Insiders** from the editor selector dropdown by clicking on the dropdown arrow next to the editor button on the action bar.

<Frame caption="VS Code Insiders">
  <img src="https://www.gitpod.io/images/docs/flex/integrations/vscode/select_vscode_insiders.png" />
</Frame>

## Install and Sign In

#### 1. Install the Gitpod Flex Extension

After opening, VS Code will prompt you to install the **Gitpod Flex** extension if it's not already installed.

* Click **Allow** when prompted.

  <Frame caption="Extension Installation Prompt">
    <img src="https://www.gitpod.io/images/docs/flex/integrations/vscode/install_extension.png" />
  </Frame>

> **Note**: The extension will make changes to your local SSH configuration to enable a smooth experience. This allows for seamless connectivity between VS Code and your environments.

#### 2. Install Remote Development Extensions

The integration requires both the **Remote - SSH** extension to function. If this is not already installed, VS Code will notify you to add it.

* Click **Install** to add this dependency.

  <Frame caption="Install Prompt for Remote Development Extensions">
    <img src="https://www.gitpod.io/images/docs/flex/integrations/vscode/install_remote_dev.png" />
  </Frame>

#### 3. Authenticate with Gitpod

VS Code will then ask you to authenticate with your Gitpod account:

1. Click **Open** when prompted to navigate to the Gitpod authentication page.
   <Frame caption="Authentication Prompt">
     <img src="https://www.gitpod.io/images/docs/flex/integrations/vscode/open_auth.png" />
   </Frame>
2. Follow the authentication process to complete the sign-in.
   <Frame caption="Complete Authentication Page">
     <img src="https://www.gitpod.io/images/docs/flex/integrations/vscode/complete_auth.png" />
   </Frame>
3. After signing in, you will be redirected back to VS Code and the page can be closed.

> **Note**: If you encounter any issues during the sign-in process, it may be helpful to sign out and try again.

## Workspace Trust

When connecting to a new environment, VS Code may prompt you to trust the workspace. This is a standard security measure for potentially untrusted code. For more information, refer to the [VS Code documentation](https://code.visualstudio.com/editor/workspace-trust).

Gitpod environments always run in isolated VMs, ensuring that code doesn't access secrets outside the environment. The environment remains secure regardless of how you access it. If you're familiar with the repository, you can safely click **Trust Folder & Continue**.

<Frame caption="Workspace Trust Prompt">
  <img src="https://www.gitpod.io/images/docs/flex/integrations/vscode/workspace_trust.png" />
</Frame>

## Managing Your Environment

Once connected, you can manage your environment directly from VS Code:

### Viewing Environment Details

* Check the status, active branch, and logs using the **Environment Details** panel.
* If you closed the panel, re-open it using the `Gitpod Flex: Show Environment Details` command from the Command Palette.

<Frame caption="Environment Details in VS Code">
  <img src="https://www.gitpod.io/images/docs/flex/integrations/vscode/details_view.png" />
</Frame>

> **Note**: Clicking on **details** while opening the environment will also open the **Environment Details** panel.

<Frame caption="Environment Details from Notification">
  <img src="https://www.gitpod.io/images/docs/flex/integrations/vscode/openning.png" />
</Frame>

### Accessing Commands

* Open the Command Palette (`Cmd+Shift+P` or `Ctrl+Shift+P`) and type `Gitpod Flex` to view commands such as:
  <Frame caption="Gitpod Commands">
    <img src="https://www.gitpod.io/images/docs/flex/integrations/vscode/command_palette.png" />
  </Frame>

* Clicking on the **remote indicator** in the bottom-left corner of the remote window also shows a quick menu of Gitpod commands.
  <Frame caption="Remote Indicator">
    <img src="https://www.gitpod.io/images/docs/flex/integrations/vscode/remote_indicator.png" />
  </Frame>

### Rebuild

Rebuilding is necessary to apply changes made to `.devcontainer.json`, `Dockerfile`, or `docker-compose.yml` files to the container. This process ensures that your development environment reflects the latest configuration updates.

To rebuild the container, you have two options:

1. **Command Palette**: Use `Gitpod Flex: Rebuild Container`
2. **Rebuild Prompt**: VS Code detects changes and prompts

   <Frame caption="Rebuild Prompt">
     <img src="https://www.gitpod.io/images/docs/flex/integrations/vscode/rebuild_notification.png" />
   </Frame>

While the container is rebuilding, you will be disconnected and automatically reconnected when it's finished. You can inspect the details view to learn about the progress and inspect logs.

<Frame caption="Rebuild Logs">
  <img src="https://www.gitpod.io/images/docs/flex/integrations/vscode/rebuild_logs.png" />
</Frame>

## Troubleshooting

### Limitations

Currently there are a couple limitations related to the devcontainer specification:

* Port forwarding does not work for hosts other than `localhost`. For instance, forwarding ports from other services specified in a docker-compose.yml  .
  * ✅ Workaround: Use `network_mode: host` in your docker-compose.yml for the services you want to port forward.
* `remoteEnv` environment variables values are not applied unless the devcontainer is rebuilt.

### Build Issues

If the initial build or a rebuild fails, you will enter recovery mode.

When a build failure occurs:

1. A modal will appear notifying you of the failure.
   <Frame caption="Rebuild Failure">
     <img src="https://www.gitpod.io/images/docs/flex/integrations/vscode/rebuild_failed.png" />
   </Frame>
2. Pay close attention to the error messages in the details view.
   <Frame caption="Rebuild Failure Details">
     <img src="https://www.gitpod.io/images/docs/flex/integrations/vscode/rebuild_failed_details.png" />
   </Frame>
3. Inspect the logs as necessary to understand the root cause of the failure.
   <Frame caption="Rebuild Failure Logs">
     <img src="https://www.gitpod.io/images/docs/flex/integrations/vscode/rebuild_failed_logs.png" />
   </Frame>
4. Make the required changes to the `.devcontainer.json` file to address the issue.
5. Trigger a rebuild using the `Gitpod Flex: Rebuild Container` command.

> **Important**: The recovery mode is not stable for development. Always aim to fix the configuration and successfully rebuild the container.

### Authentication Issues

If you're experiencing authentication issues or need to switch accounts:

1. Use the `Gitpod Flex: Sign Out` command to sign out.
2. Confirm the sign-out when prompted.
3. You can then sign in again with the same or a different account.

### General Issues

If you encounter unexpected problems:

1. Check the `Gitpod Flex` output view for any useful information.
2. Check your network settings, sometimes the VPN or firewall settings can interfere with the connection.
3. When sharing reports with us:
   * Use `Developer: Set Log Level...` command to Trace, it would give us more insights. Remember to set it back to Info afterwards.
   * In your VS Code settings, set `remote.SSH.logLevel` to `trace`.
   * Use the `Gitpod Flex: Export all logs` command from the problematic window. This will contain all relevant logs.

> **Note**: Be cautious when sharing logs on the internet, as they may contain sensitive information.

## Uninstalling

When uninstalling the Gitpod Flex extension, simply removing the extension from VS Code is not sufficient for a complete uninstall. Using the `Uninstall Extension` command ensures that all associated configurations, including SSH settings, are properly cleaned up.

1. Use the `Gitpod Flex: Uninstall Extension` command to initiate the uninstallation process.
2. Follow the prompts to complete the uninstallation process.

If you've already uninstalled the extension without using the command, you can install it again and then use the uninstall command.
