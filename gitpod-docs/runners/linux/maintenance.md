# Updates and Maintenance

This guide covers how to keep your Linux runner updated and running smoothly.

## Version Management

The runner periodically checks for newer versions and logs a message when updates are available. You can see the current version of your runner in the Gitpod UI under Settings -> Runners.

## Updating the Runner

Updates are performed manually using the Gitpod CLI. To update your runner:

1. Stop the runner

   * If running in the terminal, press Ctrl+C
   * If running as a service:

     ```bash
     sudo systemctl stop gitpod-runner
     ```

     <Note>
       Stopping the runner does not stop any running environments. The
       environments will continue running, but the runner will not process
       any new start/stop requests or report environment status updates to
       Gitpod while it is stopped.
     </Note>

2. Run the update command:

   ```bash
   gitpod runner update
   ```

3. Restart the runner
   * If running in the terminal:
     ```bash
     gitpod runner run
     ```
   * If running as a service:
     ```bash
     sudo systemctl start gitpod-runner
     ```

## Monitoring

### Logs

* If running in the terminal, logs are printed directly to stdout
* If running as a systemd service, view logs with:
  ```bash
  journalctl -u gitpod-runner
  ```

Use the `-f` flag to follow logs in real-time:

```bash
journalctl -u gitpod-runner -f
```

### Runner Status

You can monitor your runner's status in the Gitpod UI under Settings -> Runners. The status will show:

* Connection state
* Version information
* Any warning or error messages

## Resource Management

The Linux runner runs environments as virtual machines on your host. The runner has a built-in limit of 10 environments (excluding deleted environments) per runner. To maintain good performance:

* Monitor system resource usage (CPU, memory, disk)
* Consider the number of concurrent environments
* Keep sufficient free disk space for environment data

## Best Practices

1. **Regular Updates**

   * Watch for update notifications in the logs
   * Plan updates during low-usage periods
   * Keep the runner up to date for the latest features and fixes

2. **Log Management**

   * If using systemd, consider configuring log rotation
   * Monitor logs periodically for warnings or errors
   * Keep track of resource usage patterns

3. **Backup Considerations**

   * The runner stores environment data in `~/gitpod-runner`
   * Consider this location in your backup strategy if needed

4. **System Maintenance**
   * Keep the host system updated
   * Monitor system health
   * Maintain sufficient free resources

## Common Maintenance Tasks

### Checking Runner Status

```bash
# If running as a service
sudo systemctl status gitpod-runner
```

### Restarting the Runner

```bash
# If running as a service
sudo systemctl restart gitpod-runner
```

## Deleting the Runner

To completely remove a runner:

1. Delete the runner from Gitpod in Settings -> Runners

2. On your Linux machine:

   a. Stop the runner process:

   * If running in the terminal, press Ctrl+C or terminate the `gitpod runner run` process
   * If running as a systemd service:
     ```bash
     sudo systemctl stop gitpod-runner
     ```

   b. Remove runner files and environment data:

   ```bash
   rm -rf ~/gitpod-runner
   ```

   c. If you set up a systemd service, remove it:

   ```bash
   sudo systemctl disable gitpod-runner
   sudo rm /etc/systemd/system/gitpod-runner.service
   ```

   d. Remove the sudoers configuration:

   ```bash
   sudo rm /etc/sudoers.d/gitpod-runner
   ```

## Next Steps

* [Troubleshooting guide](/flex/runners/linux/troubleshooting) for common issues
* [System requirements](/flex/runners/linux/requirements) for reference
* [Setup guide](/flex/runners/linux/setup) for installation details
