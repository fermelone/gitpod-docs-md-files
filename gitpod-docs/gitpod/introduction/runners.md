# Runners

Runners are flexible orchestrators of remote development environments that operate within your infrastructure. This "bring your own cloud" model provides you with complete control over where your development environments run while Gitpod manages the administration complexity.

## What are Runners?

Runners are responsible for key operational tasks within your infrastructure:

* Environment provisioning and scaling
* Backup management
* Local caching
* Source code management (SCM) integration
* Environment security

While runners operate in your infrastructure, they connect to Gitpod's management plane, which handles user authentication, identity management, and runner coordination. This hybrid approach gives you data control without the operational burden.

## Runner Types

Gitpod offers multiple runner options to fit your infrastructure needs:

1. **AWS Runner**

   * Deployed in your AWS account via CloudFormation
   * Supports horizontal scaling up to 400 concurrent environments
   * Minimal base cost (approximately \$8/month, often covered by AWS free tier)
   * Available in any AWS region or availability zone
   * Support for GPU-enabled environments

2. **Linux Runner**

   * Runs directly on your Linux machine with AMD64/x86\_64 architecture
   * Supports up to 10 concurrent environments
   * Provides direct local network access
   * Requires hardware virtualization support (KVM)

3. **Gitpod Desktop**
   * Run Dev Containers locally with built-in Linux virtualization
   * No infrastructure costs—everything runs locally
   * Currently available for Apple silicon users

## Runner Architecture

Runners work in conjunction with the Gitpod management plane:

* **Management Plane** (hosted by Gitpod): Handles database, SSO, identity management, user management, and runner coordination
* **Runner** (in your infrastructure): Manages environment provisioning, SCM authentication, and SCM context parsing
* **Environments** (created by runners): Provide security boundaries, secrets resolution, and automations execution

## Key Benefits

* **Infrastructure control**: Keep sensitive code and data within your own infrastructure
* **Private networking**: Access internal resources without exposing them to the public internet
* **Geographical flexibility**: Deploy runners close to your team to minimize latency
* **SCM integration**: Connect to private repositories on GitHub, GitLab, Bitbucket, or Azure DevOps
* **Resource optimization**: Use your own cloud resources and leverage committed spend
* **Team sharing**: Runners are shared across developers in your organization
* **Multiple deployment options**: Run as many runners as needed in different regions or availability zones

## Administration

* Runners require admin role in your Gitpod organization to create or modify
* Runners update automatically approximately once per week with no downtime
* Runners can be monitored using Prometheus
* Connection between users and environments is direct, secured with SSH keys
* Each runner can support up to 400 concurrent environments with no limit on total users

Organizations can deploy multiple runners across different regions and even mix runner types to best support global teams, data sovereignty requirements, and specific workloads.

For specific setup instructions, refer to the runner-specific documentation sections:

* [AWS Runner Setup](/flex/runners/aws)
* [Linux Runner Setup](/flex/runners/linux)
* [Gitpod Desktop](/flex/gitpod-desktop)
