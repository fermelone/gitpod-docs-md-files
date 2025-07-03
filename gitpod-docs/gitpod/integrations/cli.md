# Gitpod CLI

The Gitpod CLI is a powerful tool that allows you to interact with your Gitpod environments and manage your development workflow directly from the terminal. Whether you're starting new environments, managing existing ones, or configuring your workspace, the CLI provides a streamlined interface for all your Gitpod operations.

## Installation

Getting started with the Gitpod CLI is straightforward. You have two options:

### Option 1: Quick Install (UNIX Systems)

```bash
curl -o gitpod -fsSL "https://releases.gitpod.io/cli/stable/gitpod-$(uname -s | tr '[:upper:]' '[:lower:]')-$(uname -m | sed 's/x86_64/amd64/;s/\(arm64\|aarch64\)/arm64/')" && \
chmod +x gitpod && \
sudo mv gitpod /usr/local/bin
```

### Option 2: Direct Download

Choose the appropriate version for your system:

* macOS: [x86\_64](https://releases.gitpod.io/cli/stable/gitpod-darwin-amd64) | [arm64](https://releases.gitpod.io/cli/stable/gitpod-darwin-arm64)
* Linux: [x86\_64](https://releases.gitpod.io/cli/stable/gitpod-linux-amd64) | [arm64](https://releases.gitpod.io/cli/stable/gitpod-linux-arm64)
* Windows: [x86\_64](https://releases.gitpod.io/cli/stable/gitpod-windows-amd64.exe) | [arm64](https://releases.gitpod.io/cli/stable/gitpod-windows-arm64.exe)

After downloading, you'll need to:

1. Make the binary executable:

   ```bash
   chmod +x gitpod
   ```

   Move it to your PATH:

   ```bash
   sudo mv gitpod /usr/local/bin
   ```

<Note>
  {' '}

  **Note for macOS users:** When first running a downloaded binary, you may see
  a security warning.
</Note>

You can resolve this by either:
Approving the app in *System Settings* → *Privacy & Security*

Or removing the quarantine attribute via terminal:

```bash
xattr -d com.apple.quarantine gitpod
```

The binary's signature can be verified using:

```bash
codesign -v gitpod -vvv
```

### Verifying Download Integrity

For security, verify the integrity of your downloaded CLI binary using SHA256 checksums from our release manifest:

```bash
# Get the checksums for the current release
curl https://releases.gitpod.io/cli/stable/manifest.json -L
```

#### Verification Steps

1. **Get the expected checksum** for your platform:
   ```bash
   # Extract checksum for your platform (requires jq)
   curl -sL https://releases.gitpod.io/cli/stable/manifest.json | jq -r '.downloads["<platform>"].digest'

   # Examples:
   # macOS Intel:        .downloads["darwin-amd64"].digest
   # macOS Apple Silicon: .downloads["darwin-arm64"].digest  
   # Linux x86_64:       .downloads["linux-amd64"].digest
   # Windows x86_64:     .downloads["windows-amd64"].digest
   ```

2. **Calculate your file's checksum**:
   ```bash
   # macOS/Linux
   shasum -a 256 gitpod

   # Windows PowerShell
   Get-FileHash gitpod-windows-amd64.exe -Algorithm SHA256
   ```

3. **Compare the checksums** - they must match exactly.

<Note>
  **Security Warning:** If the checksums don't match, do not use the binary and re-download from the official source.
</Note>

#### Without jq

If you don't have `jq` installed, view the full manifest and manually find your platform's digest:

```bash
curl https://releases.gitpod.io/cli/stable/manifest.json -L
```

## Getting started with Gitpod CLI

### Authentication

The Gitpod CLI supports multiple authentication methods:

#### Automated Authentication (in Gitpod Environments)

When using the CLI in a Gitpod environment, it automatically authenticates using the environment's token. Check your authentication status:

```bash
gitpod whoami
```

The output shows your access level:

* `PRINCIPAL_ENVIRONMENT`: Limited access to current environment only
* Your username: Full access to all features and environments

#### Browser-based Authentication

```bash
gitpod login
```

This is the simplest method that will:

* Open your default browser for authentication
* Create a new context for your session
* Store your credentials securely

#### Personal Access Token Authentication

For headless environments or automation scenarios, you can authenticate using a [Personal Access Token](./personal-access-token):

```bash
gitpod login --token
```

You can also provide the token directly:

```bash
gitpod login --token "your-token-here"
```

#### Environment Variables

Set the `GITPOD_TOKEN` environment variable before logging in:

```bash
export GITPOD_TOKEN="your-token-here"
gitpod login
```

### CLI in Gitpod Environments

#### Pre-installed CLI

Every Gitpod environment comes with the CLI pre-installed as `gitpod`. The CLI is automatically authenticated with limited access to the current environment's context, allowing you to:

* Stop the current environment (`gitpod environment stop`)
* View environment logs (`gitpod environment logs`)
* Rebuild the development container (`gitpod devcontainer rebuild`)

#### Upgrading Environment Access

To access additional features like managing other environments or organization resources, you'll need to create a new, fully authenticated context:

1. From within your environment, run:

   ```bash
   gitpod login
   ```

2. After authentication, the new context will automatically activate, giving you access to:
   * All environment management commands
   * Organization settings
   * Project management
   * Automation controls
   * Secret management

Remember that this upgraded access persists only for the current environment session. You'll need to re-authenticate if you restart the environment.

### Access Levels and Authentication Scope

Depending on how you're logged in, you may have different access levels. You can always change your authentication method or scope using the `gitpod login` command.

#### Default Environment Access (Pre-authenticated)

* View current environment status
* Basic environment operations
* Local development container management
* Port forwarding

#### Full Authentication Access (After Login)

* Create and manage all environments
* Organization management
* Project creation and configuration
* Secret management
* Automation control
* Runner management
* Cross-environment operations

### Basic Commands

Here are some essential commands to get you started:

```bash
# View your user information
gitpod whoami

# List your environments
gitpod environment list

# Create a new environment
gitpod environment create <repository-url>

# Start an existing environment
gitpod environment start <environment-id>

# Stop an environment
gitpod environment stop <environment-id>

# Delete an environment
gitpod environment delete <environment-id>
```

### Machine-readable Output

For scripting and automation, you can get machine-readable output in JSON or YAML format:

```bash
gitpod environment list -o json
gitpod environment list -o yaml
```

## Core Features

### Environment Management

#### Creating Environments

```bash
gitpod environment create <repo-url> [flags]

# Common flags:
--class-id        # Specify environment class
--editor          # Choose your preferred editor
--interactive     # Use interactive mode
--set-as-context  # Set as active context
```

#### Working with Running Environments

```bash
# SSH into an environment
gitpod environment ssh <environment-id>

# View environment logs
gitpod environment logs <environment-id>

# List environment ports
gitpod environment port list

# Open a port
gitpod environment port open <port-number>

# List available editors
gitpod environment list-editors

# Open with an editor
gitpod environment open <environment-id> --editor <editor-name|editor-id>
```

### Automation Management

The CLI provides comprehensive automation management capabilities:

```bash
# Initialize new automation
gitpod automations init

# Update automations of an environment
gitpod automations update automations.yaml

# Update the default automation file of an environment
gitpod automations update -s .gitpod/automations.yaml

# List automation tasks
gitpod automations task list

# Start a task
gitpod automations task start <task-reference>

# View task logs
gitpod automations task logs <task-reference>

# List automation services
gitpod automations service list

# Start a task
gitpod automations service start <service-reference>

# View task logs
gitpod automations service logs <service-reference>
```

## Advanced Features

### SSH Configuration

Set up native SSH access to your environments:

```bash
gitpod environment ssh-config
```

After configuration, connect directly using:

```bash
ssh <environment-id>.gitpod.environment
```

### Project Management

```bash
# List projects
gitpod project list

# Get project details
gitpod project get <project-id>

# Create a new project
gitpod project create <repo-url>
```

### Port Management

```bash
# Open a port with a custom name
gitpod environment port open <port> --name "my-service"

# Close a port
gitpod environment port close <port>
```

### Context Management

```bash
# List available contexts
gitpod config context list

# Switch contexts
gitpod config context use <context-name>

# Modify context settings
gitpod config context modify <context-name>
```

### Global Configuration

The CLI configuration file is located at `~/.gitpod/configuration.yaml`. You can modify settings using:

```bash
gitpod config set [flags]

# Common configuration options:
--autoupdate        # Enable/disable automatic updates
--release-channel   # Set release channel (stable/latest)
--host              # Set Gitpod instance host
```

## Best Practices

1. **Context Management**

   * Use separate contexts for different projects or organizations
   * Name contexts meaningfully for easy identification

2. **Environment Lifecycle**

   * Stop unused environments to conserve resources
   * Use `--dont-wait` flags for batch operations
   * Set appropriate timeouts for long-running operations

3. **Automation**

   * Initialize automation files in your project root
   * Use descriptive task names
   * Monitor task logs for debugging

4. **Security**
   * Regularly rotate access tokens
   * Use environment-specific SSH keys
   * Keep the CLI updated for security patches

## Troubleshooting

Common issues and solutions:

### Authentication Issues

```bash
gitpod login --non-interactive  # For environments without browser access
gitpod login --token "<your-token>"  # Use a token directly
gitpod config context modify --token "<your-token>"  # Update token manually
```

### Connection Problems

```bash
gitpod environment logs --include-system-logs --raw # View detailed logs
gitpod environment ssh --verbose  # Debug SSH connections
ssh -vvv <environment-id>.gitpod.environment  # Debug SSH connections
```

### Too Many SSH Authentication Failures

If you encounter `too many authentication failures` when connecting to a Gitpod environment, it may be due to multiple SSH keys being offered by an agent (e.g., 1Password). The server rejects connections after six failed attempts.

**Solutions:**

1. Stop the SSH agent to prevent other keys from being offered.
2. Ensure only the CLI key is used by adding `IdentitiesOnly yes` to your `~/.ssh/gitpod/config` under the `Host *.gitpod.environment` section.

#### Testing:

Re-enable your SSH agent and test the connection:

```bash
ssh -vvv <environment-id>.gitpod.environment
```

Ensure the correct key (`Offering public key:`) is used.

## Shell Completion

Enable shell completion for easier CLI usage:

```bash
# Bash
gitpod completion bash > /etc/bash_completion.d/gitpod

# Zsh
gitpod completion zsh > "${fpath[1]}/_gitpod"

# Fish
gitpod completion fish > ~/.config/fish/completions/gitpod.fish

# PowerShell
gitpod completion powershell | Out-String | Invoke-Expression
```

## Updates and Maintenance

Keep your CLI up to date:

```bash
# Check version
gitpod version

# Update CLI
gitpod version update

# Force update (even if version is up-to-date)
gitpod version update --force
```

## Additional Resources

* Use `gitpod help` for comprehensive command documentation
* Add `-h` or `--help` to any command for specific usage information
* Use `--verbose` flag for detailed logging when troubleshooting
* Check the configuration file at `~/.gitpod/configuration.yaml` for custom settings

Remember that the CLI is constantly evolving with new features and improvements. Keep your installation updated and refer to the official documentation for the latest information.
