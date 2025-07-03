# Self-host Linux runner

> Run Gitpod environments on your own Linux machine

The Linux runner enables you to run Gitpod environments directly on your own Linux machine. This gives you full control over your infrastructure while enjoying Gitpod's collaborative features.

## Benefits of self-hosting

Self-hosting a Linux runner offers several advantages:

* **Full infrastructure control**: Maintain complete control over your hardware and environment configurations
* **Fixed costs**: Only pay for your own hardware with no usage-based billing
* **Network access**: Direct access to your local network services and resources
* **Resource allocation**: Support for up to 10 concurrent environments on a single runner
* **Security**: Keep your code and development activities within your own infrastructure
* **Customization**: Tailor hardware resources to your specific development needs

## Prerequisites

Before setting up a Linux runner, ensure your system meets these requirements:

* A Linux machine with AMD64/x86\_64 architecture
* Hardware virtualization support (KVM)
* Minimum 2GB RAM per environment you plan to run
* Root/sudo access for initial setup
* Admin access to your Gitpod organization

For detailed system requirements, see the [requirements documentation](/flex/runners/linux/requirements).

## Security considerations

When self-hosting a Linux runner:

* The runner requires root access during installation but runs with reduced privileges
* Environments run in isolated containers but can access the host network
* Consider network isolation if running on shared infrastructure
* Regularly update the runner for security patches

## Limitations

* Maximum of 10 concurrent environments per runner
* No built-in high availability options

## Installation and setup

To set up your Linux runner:

1. [Set up your Linux runner](/flex/runners/linux/setup)
2. [Configure environment classes](/flex/runners/linux/setup#environment-classes)
3. [Set up repository access](/flex/runners/linux/setup#repository-access)

For detailed information about Linux runners, including maintenance and troubleshooting, see the [Linux runners documentation](/flex/runners/linux).
