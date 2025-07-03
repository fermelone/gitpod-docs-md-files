# Linux Runner

The Linux runner lets you run Gitpod development environments directly on your Linux machine. It's designed to be an easy way to try Gitpod while maintaining full control over your infrastructure and costs.

## Key Features

* **Simple Setup**: Quick installation on your Linux machine
* **Fixed Costs**: Only pay for your hardware
* **Local Control**: Full control over your infrastructure
* **Local Network Access**: Direct access to local network services

## Architecture

The Linux runner consists of:

* **Runner Service**: Orchestrates environment lifecycle
* **Virtual Machines**: Uses cloud-hypervisor for environment isolation
* **Network Layer**: Manages VM connectivity and local network access
* **Management Plane Integration**: Connects to Gitpod for environment management

## Use Cases

Best suited for:

* **Evaluation**: Quick start without cloud infrastructure
* **Small Teams**: 2-10 developers sharing the runner for their environments
* **Local Network Access**: Teams needing local network service access
* **Cost Control**: Fixed infrastructure costs

## Comparison with AWS Runner

| **Feature**     | **Linux Runner**           | **AWS Runner**            |
| --------------- | -------------------------- | ------------------------- |
| Infrastructure  | Single Linux machine       | AWS cloud infrastructure  |
| Scaling         | Fixed to machine resources | Horizontal scaling        |
| Cost Model      | Fixed (hardware only)      | Pay per use               |
| Setup           | Simple local setup         | AWS account required      |
| Best For        | Evaluation & small teams   | Production & larger teams |
| Resource Limits | 10 environments max        | AWS quota based           |

## Limitations

* No horizontal scaling (single machine)
* Maximum 10 concurrent environments per runner
* AMD64 architecture only (no ARM support)
* Requires virtualization support (KVM)

## Network Access

Environments can access your local network, enabling:

* Local service integration
* Development database access
* On-premises tool connectivity

<Warning>
  Consider network policies as environments have full access to your local
  network.
</Warning>

## Getting Started

1. [Check Requirements](/flex/runners/linux/requirements)
2. [Install & Configure](/flex/runners/linux/setup)
3. [Setup Repository Access](/flex/runners/linux/setup#repository-access)
4. [Configure Environment Classes](/flex/runners/linux/setup#environment-classes)
5. [Share with your team](/flex/runners/aws/sharing-runners)

## Additional Resources

* [Maintenance Guide](/flex/runners/linux/maintenance)
* [Troubleshooting](/flex/runners/linux/troubleshooting)
