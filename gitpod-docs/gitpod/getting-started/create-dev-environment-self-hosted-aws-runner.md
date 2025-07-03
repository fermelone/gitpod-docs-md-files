# AWS Runner

> Deploy a Gitpod runner in your AWS account to create secure, cloud-based development environments for your entire team

Deploy a Gitpod runner in your AWS account to create secure, cloud-based development environments for your entire team. Unlike Gitpod Desktop which is installed per user, an AWS runner is deployed once and can be used by multiple team members.

## Benefits of the AWS Runner

* **Team-wide deployment**: Install once, benefit the entire team
* **Enhanced security**: Development environments run within your own AWS infrastructure
* **Resource efficiency**: Centralized management of compute resources
* **VPC integration**: Securely access internal services and resources within your AWS network
* **Customizable performance**: Configure environment classes to match your development needs
* **Scalability**: Support for multiple team members without individual installations

## Prerequisites

* **Admin role** in your Gitpod organization
* An AWS account with permissions to create CloudFormation stacks
* Basic knowledge of AWS networking concepts (VPC, subnets)

## Steps to set up an AWS runner

### 1. Create a runner configuration

1. Visit [app.gitpod.io](https://app.gitpod.io/)
2. Open your organization settings
3. Click **Runners** in the navigation
4. Click **Setup an AWS runner**

<Frame caption="Runners configuration page in Gitpod">
  <img src="https://www.gitpod.io/images/docs/flex/runners/runners-settings.png" />
</Frame>

**Note:** A runner is associated with an organization. You can have multiple runners, each restricted to a single AWS region.

### 2. Connect the runner to AWS

1. Ensure you're logged into the correct AWS account
2. Click **Continue on AWS**

<Frame caption="Runner configuration ready for AWS deployment">
  <img src="https://www.gitpod.io/images/docs/flex/runners/runner-aws-config-complete.png" />
</Frame>

> If you don't have direct AWS access, you can copy the runner details from this page and share them with your AWS account administrator.

3. Complete the CloudFormation form with the **required** fields:
   * VPC
   * Availability zone
   * Subnet

If you're unsure which values to use, select the [default networking](https://docs.aws.amazon.com/vpc/latest/userguide/default-vpc.html) options, which should auto-populate in the form.

<Frame caption="AWS CloudFormation parameters configuration">
  <img src="https://www.gitpod.io/images/docs/flex/runners/aws-parameters-configuration.png" />
</Frame>

4. Click **Create stack**

The CloudFormation stack typically takes about 3 minutes to deploy.

### 3. Configure source control access

1. Return to the runner configuration page where your runner should now show as **Online**
2. Configure repository access by selecting a provider (such as GitHub)
3. Enable OAuth or [Personal Access Token (PAT)](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) access

<Frame caption="Configure source control providers in Gitpod">
  <img src="https://www.gitpod.io/images/docs/flex/runners/repository-provider.png" />
</Frame>

### 4. Configure environment classes (Optional)

You can configure available environment classes for your runner. An environment class defines the performance profile (CPU, memory) for development environments on this runner.

<Frame caption="Add environment class in Gitpod">
  <img src="https://www.gitpod.io/images/docs/flex/runners/add-env-class.png" />
</Frame>

### 5. Create your development environment

1. Click **Create an environment** in the navigation bar
2. Paste a repository URL (public or private)
3. Click **Create environment**
4. Select an environment class from your AWS runner

<Frame caption="Select environment class for your new environment">
  <img src="https://www.gitpod.io/images/docs/flex/getting-started/select-environment-class.png" />
</Frame>

## Troubleshooting

### Common issues

* **CloudFormation deployment fails**: Ensure you've selected a valid VPC and subnet. The most common error is forgetting to select these required fields.
* **Runner shows as offline**: Check your AWS console to verify the EC2 instances are running correctly.
* **Cannot access private repositories**: Verify your OAuth or PAT configuration has the correct permissions for repository access.

## Next steps

After setting up your AWS runner and creating your first environment:

* Learn more about [projects](/flex/projects/overview)
* See [AWS Runner](/flex/runners/aws) for more detailed information.
