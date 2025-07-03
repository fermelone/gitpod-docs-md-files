# Setting up Linux Runners

This guide walks you through setting up a Linux runner. Before starting, ensure your system meets the [requirements](/flex/runners/linux/requirements).

## Prerequisites

* Admin access to your Gitpod organization
* Root/sudo access on your Linux machine
* A machine meeting all [system requirements](/flex/runners/linux/requirements)

## Installation Steps

### 1. Create Linux Runner in Gitpod

First, create a runner in your Gitpod organization:

1. Go to [Settings -> Runners](https://app.gitpod.io/settings/runners) in your Gitpod organization
2. Click **Set up a new runner**, and select **Linux**
3. Choose a name for your runner and click **Create**
4. Keep this page open - it will guide you through the remaining setup steps and automatically transition to repository access configuration once the runner is running

### 2. Install Gitpod CLI

On your Linux machine, install the Gitpod CLI:

```bash
wget -O gitpod "https://releases.gitpod.io/cli/stable/gitpod-linux-amd64"
chmod +x gitpod
sudo mv gitpod /usr/local/bin
```

### 3. Set up Runner

Run the setup command shown in the Gitpod UI in step 1:

```bash
gitpod runner setup --exchange-token <token>
```

The setup will:

* Validate system requirements
* Configure networking
* Set required permissions
* Download necessary components

If any requirements are not met, the setup will provide specific instructions for resolving the issues. Re-run the setup command after resolving any issues until it completes successfully.

### 4. Configure Permissions

During setup, the runner will check if it can set the required network capabilities. If it cannot, you'll be prompted to add specific rules to your sudoers configuration.

Follow the instructions provided by the setup command, which will typically include:

1. Copy the suggested sudoers rules, these should look like this (replacing `YOUR_USERNAME` with your user):
   ```
   YOUR_USERNAME ALL=(root) NOPASSWD: /sbin/setcap cap_net_admin+ep /home/YOUR_USERNAME/gitpod-runner/bin/*/gitpod-runner
   YOUR_USERNAME ALL=(root) NOPASSWD: /sbin/setcap cap_net_admin+ep /home/YOUR_USERNAME/gitpod-runner/bin/*/cloud-hypervisor
   ```
2. Open the sudoers file with:
   ```bash
   sudo visudo -f /etc/sudoers.d/gitpod-runner
   ```
3. Add the provided rules and save the file

These permissions allow the runner to:

* Set required network capabilities on its binaries without requiring full sudo access
* Automatically update itself without manual intervention
* Maintain proper isolation between environments

This approach is more secure than granting full sudo access because it:

* Limits elevated permissions to only the specific setcap command
* Restricts which binaries can receive capabilities
* Specifies exactly which capabilities can be granted
* Eliminates the need for password prompts during updates

### 5. Start Runner

```bash
gitpod runner run
```

Keep this command running to maintain the runner's operation. The runner will check for new environments to start and manage
existing ones.

## Optional: Systemd Service Setup

To run the runner as a system service, create a systemd service file:

1. Create the service file:

```bash
sudo nano /etc/systemd/system/gitpod-runner.service
```

2. Add this configuration:

> Make sure to replace `YOUR_USER_HERE` with your actual system username (`whoami`).

```
[Unit]
Description=Gitpod Runner Service
After=network.target

[Service]
Type=simple
User=YOUR_USER_HERE
ExecStart=/usr/local/bin/gitpod runner run
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

3. Start and enable the service:

```bash
sudo systemctl daemon-reload
sudo systemctl enable gitpod-runner
sudo systemctl start gitpod-runner
```

4. Check the service status:

```bash
sudo systemctl status gitpod-runner
```

5. Check the service logs:

```bash
journalctl -u gitpod-runner
```

## Repository Access

Before the runner can be used to launch environments, configure repository access by following our [repository access guide](/flex/runners/aws/setup-aws-runners#configuring-repository-access).

## Environment Classes

Configure environment classes to define the resources allocated to each environment. See our [environment classes guide](/flex/runners/aws/environment-classes).

The Linux runner creates a default set of environment classes based on the resources available on the host machine.

## Next Steps

* [Share runner with your team](/flex/runners/linux/maintenance#sharing)
* [Review maintenance guide](/flex/runners/linux/maintenance) for updates and maintenance
* [Review troubleshooting guide](/flex/runners/linux/troubleshooting) if you encounter issues

## Monitoring

Monitor your runner through:

* Gitpod UI (Settings -> Runners)
* System logs:
  ```bash
  # For systemd service
  journalctl -u gitpod-runner -f
  ```

## Common Setup Issues

If the setup fails, check:

1. System meets all [requirements](/flex/runners/linux/requirements)
2. Network/firewall configuration
3. Virtualization support is enabled in BIOS
4. Sufficient disk space and memory
5. Sudoers configuration is set correctly for automatic capability setting

For more help, see our [troubleshooting guide](/flex/runners/linux/troubleshooting).
