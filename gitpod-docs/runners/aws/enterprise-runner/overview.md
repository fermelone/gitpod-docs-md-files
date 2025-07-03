# Overview

<Warning>
  Enterprise Runner is exclusively available to customers on the [Enterprise tier](https://www.gitpod.io/pricing). If you're an Enterprise customer, contact your Gitpod account manager for more information.
</Warning>

The Enterprise AWS Runner provides enhanced capabilities including AI agent support and direct connectivity options. Designed for enterprise customers who need advanced features and greater control over their infrastructure with custom networking configurations.

## Key Features

* **Ona AI agent integration** - Enhanced development workflows with AI-powered assistance
* **Direct connectivity** - Bypasses Gitpod's central gateway by using your own Network Load Balancer, secured with your custom domain and SSL/TLS certificate
* **Private VPC endpoints** - Connect to Gitpod's management plane via AWS PrivateLink for enhanced security without public internet traversal
* **Enhanced security** - Fine-grained IAM policies with permission boundaries for enterprise security requirements
* **HTTP proxy support** - Custom HTTP proxy configuration for environments behind corporate firewalls
* **Custom CA certificate support** - Support for enterprise certificate authorities and custom certificate chains

<Frame caption="Enterprise Runner architecture">
  <img src="https://www.gitpod.io/images/docs/flex/runners/enterprise-runner.webp" />
</Frame>

## Prerequisites

Before deploying your Enterprise AWS Runner, ensure you have:

1. **AWS Account** with elevated permissions for enterprise features

2. **Capacity Planning** - Follow our [Capacity Planning](/gitpod/runners/aws/capacity-planning) guide to determine your infrastructure requirements

3. **AMI Access** - If your organization restricts AMI usage, allowlist the AMIs Gitpod runners and environments run on

   | AMI Name                                     | Owner Account ID | Owner  | Purpose                  |
   | -------------------------------------------- | ---------------- | ------ | ------------------------ |
   | `bottlerocket-aws-ecs-1-x86_64`              | `149721548608`   | Amazon | Runner service           |
   | `gitpod/images/gitpod-next/ec2-runner-ami-*` | `995913728426`   | Gitpod | Development environments |

   For more details, review our [AMI Requirements](/gitpod/runners/aws/detailed-access-requirements#ami-requirements) guide

4. **Domain Name** that you control with DNS modification capabilities

5. **SSL/TLS Certificate** provisioned in AWS Certificate Manager (ACM). Your SSL certificate must include both Subject Alternative Names (SANs):
   * `yourdomain.com` (root domain)
   * `*.yourdomain.com` (wildcard subdomain)

## Network Requirements

The Enterprise Runner requires a custom VPC with specific networking setup for enhanced security and direct connectivity.

<Frame caption="Network Configuration Diagram">
  <img src="https://www.gitpod.io/images/docs/flex/runners/aws-networking-enterprise.webp" />
</Frame>

### AWS Infrastructure Setup

#### VPC Requirements

* Custom VPC spanning 2-3 Availability Zones for high availability
* CIDR block sized appropriately for your expected workload capacity

#### Subnet Architecture

* **EC2 instance subnets**: Private or public subnets where Runner instances will be deployed
  * Must be sufficiently large for your expected concurrent Environments
  * Can have non-routable CIDR range (e.g.: CGNAT range)
* **Load balancer subnets**: Subnets for the Network Load Balancer deployment
  * Public subnets for internet-facing deployments
  * Private subnets for internal-only access (must be routable from user networks)
  * Should span multiple Availability Zones for high availability
  * Must have a routable CIDR range

### Connectivity Requirements

This section outlines the network connectivity requirements for your Enterprise Runner deployment, including user access paths and required outbound connections.

#### User access to Environments

* Load balancer subnets must be routable from your internal network via VPN, Direct Connect, Transit Gateway, or other networking solutions
* DNS resolution for your custom domain from user networks
* Firewall rules allowing HTTP (port 80) and HTTPS (port 443) traffic to the load balancer

#### Outbound access requirements

| Endpoint                           | Purpose                           | Protocol | Port |
| ---------------------------------- | --------------------------------- | -------- | ---- |
| `app.gitpod.io`                    | Gitpod Service (management plane) | HTTPS    | 443  |
| `releases.gitpod.io/*`             | Gitpod Release Artifacts          | HTTPS    | 443  |
| `update.code.visualstudio.com/*`   | VS Code Server                    | HTTPS    | 443  |
| `*.vscode-unpkg.net`               | VS Code Extensions                | HTTPS    | 443  |
| `marketplace.visualstudio.com`     | VS Code Marketplace               | HTTPS    | 443  |
| `*.gallerycdn.vsassets.io`         | VS Code Assets                    | HTTPS    | 443  |
| `*.jetbrains.com`                  | JetBrains IDEs                    | HTTPS    | 443  |
| `public.ecr.aws`                   | Container images                  | HTTPS    | 443  |
| `*.amazonaws.com`                  | AWS API calls                     | HTTPS    | 443  |
| SCM Services                       | Source code repositories          | HTTPS    | 443  |
| (optional) Prometheus Remote write | Metrics endpoint                  | HTTPS    | 443  |
| (optional) Container Registries    | Custom container registries       | HTTPS    | 443  |

<Note>
  For more details about each of these outbound requirements, see [Detailed Access Requirements](/gitpod/runners/aws/detailed-access-requirements).
</Note>

#### VPC Endpoints (Optional)

VPC endpoints can help reduce data transfer costs and improve security by keeping traffic within the AWS network. Create VPC endpoints for all required AWS services per the [detailed access requirements](/gitpod/runners/aws/detailed-access-requirements#aws-services) guide.

For Enterprise customers with strict security requirements, you can also establish private connectivity to Gitpod's management plane using AWS PrivateLink. This eliminates the need for public internet access to communicate with Gitpod services. See the [setup guide](/gitpod/runners/aws/enterprise-runner/setup#private-vpc-endpoints-optional) for configuration details.

> Note: With standard VPC endpoints for AWS services, outbound internet access to Gitpod services is still required unless you also configure private VPC endpoints for Gitpod's management plane.

### Security Group Configuration

The CloudFormation template creates a default security group that will be associated with the Network Load Balancer with the following configuration:

* All egress traffic allowed
* Ingress from any IP (0.0.0.0/0) on ports 80 and 443

For enhanced security, you can create a custom security group and specify it in the CloudFormation template parameters to limit the load balancer access further. When creating a custom security group, ensure the following access:

**Inbound Rules:**

* Allow ports 80 and 443 from all IP ranges where your users will connect to Gitpod Environments
* Allow ports 80 and 443 from your SCM provider IP ranges (GitHub, GitLab, etc.) to enable OAuth redirects

**Outbound Rules:**

* Outbound access should allow connectivity to all the required services listed [above](#outbound-access-requirements)

## Next Steps

Ready to deploy your Enterprise Runner? Follow our comprehensive setup guide designed specifically for enterprise deployments.

<CardGroup cols={2}>
  <Card title="Set up Enterprise Runner" icon="rocket" href="/gitpod/runners/aws/enterprise-runner/setup">
    Deploy your Enterprise AWS Runner with enhanced capabilities
  </Card>

  <Card title="Troubleshooting AWS Runners" icon="wrench" href="/gitpod/runners/aws/troubleshooting-runners">
    Resolve common issues including networking problems and Runner configuration
  </Card>
</CardGroup>
