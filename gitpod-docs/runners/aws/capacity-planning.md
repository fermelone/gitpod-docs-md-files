# Capacity Planning

Planning your AWS infrastructure for Gitpod requires careful consideration of your organization's network requirements and future growth. This guide helps you plan the required AWS account, regions, availability zones, and subnets for your deployment.

When planning your AWS infrastructure, consider these key objectives:

* Identify regions that offer optimal latency for your users
* Plan network capacity based on anticipated user count and growth
* Ensure system robustness through strategic availability zone selection
* Minimize future infrastructure changes by planning for scale

We'll create a planning table that will serve as input to set up your [Standard AWS Runner](/gitpod/runners/aws/standard-runner) or [Enterprise AWS Runner](/gitpod/runners/aws/enterprise-runner/overview). Enterprise Runners require additional load balancer subnet planning due to their dual-subnet architecture.

# Quick Start: Basic Setup

For a basic setup (single runner, single region, fewer than 1000 users):

1. Select your region based on the [recommended latency](/flex/runners/aws/aws-regions#recommended-latency)
2. Use the following configuration:

**Standard Runner**

| Runner Name | Max Users | Region    | Number of AZs | EC2 Subnet Size | Total Capacity |
| ----------- | --------- | --------- | ------------- | --------------- | -------------- |
| us-east     | 1000      | us-east-1 | 2             | /23 (512 IPs)   | 1019           |

**Enterprise Runner**

| Runner Name | Max Users | Region    | Number of AZs | EC2 Subnet Size | Load Balancer Subnet Size | Total Capacity |
| ----------- | --------- | --------- | ------------- | --------------- | ------------------------- | -------------- |
| us-east     | 1000      | us-east-1 | 2             | /23 (512 IPs)   | /28 (16 IPs)              | 1019           |

<Note>
  **Standard runners** use a single subnet type for EC2 instances. **Enterprise runners** require both EC2 subnets (for environments) and load balancer subnets (must be routable from your internal network).
</Note>

If this **Basic Setup** is sufficient for your needs, feel free to **skip the rest of this chapter** and proceed to setup your [Standard Runner](/gitpod/runners/aws/standard-runner) or [Enterprise Runner](/gitpod/runners/aws/enterprise-runner/setup).

# Example Planning Table

The following table demonstrates how to plan your AWS Runner infrastructure. We'll use this format to help you plan your specific deployment.

**Standard Runner Example**

| Runner Name | Users | Region    | Number of AZs | EC2 Subnet Size | Capacity |
| ----------- | ----- | --------- | ------------- | --------------- | -------- |
| us-east     | 500   | us-east-1 | 3             | /22 (1024 IPs)  | 3068     |
| us-west     | 100   | us-west-1 | 2             | /23 (512 IPs)   | 1019     |
| europe      | 300   | eu-west-1 | 2             | /21 (2048 IPs)  | 4091     |

**Enterprise Runner Example**

| Runner Name | Users | Region    | Number of AZs | EC2 Subnet Size | Load Balancer Subnet Size | Capacity |
| ----------- | ----- | --------- | ------------- | --------------- | ------------------------- | -------- |
| us-east     | 500   | us-east-1 | 3             | /22 (1024 IPs)  | /28 (16 IPs)              | 3068     |
| us-west     | 100   | us-west-1 | 2             | /23 (512 IPs)   | /28 (16 IPs)              | 1019     |
| europe      | 300   | eu-west-1 | 2             | /21 (2048 IPs)  | /28 (16 IPs)              | 4091     |

**Table Column Definitions**

* **Runner Name**: Choose a meaningful identifier for your runner
* **Users**: Maximum number of users expected to use the runner, including planned growth
* **Region**: AWS region where the runner will be deployed
* **Number of AZs**: Number of Availability Zones for the runner deployment
* **EC2 Subnet Size**: CIDR block size for EC2 subnets (where environments run)
* **Load Balancer Subnet Size (for Enterprise Runners only)**: CIDR block size for load balancer subnets. Load balancer must be routable from your internal network.
* **Capacity**: [Maximum number](#step-4%3A-plan-subnet-sizes) of dev environments the runner can support.

# Your Planning Table

Please create your own table and fill in the columns with your values.

### Infrastructure Considerations

Before creating your planning table, consider these important points:

* Gitpod AWS Runners can share AWS accounts, VPCs, regions, and subnets with other AWS runners
* Runners operate independently and can be deployed across multiple AWS accounts and VPCs
* For multiple runners, you can (but don't have to) use separate AWS accounts
  * If using multiple AWS accounts, add an "AWS Account" column to your planning table

### Step 1: Select Regions

Gitpod supports multiple runners that can be added or removed as needed. However, it's important to plan your regions carefully as you'll need appropriately sized subnets in each region.

Choose one or more [AWS Regions that provide the best latency for your users](/flex/runners/aws/aws-regions).

### Step 2: Estimate Users per Region

For each selected region, estimate the maximum number of users, considering:

* Current number of users
* Expected growth over time
* Peak usage patterns
* Geographic distribution of your team

### Step 3: Determine Availability Zones

Each AWS Runner requires at least one Availability Zone (AZ) and can utilize all AZs within a region. Key points:

* One subnet is required per AZ
* We recommend using 2-3 AZs per region for optimal availability
* More AZs provide better fault tolerance but increase complexity
* Consider your organization's high availability requirements

### Step 4: Plan Subnet Sizes

Subnet sizing is crucial for your Gitpod deployment's functionality and depends on the workload you are likely to have. Proper planning ensures you have sufficient IP addresses for your development environments while avoiding over-provisioning that wastes resources. Based on your runner type, you'll need to plan different subnet configurations.

#### EC2 Subnets (Both Standard and Enterprise Runners)

These subnets host your development environments and require careful capacity planning.

* Each environment requires one IP address
* Each AZ requires one subnet
* Management services need fewer than five IP addresses
* For Standard Runners, Environments run as EC2 instances and require routable subnets
* For Enterprise Runners, EC2 subnets can use non-routable CIDR ranges (such as CGNAT ranges) since they don't need direct access from your internal network
* Gitpod does not use Network Address Translation (NAT) for environments
* The minimum subnet size is `/28` (supports 10 environments)
* If multiple runners share subnets, they share the available IP address pool
* Maximum capacity = (Total subnet IPs × Number of AZs) - Management IPs
* **For public subnets** If using public subnets with internet gateway routing, ensure the subnet is configured to auto-assign public IP addresses. See [AWS documentation on auto-assign public IP](https://docs.aws.amazon.com/vpc/latest/userguide/subnet-public-ip.html) for configuration details.
* Note that it's best practice to choose subnet sizes generously, as expanding a subnet later can be more complex and costly than planning for growth upfront

#### Load Balancer Subnets (Enterprise Runners Only)

Enterprise Runners require additional subnets for their Network Load Balancer infrastructure, which provides direct connectivity to your environments.

* Required for Network Load Balancer deployment
* Must be routable from your internal network (unlike EC2 subnets which can use non-routable CIDR ranges)
* Typically `/28` (16 IPs) is sufficient for most deployments
* Need one subnet per AZ for high availability
* Do not affect environment capacity calculations
