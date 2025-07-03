# System Requirements

## Hardware Requirements

### CPU

* Architecture: x86\_64/AMD64
* Virtualization support (VMX or SVM)
* KVM enabled

```bash
# Verify CPU support
grep -E 'svm|vmx' /proc/cpuinfo
# Verify KVM
ls /dev/kvm
```

### Memory

* Base: 100MB for runner service
* Per Environment: 2GB minimum
* Example sizing:
  * 3 environments: 6.1GB minimum
  * 5 environments: 10.1GB minimum
  * 10 environments: 20.1GB minimum

### Storage

* Minimum: 10GB free space
* Recommended: 50GB+ for multiple environments
* SSD recommended for performance

```bash
# Check free space
df -h
```

## Operating System

### Supported Distributions

* Ubuntu 24.04 LTS
* CentOS 9
* Fedora 40
* Other modern distributions (may need additional configuration)

### Architecture Support

* ✅ AMD64 (x86\_64)
* ❌ ARM64/AArch64 (not supported)

## System Configuration

> You don't need to make these changes manually. The setup command will:

* Check for all required configurations
* Show you exactly what changes are needed
* Guide you through making any necessary changes

The following sections describe what the setup will check and configure:

#### 1. Kernel Modules

* **What**: The following kernel modules are required:

  Network modules:

  * `bridge`: Network bridge support
  * `br_netfilter`: Bridge netfilter support
  * `nf_tables`: Netfilter tables
  * `nf_nat`: Network address translation
  * `nf_conntrack`: Connection tracking
  * `xt_conntrack`: Connection tracking netfilter module
  * `tun`: Network tunneling support

  Virtualization modules:

  * `kvm`: Base KVM module
  * `kvm_intel` (Intel CPUs) or `kvm_amd` (AMD CPUs): CPU-specific virtualization

* **Why**: These modules enable:
  * Network isolation and routing between environments
  * Virtual machine creation and management
  * Secure network communication

#### 2. Network Settings

* **What**: Enable IP forwarding and bridge filtering
* **Why**: Allows environments to access the internet and communicate securely
* **Changes**:

  ```bash
  # Apply settings
  sudo sysctl -w net.ipv4.ip_forward=1
  sudo sysctl -w net.bridge.bridge-nf-call-iptables=1
  sudo sysctl -w net.bridge.bridge-nf-call-ip6tables=1

  # Make permanent
  sudo bash -c 'cat > /etc/sysctl.d/99-gitpod-runner.conf << EOF
  net.ipv4.ip_forward=1
  net.bridge.bridge-nf-call-iptables=1
  net.bridge.bridge-nf-call-ip6tables=1
  EOF'
  ```

#### 3. UFW Configuration (if using UFW)

* **What**: Allow forwarding in UFW firewall
* **Why**: Required for environment network connectivity
* **Changes**:

  ```bash
  # Edit /etc/default/ufw
  DEFAULT_FORWARD_POLICY="ACCEPT"

  # Reload UFW
  sudo ufw reload
  ```

### Reverting Changes

To revert all system changes after uninstalling the runner:

```bash
# 1. Remove configuration files
sudo rm /etc/modules-load.d/gitpod-runner.conf
sudo rm /etc/sysctl.d/99-gitpod-runner.conf

# 2. Restore UFW settings (if modified)
sudo sed -i 's/DEFAULT_FORWARD_POLICY="ACCEPT"/DEFAULT_FORWARD_POLICY="DROP"/' /etc/default/ufw
sudo ufw reload

# 3. Restore system settings
sudo sysctl -w net.ipv4.ip_forward=0
sudo sysctl -w net.bridge.bridge-nf-call-iptables=0
sudo sysctl -w net.bridge.bridge-nf-call-ip6tables=0

# 4. Unload kernel module(s) (optional). Example:
sudo modprobe -r br_netfilter
```

> Save your original network configuration before making changes if you need to restore exact previous values.

### Connectivity

* Outbound internet access required for:
  * Gitpod services
  * Container registries
  * Source code repositories

### Network Access

* Runner creates virtual networks
* Environments can access local network
* Consider security implications

## User Permissions

### Installation

Requires root/sudo for:

* Installing Gitpod CLI
* Setting capabilities
* Configuring network
* Setting up systemd service

### Operation

* Runs without root after setup
* Service user needs network capabilities

## Unsupported Configurations

❌ Will not work on:

* Virtual machines
* Cloud instances
* ARM-based systems
* Windows/macOS
* Systems without hardware virtualization

## Validation

The runner automatically validates these requirements during setup. When you run `gitpod runner setup`, it will check:

* CPU virtualization support
* KVM availability
* Memory and disk space
* Network configuration
* Required system capabilities

If any requirements are not met, the setup will provide specific instructions for resolving the issues.

## Next Steps

Once requirements are met:

1. [Set up your Linux runner](/flex/runners/linux/setup)
2. [Configure environment classes](/flex/runners/linux/setup#environment-classes)
3. [Set up repository access](/flex/runners/linux/setup#repository-access)

If you encounter issues, check our [troubleshooting guide](/flex/runners/linux/troubleshooting).
