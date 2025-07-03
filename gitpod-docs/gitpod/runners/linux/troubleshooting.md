# Troubleshooting Linux Runners

## Common Symptoms

### Environment Stuck in Startup Phase

If your environment is stuck in the startup phase:

1. Check network forwarding configuration:

   ```bash
   # If using UFW (Uncomplicated Firewall)
   grep FORWARD /etc/default/ufw
   sudo ufw status

   # If not using UFW, check iptables
   sudo iptables -L FORWARD
   ```

2. If you see `Chain FORWARD (policy DROP)` in `iptables` or UFW's forward policy is not set to ACCEPT:

   ```bash
   # For UFW
   sudo nano /etc/default/ufw
   # Set DEFAULT_FORWARD_POLICY="ACCEPT"
   sudo ufw reload

   # For iptables
   sudo iptables -P FORWARD ACCEPT
   ```

3. Verify internet connectivity on the host machine

### Runner Shows as Disconnected

If the runner appears disconnected in the UI:

1. Check runner service status:

   ```bash
   # If running as a service
   sudo systemctl status gitpod-runner
   ```

2. View logs for errors:

   ```bash
   journalctl -u gitpod-runner
   ```

3. Verify:
   * Internet connectivity
   * System resources
   * Service configuration

### Setup Validation Fails

#### CPU Virtualization Not Enabled

```bash
❌ System requirements validation failed:
• CPU virtualization not enabled
```

1. Verify CPU virtualization support:
   ```bash
   grep -E 'svm|vmx' /proc/cpuinfo
   ```
2. Enable virtualization in BIOS if supported
3. Note: Most cloud VMs don't support nested virtualization by default

#### UFW Forwarding Policy Error

```bash
❌ System requirements validation failed:
• UFW forwarding policy needs to be configured
```

Follow the steps in [Environment Stuck in Startup Phase](#environment-stuck-in-startup-phase)

### Permission Issues

If you see capability or permission errors:

```bash
Error: failed to set capabilities on runner binary
```

This usually indicates an issue with the sudoers configuration. Check:

1. Verify your sudoers configuration:

   ```bash
   sudo cat /etc/sudoers.d/gitpod-runner
   ```

2. Ensure it contains the correct rules for your user and runner path:

   ```
   YOUR_USERNAME ALL=(root) NOPASSWD: /sbin/setcap cap_net_admin+ep /home/YOUR_USERNAME/gitpod-runner/bin/*/gitpod-runner
   YOUR_USERNAME ALL=(root) NOPASSWD: /sbin/setcap cap_net_admin+ep /home/YOUR_USERNAME/gitpod-runner/bin/*/cloud-hypervisor
   ```

3. If the file doesn't exist or has incorrect permissions, recreate it:

   ```bash
   sudo visudo -f /etc/sudoers.d/gitpod-runner
   ```

4. Add the rules provided during the setup process, replacing `YOUR_USERNAME` in paths and username with your actual values

### Resource Constraints

If environments fail to start or perform poorly:

1. Check system resources:

   ```bash
   free -h
   df -h
   ```

   > Runner data is stored in `~/gitpod-runner`

2. Solutions:
   * Stop unused environments
   * Increase system resources
   * Reduce concurrent environment count

### Environment Limit Reached

If you hit the 10 environment limit:

1. Check current environments in UI
2. Delete unused environments
3. Note: Deleted environments don't count towards limit

### Network Access Issues

If environments can't access the network:

1. Check forwarding configuration (see [Environment Stuck in Startup Phase](#environment-stuck-in-startup-phase))
2. Verify host machine network connectivity
3. Check network interface configuration:
   ```bash
   ip link show
   ```

### Repository Access Issues

If the runner can't access repositories:

1. Verify repository provider configuration in UI
2. Check authentication status
3. Try re-authenticating with repository provider

## Viewing Logs

For systemd service:

```bash
# View all logs
journalctl -u gitpod-runner

# Follow logs in real-time
journalctl -u gitpod-runner -f

# View recent logs
journalctl -u gitpod-runner -n 100
```

For terminal mode, logs are printed to stdout.

## Getting Help

If you can't resolve an issue:

1. Collect information:

   * Runner logs (from `journalctl` or terminal, also in `~/gitpod-runner/state/${RUNNER_ID}/log/`)
   * Runner version (visible in UI)
   * System information
   * Error messages
   * Environment logs (in `~/gitpod-runner/state/${RUNNER_ID}/environments/${ENV_ID}/logs/*.log`)

2. Contact Gitpod support through:
   * Support chat (bottom right in UI)
   * Include collected information in your report

## Prevention

To prevent common issues:

1. Regular maintenance:

   * Keep runner updated
   * Monitor resource usage
   * Clean up unused environments

2. Monitor logs for warnings:

   ```bash
   journalctl -u gitpod-runner
   ```

3. Keep sufficient free resources:
   * Disk space
   * Memory
   * CPU capacity
