# Zero-trust environments

With Gitpod your source code, secrets, and internal network are isolated within your network perimeter. Gitpod's architecture is deployed in your infrastructure, providing full control over networking setup.

## How zero-trust principles protect your environments

Gitpod's architecture adheres to core zero-trust principles:

* **No implicit trust** — No user, device, or network is automatically trusted, whether inside or outside your architectural perimeter
* **Least privilege access** — Each component only has access to the resources it needs to function
* **Continuous validation** — Every request is authenticated, authorized, and validated before granting or maintaining access
* **Comprehensive identity model** — All actions are tied to specific identities (users, environments, runners, or accounts)

## Architecture that keeps you in control

Gitpod consists of two main components:

* **Management plane** (hosted by Gitpod) — Handles authentication, administrative functions, and policy management
* **Runners** (deployed in your VPC or "bring your own cloud") — Orchestrate development environments while keeping sensitive assets within your network boundaries

<Frame caption="Gitpod Architecture">
  <img src="https://www.gitpod.io/images/docs/flex/introduction/flex-architecture.png" />
</Frame>

{/* <!-- Insert architecture diagram showing security boundaries */}

## Data residency and compliance

Environments can be deployed across supported regions in AWS or on Linux machines:

* **AWS US regions**: `us-east-1`, `us-east-2`, `us-west-1`, `us-west-2`
* **AWS APAC regions**: `ap-southeast-1`, `ap-southeast-2`, `ap-northeast-1`
* **AWS EU regions**: `eu-west-1`, `eu-central-1`
* **AWS Other regions**: `sa-east-1`, `ca-central-1`

This flexibility helps organizations meet data residency requirements and compliance needs. Gitpod is SOC 2 Type 2 compliant.

## Comprehensive security audit trail

Every create/write/update operation on the management plane is logged through a centralized logging system, providing a comprehensive audit trail accessible via API. This enables:

* Complete visibility into all system activities
* Ability to trace any action back to a specific identity
* Support for compliance and security investigations

## Secret management

Gitpod's secret management system offers comprehensive encryption to protect your sensitive data:

* **Industry-standard encryption** — Secrets are encrypted using AES256-GCM at rest in the database
* **Multi-layered protection** — The database is additionally secured with AWS RDS encryption
* **Zero access by Gitpod** — Gitpod employees do not have access to encryption keys and cannot decrypt your secrets

Secrets can be configured as:

* **Files** — Mounted in the environment at a path of your choosing (recommended for sensitive data)
* **Environment Variables** — Accessible as standard environment variables

Files are recommended for sensitive information as they avoid common security issues with environment variables such as process visibility, logging exposure, and unintended inheritance by child processes.

Secrets are configured at the project level and automatically made available to environments launched from that project.

## Learn more

For a deeper technical dive into Gitpod's zero-trust architecture, including how identities are attested and how multi-tenancy is implemented, read our [blog post on building a zero-trust architecture for cloud development environments](https://www.gitpod.io/blog/how-we-built-it-zero-trust-architecture).
