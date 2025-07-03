# JetBrains

> Integrate JetBrains IDEs with Gitpod

Gitpod seamlessly integrates with JetBrains IDEs including IntelliJ IDEA Ultimate, GoLand, PhpStorm, PyCharm, RubyMine, WebStorm, Rider, CLion, and RustRover.

This guide will walk you through the setup process and provide tips for managing your development environments.

<Frame caption="Gitpod Website in WebStorm">
  <img src="https://www.gitpod.io/images/docs/flex/integrations/jetbrains/ide-overview.png" />
</Frame>

## Prerequisites

Before starting, ensure that you have:

1. [JetBrains Toolbox](https://www.jetbrains.com/toolbox-app/) installed on your system

> **Tip**: Keep JetBrains Toolbox for the best experience.

## Opening an Environment

1. Start an environment in Gitpod
2. Select your preferred JetBrains IDE (e.g., "Open IntelliJ IDEA Ultimate") from the action bar

<Frame caption="Open from Environment Details">
  <img src="https://www.gitpod.io/images/docs/flex/integrations/jetbrains/open-ide-button.png" />
</Frame>

### First-time Setup

On your first environment open, the setup process will:

1. Launch JetBrains Toolbox
2. Install the Gitpod plugin when prompted

<Frame caption="Plugin Installation">
  <img src="https://www.gitpod.io/images/docs/flex/integrations/jetbrains/plugin-install.png" />
</Frame>

3. Request authentication with your Gitpod account

<Frame caption="Authentication">
  <img src="https://www.gitpod.io/images/docs/flex/integrations/jetbrains/auth-prompt.png" />
</Frame>

### Connection Process

After authentication, Toolbox will:

1. Download and provision the IDE backend

<Frame caption="Installing JetBrains IDE Backend">
  <img src="https://www.gitpod.io/images/docs/flex/integrations/jetbrains/installing-ide-backend.png" />
</Frame>

2. Start your local IDE client

<Frame caption="Installing JetBrains IDE Client">
  <img src="https://www.gitpod.io/images/docs/flex/integrations/jetbrains/installing-ide-client.png" />
</Frame>

3. Connect to your environment automatically

<Frame caption="Connection Progress">
  <img src="https://www.gitpod.io/images/docs/flex/integrations/jetbrains/connection-progress.png" />
</Frame>

## Limitations

* The version of JetBrains IDEs cannot be changed.
* JetBrains IDE settings and plugins cannot be customized.

## Managing Authentication

To change your Gitpod account or sign out from JetBrains Toolbox:

1. Open JetBrains Toolbox
2. Go to Settings → Providers → Gitpod
3. Click "Sign Out"
4. Click "Sign In" to authenticate with a different account

<Frame caption="Signing Out">
  <img src="https://www.gitpod.io/images/docs/flex/integrations/jetbrains/sign-out.png" />
</Frame>

## Managing Environments

Toolbox list shows only recent environments you've previously opened. Open new environments from Gitpod directly.

<Frame caption="Recent Environments">
  <img src="https://www.gitpod.io/images/docs/flex/integrations/jetbrains/recent-environments.png" />
</Frame>

## Rebuilding Dev Containers

When rebuilding a devcontainer:

1. Close your current IDE window
2. Wait for rebuild to complete
3. Return to Gitpod
4. Select the IDE in the action bar to reconnect

## Troubleshooting

### Connection Issues

If your IDE doesn't connect:

1. Verify JetBrains Toolbox is running
2. Ensure your environment is running in Gitpod
3. Try closing the IDE and reopening from Gitpod

### Collecting Toolbox Logs

For persistent issues:

1. Open JetBrains Toolbox
2. Navigate to Settings → About
3. Click "Show log files"
4. Locate `toolbox.log`
5. Send to [support@gitpod.io](mailto:support@gitpod.io)

<Frame caption="Collecting Toolbox Logs">
  <img src="https://www.gitpod.io/images/docs/flex/integrations/jetbrains/collecting-toolbox-logs.png" />
</Frame>

<Warning>Do **NOT** share logs publicly as they may contain sensitive information</Warning>

### Collecting IDE Logs

For persistent issues:

1. Open JetBrains Toolbox
2. Navigate to your environment
3. Click on the three dots next to the IDE entry in the installed IDE list
4. Click "Show log files"
5. Send to [support@gitpod.io](mailto:support@gitpod.io)

<Frame caption="Collecting IDE Logs">
  <img src="https://www.gitpod.io/images/docs/flex/integrations/jetbrains/collecting-ide-logs.png" />
</Frame>

<Warning>Do **NOT** share logs publicly as they may contain sensitive information</Warning>
