# Zed

## Connecting an environment to Zed

Gitpod works with any remote and SSH compatible editor, including [Zed](https://zed.dev/download).

### Step 1 - Install the CLI and setup your SSH configuration

The easiest way to setup SSH configuration is by installing the [Gitpod CLI](/flex/integrations/cli).

Once installed, run `gitpod env ssh-config` to update your **local** SSH configuration.

To validate ensure the directory `~/.ssh/gitpod` is created on your local machine.

### Step 2 - Find the host for your environment

You can find the host name on your started environment details page.

The host format is: `<environment-id>.gitpod.environment`

For example: `01922350-2462-79da-8c80-770fe4275aa2.gitpod.environment`

<Frame caption="copying host id from app">
  <img src="https://www.gitpod.io/images/docs/flex/integrations/copy-host.png" />
</Frame>

> **Note:** You do not need the `ssh` command when connecting to JetBrains.

### Step 3 - Connect with your environment

In Zed open the remote projects dialogue with `cmd-shift-p remote`. - Add a connection. - Insert the SSH host from above.

<Frame caption="connect via zed">
  <img src="https://www.gitpod.io/images/docs/flex/integrations/zed-connection.png" />
</Frame>

See [zed documentation](https://zed.dev/remote-development) for more.
