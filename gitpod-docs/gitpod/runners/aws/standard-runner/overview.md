# Overview

The Standard AWS Runner provides a complete, easy-to-deploy solution for running Gitpod Environments in your AWS infrastructure. It connects securely through our central gateway, ensuring your Environments stay protected while maintaining simplicity.

## Key Features

* Super easy setup with CloudFormation template
* Complete AWS EC2 Runner solution
* Secure connectivity through Gitpod's central gateway

<Frame caption="Standard Runner">
  <img src="https://www.gitpod.io/images/docs/flex/runners/standard-runner.webp" />
</Frame>

## Gitpod Gateway

The Standard AWS Runner uses **Gitpod Gateway** to establish secure connectivity between your Runner infrastructure and Gitpod services. Gateway is an overlay network that creates encrypted tunnels to expose Environment ports and logs, as well as OAuth redirect URLs for Runners.

This eliminates the need to configure load balancers, SSL certificates, or custom DNS settings in your AWS environment. Gateway handles secure routing and authentication automatically, allowing users to access Environment services through Gitpod-managed domains while keeping your infrastructure private.

## Prerequisites

Before deploying your Standard AWS Runner, ensure you have:

1. **AWS Account** - Use either an existing AWS account or create a new one

2. **AMI Access** - If your organization restricts AMI usage, allowlist the AMIs that Gitpod runners and environments run on:

   | AMI Name                                     | Owner Account ID | Owner  | Purpose                  |
   | -------------------------------------------- | ---------------- | ------ | ------------------------ |
   | `bottlerocket-aws-ecs-1-x86_64`              | `149721548608`   | Amazon | Runner service           |
   | `gitpod/images/gitpod-next/ec2-runner-ami-*` | `995913728426`   | Gitpod | Development environments |

   For more details, review our [AMI Requirements](/gitpod/runners/aws/detailed-access-requirements#ami-requirements) guide.

3. **Optional IAM Role** - Configure an IAM role if needed for enhanced permissions and security

## Network Requirements

<Frame caption="Network Configuration Diagram">
  <img src="https://www.gitpod.io/images/docs/flex/runners/aws-networking.png" />
</Frame>

Your Standard AWS Runner requires specific network connectivity. **This applies to both deployment options below.**

### Required Ports

**User Access:**

* Port 29222 (TCP): SSH access from your users to development Environments

**Internal Communication:**

* Port 22999 (HTTP): Gitpod Runner to Environments
* Port 9090 (HTTP): Internal healthcheck within Gitpod Runner ECS task

### Required Outbound Endpoints

Your subnets must have outbound access to these endpoints:

| Endpoint                           | Purpose                           | Protocol | Port      |
| ---------------------------------- | --------------------------------- | -------- | --------- |
| `app.gitpod.io`                    | Gitpod Service (management plane) | HTTPS    | 443       |
| `*.us01.gitpod.dev`                | Gitpod Service (gateway)          | HTTPS    | 443, 8443 |
| `*.us01.gitpod.dev`                | Gitpod Service (gateway)          | UDP      | 4242      |
| `35.171.240.32`                    | Gitpod Service (gateway)          | UDP      | 4242      |
| `13.216.138.24`                    | Gitpod Service (gateway)          | UDP      | 4242      |
| `44.223.157.13`                    | Gitpod Service (gateway)          | UDP      | 4242      |
| `54.163.142.39`                    | Gitpod Service (gateway)          | UDP      | 4242      |
| `35.171.31.215`                    | Gitpod Service (gateway)          | UDP      | 4242      |
| `releases.gitpod.io/*`             | Gitpod Release Artifacts          | HTTPS    | 443       |
| `update.code.visualstudio.com/*`   | VS Code Server                    | HTTPS    | 443       |
| `*.vscode-unpkg.net`               | VS Code Extensions                | HTTPS    | 443       |
| `marketplace.visualstudio.com`     | VS Code Marketplace               | HTTPS    | 443       |
| `*.gallerycdn.vsassets.io`         | VS Code Assets                    | HTTPS    | 443       |
| `*.jetbrains.com`                  | JetBrains IDEs                    | HTTPS    | 443       |
| `public.ecr.aws`                   | Container images                  | HTTPS    | 443       |
| `*.amazonaws.com`                  | AWS API calls                     | HTTPS    | 443       |
| SCM Services                       | Source code repositories          | HTTPS    | 443       |
| (optional) Prometheus Remote write | Metrics endpoint                  | HTTPS    | 443       |
| (optional) Container Registries    | Custom container registries       | HTTPS    | 443       |

<Note>
  For more information about each of these outbound requirements, see [Detailed Access Requirements](/gitpod/runners/aws/detailed-access-requirements).
</Note>

## Deployment Options

Choose the deployment option that best fits your needs:

### Option 1: Quick Start (AWS Default VPC)

Get a working Runner with minimal configuration in under 30 minutes.

**Requirements:**

* Uses your AWS account's **default VPC** with Internet Gateway
* **Subnets** with [auto-assign public IP address enabled](https://docs.aws.amazon.com/vpc/latest/userguide/subnet-public-ip.html)
* Internet connectivity for all required endpoints listed above

**Ready to start?** Go to [Setup](/gitpod/runners/aws/standard-runner/setup) and use the quick start options.

### Option 2: Custom VPC Setup

Full control over networking, security, and deployment architecture.

**Requirements:**

* **Capacity Planning** - Follow our [Capacity Planning](/gitpod/runners/aws/capacity-planning) guide to determine your infrastructure requirements
* **Custom VPC** with your preferred networking setup:
  * Private subnets with NAT Gateway, Transit Gateway, VPN, or other connectivity solutions
  * Outbound internet access to all required endpoints listed above
* **Optional VPC endpoints** for cost optimization

<Note>
  **Important:** If using private subnets, ensure connectivity is available to the private IP addresses of the VPC from your local machine, as you'll need to connect to the EC2 instances.
</Note>

#### VPC Endpoints (Optional)

VPC endpoints can help reduce data transfer costs and improve security by keeping traffic within the AWS network. For a complete list of supported AWS services, see the [AWS Services page](/gitpod/runners/aws/detailed-access-requirements#aws-services).

> Note: Even with VPC endpoints, outbound internet access to Gitpod services is still required.

## Security Group Configuration

The CloudFormation template automatically creates a default security group for EC2 Environments with the necessary rules for Gitpod to function. This security group controls access to your development Environments.

**Default security group includes:**

* **Inbound:** Port 29222 (TCP) from any IP address (0.0.0.0/0) - for user SSH access to Environments
* **Inbound:** Port 22999 (HTTP) within VPC - for Runner orchestrator communication
* **Outbound:** All traffic to required endpoints

### Using a Custom Security Group (Optional)

<Warning>
  **Important:** This security group is applied to EC2 Environments. Incorrect configuration can disrupt user connections to Environments or communication between the Runner orchestrator and Environments.
</Warning>

If you need to restrict access further (recommended for production), you can create your own security group and provide it as a CloudFormation template parameter.

**Your custom security group must include these rules:**

**Inbound Rules:**

* Port 29222 (TCP): Allow from your users' IP ranges (restrict as needed for production)
* Port 22999 (HTTP): Allow from VPC CIDR block or from Gitpod Runner security group

**Outbound Rules:**

* Allow all outbound traffic to the endpoints listed in the Network Requirements section above

## Next Steps

<CardGroup cols={2}>
  <Card title="Set up Standard Runner" icon="rocket" href="/gitpod/runners/aws/standard-runner/setup">
    Deploy your Standard AWS Runner with our step-by-step guide
  </Card>

  <Card title="Troubleshooting AWS Runners" icon="wrench" href="/gitpod/runners/aws/troubleshooting-runners">
    Resolve common issues including networking problems and Runner configuration
  </Card>
</CardGroup>
