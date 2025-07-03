# Overview

> Learn the different ways to run Gitpod development environments

Gitpod provides flexible options for running your development environments, either locally on your machine or securely in your own cloud infrastructure (VPC) or hardware.

## Deployment Options

Choose the option that best fits your workflow and infrastructure requirements:

| Option             | Description                                                 | Best for                                                         |
| ------------------ | ----------------------------------------------------------- | ---------------------------------------------------------------- |
| **Gitpod Desktop** | Run environments locally with built-in Linux virtualization | Individual developers or teams without cloud infrastructure      |
| **AWS Runner**     | Run in your own AWS VPC with full control                   | Teams needing enterprise-grade compute resources and GPU support |
| **Linux Runner**   | Run directly on your Linux machine with simple setup        | Small teams wanting direct local network access                  |

## Detailed Comparison

### Gitpod Desktop

* **Infrastructure**: Runs locally on your machine using built-in virtualization
* **Cost**: No additional infrastructure costs
* **Compute Resources**: Limited to your local hardware
* **Collaboration**: Project sharing only available with other Gitpod Desktop users
* [**Get Started with Gitpod Desktop →**](/gitpod/getting-started/create-dev-environment-desktop-app)

### AWS Runner (Bring Your Own Cloud)

* **Infrastructure**: Runs securely in your own AWS VPC
* **Cost**: Pay only for the AWS resources you use (can be covered by AWS free tier)
* **Compute Resources**: Scale up to 896 vCPUs and 12TB RAM with GPU support
* **Collaboration**: Environments can be shared with everyone in your organization
* [**Get Started with AWS Runner →**](/gitpod/getting-started/create-dev-environment-self-hosted-aws-runner)

### Linux Runner (On Your Hardware)

* **Infrastructure**: Runs directly on your Linux machine
* **Cost**: Fixed costs based on your existing hardware
* **Compute Resources**: Support for up to 10 concurrent environments
* **Collaboration**: Direct local network access for your team
* [**Get Started with Linux Runner →**](/gitpod/getting-started/create-dev-environment-linux-runner)

## Next Steps

After selecting your deployment option:

1. [Configure your development environment](/gitpod/getting-started/configure-dev-environment)
2. Set up authentication (via Personal Access Token or OAuth)
3. Configure maintenance and update strategies
