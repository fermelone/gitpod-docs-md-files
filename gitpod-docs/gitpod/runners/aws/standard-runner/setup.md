# Setup

Deploy your Standard AWS Runner using our CloudFormation template. This guide covers the step-by-step process to get your Runner up and running.

### Prerequisites

* Admin access to the Gitpod organization
* AWS account with networking configured (see [Overview](/gitpod/runners/aws/standard-runner/overview) for prerequisites)
* Permissions to deploy the CloudFormation stack

## Create AWS Runner

Go to Settings -> Runners, and press **Set up a new runner**:

<Frame caption="Runners in settings">
  <img src="https://www.gitpod.io/images/docs/flex/runners/runners-settings.webp" />
</Frame>

After choosing AWS from the list of available providers, continue with the **Standard Runner template**. If you're looking to set up a more advanced Runner with custom ingress capabilities, consider deploying an [Enterprise Runner](/gitpod/runners/aws/enterprise-runner/setup).

<Frame caption="Provider selection">
  <img src="https://www.gitpod.io/images/docs/flex/runners/runner-providers.webp" />
</Frame>

<Frame caption="CloudFormation Template selection">
  <img src="https://www.gitpod.io/images/docs/flex/runners/aws-template-standard.webp" />
</Frame>

Choose a **name** and select the **AWS region** to deploy the Runner into, then press **Create**. This creates the Runner reference in Gitpod. You will now need to run the CloudFormation stack to fully deploy your Runner.

<Note>
  Runners are regional, and can only launch Environments in the AWS region
  they are deployed in. For a multi-region support we recommend to set up
  multiple Runners in different regions. The region cannot be changed once
  deployed, but you can deploy multiple Runners in different regions.
</Note>

<Frame caption="Add a AWS Runner">
  <img src="https://www.gitpod.io/images/docs/flex/runners/add-runner.webp" />
</Frame>

<Frame caption="Runner details">
  <img src="https://www.gitpod.io/images/docs/flex/runners/runner-details.webp" />
</Frame>

## CloudFormation Template Deployment

Next, ensure you are signed into the right AWS account in the AWS console, and then press **Open AWS CloudFormation** to start deploying the Runner into your AWS account. This will link you to the AWS console to create the CloudFormation stack:

<Frame caption="Create stack in AWS">
  <img src="https://www.gitpod.io/images/docs/flex/runners/create-stack-in-aws.png" />
</Frame>

Most parameters are auto-filled already. For **Network Configuration**, choose a VPC (e.g. the default VPC) and one or more Availability Zones and subnets. The Runner will create Environments in the selected network configuration values.

<Frame caption="Parameters configuration in AWS">
  <img src="https://www.gitpod.io/images/docs/flex/runners/aws-parameters-configuration.png" />
</Frame>

When done with configuring the stack parameters, press **Create stack**. The stack is relatively simple and includes e.g. an ECS service and DynamoDB.

<Frame caption="AWS stack capabilities">
  <img src="https://www.gitpod.io/images/docs/flex/runners/stack-capabilities-note.png" />
</Frame>

<Frame caption="AWS stack component diagram">
  <img src="https://www.gitpod.io/images/docs/flex/runners/stack-component-diagram.png" />
</Frame>

Wait until the Stack is deployed successfully, and return to Gitpod Desktop.

<Info>The CloudFormation stack should deploy between 3-10 minutes.</Info>

Once deployed you should see a screen like this:

<Frame caption="AWS Runner configuration complete">
  <img src="https://www.gitpod.io/images/docs/flex/runners/runner-aws-config-complete-standard.png" />
</Frame>

## Next Steps

Once your Standard Runner is deployed and running, configure your repository access and Environment classes.

<CardGroup cols={2}>
  <Card title="Configure Repository Access" icon="git" href="/gitpod/runners/aws/configuring-repository-access">
    Set up access to your repositories
  </Card>

  <Card title="Troubleshoot" icon="wrench" href="/gitpod/runners/aws/troubleshooting-runners">
    Resolve common issues including networking problems and Runner configuration
  </Card>
</CardGroup>
