# Access Requirements

Configure your firewall and network security groups to allow outbound connections to these endpoints for Gitpod to function properly.

<Note>
  **Enterprise Runner Proxy Support**: Enterprise runners support HTTP proxy configuration for environments behind corporate firewalls. When using a proxy, ensure that `.internal`, `169.254.0.0/16`, `app.gitpod.io`, and `.amazonaws.com` are added to the NO\_PROXY list. See the [Enterprise Runner setup guide](/gitpod/runners/aws/enterprise-runner/setup#proxy-configuration-optional) for detailed proxy configuration.
</Note>

## Gitpod Services

### Management Plane

Controls Runner and Environment orchestration by communicating with Gitpod's control plane.

* `https://app.gitpod.io`

### Gateway API Server

Provides secure connectivity between your runners and Gitpod services through encrypted tunnels. Not required for Enterprise runners.

**HTTPS (Port 8443):**

* `https://us01.gitpod.dev:8443`
* `https://*.us01.gitpod.dev:8443`

**UDP (Port 4242):**

* `35.171.240.32`
* `13.216.138.24`
* `44.223.157.13`
* `54.163.142.39`
* `35.171.31.215`

## VS Code

Required for VS Code IDE functionality including server downloads and extension marketplace access.

* `https://update.code.visualstudio.com/api/commits/stable/server-linux-x64-web`
* `https://update.code.visualstudio.com/api/commits/stable/server-linux-arm64-web`
* `https://update.code.visualstudio.com/commit:*/server-linux-x64/stable`
* `https://update.code.visualstudio.com/commit:*/server-linux-arm64/stable`
* `https://*.vscode-unpkg.net`
* `https://marketplace.visualstudio.com`
* `https://*.gallerycdn.vsassets.io`

## JetBrains

Required for JetBrains IDE functionality including IDE downloads and services.

* `https://download.jetbrains.com`
* `https://download-cf.jetbrains.com`
* `https://download-cdn.jetbrains.com`
* `https://data.services.jetbrains.com`

## Release Artifacts

Downloads Gitpod updates, CLI binaries, and agent components necessary for Runner and Environment operation.

* `https://releases.gitpod.io/ec2/stable/manifest.json`
* `https://releases.gitpod.io/ec2/stable/supervisor-amd64.xz`
* `https://releases.gitpod.io/ec2/stable/gitpod-ec2-runner.json`
* `https://releases.gitpod.io/ec2/stable/gitpod-ec2-runner-enterprise.json`
* `https://releases.gitpod.io/ec2/stable/gitpod-ec2-multi-org-runner.json`
* `https://releases.gitpod.io/cli/stable/manifest.json`
* `https://releases.gitpod.io/cli/stable/gitpod-linux-amd64`
* `https://releases.gitpod.io/cli/stable/gitpod-linux-amd64.exe`
* `https://releases.gitpod.io/cli/stable/gitpod-linux-amd64.sha256`
* `https://releases.gitpod.io/cli/stable/gitpod-linux-arm64`
* `https://releases.gitpod.io/cli/stable/gitpod-linux-arm64.sha256`
* `https://releases.gitpod.io/vscode/releases/*/vscode-remote.vsix`
* `https://releases.gitpod.io/vscode/releases/*/vscode-agent-amd64`
* `https://releases.gitpod.io/vscode/releases/*/vscode-agent-arm64`
* `https://releases.gitpod.io/jetbrains/releases/*/jetbrains-agent-amd64`
* `https://releases.gitpod.io/jetbrains/releases/*/jetbrains-agent-arm64`

## Container Registries

Downloads container images used by development environments and Runner infrastructure.

**Gitpod default devcontainer image:**

* `https://mcr.microsoft.com/devcontainers/base:ubuntu-24.04`

**AWS Public ECR (Runner images):**

* `https://public.ecr.aws`

## Your Infrastructure

### SCM and SSO Providers

Access to your source code repositories and authentication providers for user login and code access.

Configure access to your specific providers (complete HTTPS URLs):

* GitHub, GitLab, Bitbucket URLs
* SSO provider URLs (Okta, Azure AD, etc.)

## Optional Services

### Prometheus Remote Write

Optional metrics collection endpoint for monitoring Runner and Environment performance.

* Your metrics endpoint URL (HTTPS 443)

### Additional Container Registries

Optional access to custom container registries for pulling private or organization-specific images.

**Common registries (allow those you use):**

* `https://index.docker.io`
* `https://registry-1.docker.io`
* `https://auth.docker.io`
* `https://ghcr.io`
* Your private registry URLs (HTTPS 443)

## AWS Services

Replace `<region>` with your AWS region and `<account-id>` with your AWS Account ID.

### Instance Metadata

EC2 instance configuration and metadata required for AWS service integration.

* **Endpoint**: `169.254.169.254`
* **Protocol**: HTTP (80)

### Regional APIs

AWS service communication for EC2 management, container registry access, and other AWS operations.

* `https://ec2.<region>.amazonaws.com`
* `https://<account-id>.dkr.ecr.<region>.amazonaws.com`
* `https://s3.<region>.amazonaws.com`
* `https://ssm.<region>.amazonaws.com`
* `https://sts.<region>.amazonaws.com`
* `https://dynamodb.<region>.amazonaws.com`
* `https://cloudformation.<region>.amazonaws.com`
* `https://secretsmanager.<region>.amazonaws.com`
* `https://logs.<region>.amazonaws.com` (optional)
* `https://elasticloadbalancing.<region>.amazonaws.com` (Enterprise runners only)
* `https://acm.<region>.amazonaws.com` (Enterprise runners only)

## AMI Requirements

Both Standard and Enterprise AWS runners require access to specific AMIs. If your AWS Organization restricts AMI access, ensure your AWS account can launch EC2 instances from these AMIs.

### Required AMIs

| AMI Name                                     | Owner Account ID | Owner  | Purpose                  |
| -------------------------------------------- | ---------------- | ------ | ------------------------ |
| `bottlerocket-aws-ecs-1-x86_64`              | `149721548608`   | Amazon | Runner service           |
| `gitpod/images/gitpod-next/ec2-runner-ami-*` | `995913728426`   | Gitpod | Development environments |

### Allowlisting Recommendations

Gitpod updates AMIs regularly as part of our continuous security and feature updates. We recommend allowing access by **Owner Account ID** rather than specific AMI ID when implementing allowlisting policies.

#### Why Use Owner Account ID

* **Automatic updates**: New AMI versions are automatically accessible without policy updates
* **Security**: Ensures you always have access to the latest security patches
* **Maintenance**: Reduces administrative overhead of managing specific AMI IDs

#### Implementation

When configuring your AWS Organization's AMI access policies:

1. **Allow by Owner Account ID**: Use the Owner Account IDs from the table above
2. **Include both accounts**: Both Amazon (`149721548608`) and Gitpod (`995913728426`) accounts are required
3. **Test access**: Verify your Runner deployment account can launch instances from these AMIs

### Testing AMI Access

To verify AMI access is working correctly:

1. **Test AMI access** by attempting to launch a test instance from the required AMIs in your target region
2. **Check deployment logs** during Runner setup for any AMI access errors
3. **Monitor CloudFormation events** for AMI-related failures during stack deployment

```bash
# List available AMIs from required accounts (replace us-east-1 with your region)
aws ec2 describe-images --region us-east-1 --owners 149721548608 --filters "Name=name,Values=bottlerocket-aws-ecs-1-*"
aws ec2 describe-images --region us-east-1 --owners 995913728426 --filters "Name=name,Values=gitpod/images/gitpod-next/ec2-runner-ami-*"
```

If you encounter AMI access issues during Runner deployment, contact your AWS administrator to review and update your organization's AMI access policies.

## SSH Domain Aliases

Gitpod uses domain aliases like `<workspace-id>.gitpod.remote` and `<workspace-id>.gitpod.environment` for SSH connectivity to workspaces.

### Understanding Domain Aliases

These domain names are not actual internet domains but SSH configuration aliases that map to EC2 instance IP addresses:

* **Virtual domains**: `gitpod.remote` and `gitpod.environment` are virtual domains that exist only in your SSH configuration
* **Automatic mapping**: The Gitpod CLI updates your SSH config with the actual instance IP addresses
* **User-friendly access**: Provides clean identifiers instead of complex AWS hostnames like `ec2-18-184-202-80.region.compute.amazonaws.com`

### How They Work

1. When you connect to a workspace via SSH or VS Code, you use the alias (e.g., `abc123.gitpod.remote`)
2. Your SSH client resolves this to the actual IP address based on your SSH configuration
3. The Gitpod CLI manages these mappings automatically, fetching the current IPs from the Gitpod API

These aliases simplify connection management while hiding the complexity of the underlying dynamic cloud infrastructure.
