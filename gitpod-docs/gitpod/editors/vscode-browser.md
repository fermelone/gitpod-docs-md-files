# Visual Studio Code Browser

You can connect to your environments using VS Code in the browser, providing a zero-install, “ready to code” experience.
This guide will walk you through the setup process and provide tips for managing and troubleshooting within VS Code Browser.

<Frame caption="VS Code Browser">
  <img src="https://www.gitpod.io/images/docs/flex/integrations/vscode-browser/vscode_browser.png" />
</Frame>

## Opening an Environment

1. Start an environment in Gitpod

2. Open in **VS Code Browser**

   * While the environment is starting, you can click the **Open in VS Code Browser** button on the action bar, which is possible even when the environment is not fully running yet. VS Code Browser should open in a new tab.

     <Frame caption="Open from the Action Bar">
       <img src="https://www.gitpod.io/images/docs/flex/integrations/vscode-browser/open_action_bar.png" />
     </Frame>

3. VS Code Browser will then ask you to authenticate with your Gitpod account:

   1. Click **Allow** when prompted to sign in to navigate to the Gitpod authentication page.

   <Frame caption="Authentication Prompt">
     <img src="https://www.gitpod.io/images/docs/flex/integrations/vscode-browser/open_auth.png" />
   </Frame>

   2. Follow the authentication process to complete the sign-in.

   <Frame caption="Complete Authentication Page">
     <img src="https://www.gitpod.io/images/docs/flex/integrations/vscode-browser/complete_auth.png" />
   </Frame>

   3. After signing in, you will be redirected back to VS Code and the page can be closed.

> **Note**: If you encounter any issues during the sign-in process, it may be helpful to sign out and try again.

## Managing Your Environment

Once connected, you can manage your environment directly from VS Code in the Browser:

### Viewing Environment Details

* Check the status, active branch, and logs using the **Environment Details** panel.
* If you closed the panel, re-open it using the `Gitpod Flex: Show Environment Details` command from the Command Palette.

<Frame caption="Environment Details in VS Code">
  <img src="https://www.gitpod.io/images/docs/flex/integrations/vscode-browser/details_view.png" />
</Frame>

### Accessing Commands

* Open the Command Palette (`Cmd+Shift+P` or `Ctrl+Shift+P`) and type `Gitpod Flex` to view commands such as:
  <Frame caption="Gitpod Commands">
    <img src="https://www.gitpod.io/images/docs/flex/integrations/vscode-browser/command_palette.png" />
  </Frame>

* Clicking on the **remote indicator** in the bottom-left corner of the window also shows a quick menu of Gitpod commands.
  <Frame caption="Remote Indicator">
    <img src="https://www.gitpod.io/images/docs/flex/integrations/vscode-browser/remote_indicator.png" />
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

### Settings Sync

Enable Settings Sync to sync all your extensions and other preferences from VS Code Desktop in VS Code Browser, read more about over at the [offical Settings Sync documentation](https://code.visualstudio.com/docs/configure/settings-sync#_turning-on-settings-sync).

## Troubleshooting

### Limitations

The following limitations are present in addition to the [limitations listed for VS Code Desktop](/flex/editors/vscode#limitations):

* For environments using a Docker Compose configuration, it's required to set `network_mode: "host"` on the main service in your Docker Compose file for VS Code Browser to successfully connect to the environment.
* VS Code Browser is not supported for [local environments](/gitpod-desktop/overview#local-environments) created using Gitpod Desktop.

### Authentication Issues

If you're experiencing authentication issues or need to switch accounts:

1. Use the `Gitpod Flex: Sign Out` command to sign out.
2. Confirm the sign-out when prompted.
3. You can then sign in again with the same or a different account.

### General Issues

If you encounter unexpected problems:

1. Check the `Gitpod Flex` output view for any useful information.
2. When sharing reports with us:
   * Use `Developer: Set Log Level...` command to Trace, it would give us more insights. Remember to set it back to Info afterwards.
   * Use the `Gitpod Flex: Export all logs` command from the problematic window. This will contain all relevant logs.

> **Note**: Be cautious when sharing logs on the internet, as they may contain sensitive information.
