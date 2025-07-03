# Costs & Budgeting for AWS Runner

This guide outlines the costs associated with the AWS runner infrastructure. It does not include development environment costs or license fees.

<Note>
  AWS costs mentioned in this document are subject to change and may vary by
  region. Please check the latest pricing on the AWS pricing pages.
</Note>

## What is an AWS runner?

An AWS Runner is an orchestrator for development environments deployed within an AWS account.

The key characteristics of a runner are:

* Shared resource serving multiple users (not personal)
* Designed for "always-on" operation with optimized cost efficiency
* Suitable for small to medium-sized organizations with a single runner architecture
* Support for multiple runners to:
  * Enhance availability
  * Reduce latency for end users
  * Ensure data residency and compliance

## Billable AWS Resources

The following are the billable resources deployed by the AWS runner:

* **AWS::ECS::Service**: Used to manage the environments.
* **AWS::DynamoDB::Table**: Used to store state related to the reconciler of environments.
* **AWS::S3::Bucket**: Used to store user image and build Docker caches for performance.
* **AWS::ECR::Repository**: Used to store cached dev container images for faster environment startup (when [dev container image cache](/gitpod/runners/aws/devcontainer-image-cache) is enabled).
* **AWS::Logs::LogGroup**: Used to store logs related to the runner ECS task.

## Baseline Costs of a Runner

The primary cost associated with a runner is the ECS task.

* **Monthly Cost for ECS**: Less than \$8 per month, which is covered by the AWS free tier. This cost is fixed and does not vary with the number of environments.
* **Other services**: Costs for DynamoDB, S3, and CloudWatch typically account for less than 1% of the overall runner cost.

## Controls for Managing Costs

### Viewing Runner Costs

To view isolated runner costs in **AWS Cost Explorer**:

1. **Navigate to AWS Cost Explorer**.
2. **Group by Usage Type** to analyze the breakdown of costs.
3. **Filter by the CloudFormation stack** name, which can be found on your runner card in the Settings > Runners section.

   * **CloudFormation Stack**: Use the `aws:cloudformation:stack-name` tag.

     <img src="https://www.gitpod.io/images/docs/flex/runners/aws_stack_name_filter.png" alt="Stack Name Filter" width="400" />

   * **Cluster Name**: Alternatively, filter by the `aws:ecs:clusterName` tag.

     <img src="https://www.gitpod.io/images/docs/flex/runners/aws_cluster_name_filter.png" alt="Cluster Name Filter" width="400" />

### Viewing Environment Costs

To view isolated runner costs in **AWS Cost Explorer**:

1. **Navigate to AWS Cost Explorer**.
2. **Group by Usage Type** to analyze the breakdown of costs.
3. **Filter by the environment ID** using the **Name** tag:

   * **Tag**: `Name`
   * **Value**: `gitpod-environment-<ID>`
   * You can find the environment ID by selecting **Copy ID** from the environment details.

     <img src="https://www.gitpod.io/images/docs/flex/runners/aws_environment_id_filter.png" alt="Environment ID Filter" width="400" />

## EC2 Instance Tagging

All EC2 instances launched by Gitpod AWS runners automatically inherit tags from the CloudFormation template. This means:

* Any tags you add to the CloudFormation template will be propagated to the EC2 instances created for environments
* This allows for consistent resource tagging across your AWS infrastructure
* Tags can be used for cost allocation, resource grouping, and access control

### Adding Tags to EC2 Instances

To add tags to EC2 instances launched by Gitpod:

1. Navigate to the CloudFormation stack for your runner in the AWS console
2. Select **Update** from the stack actions
3. Choose **Use current template**
4. In the **Parameters** section, locate the **Tags** parameter (or add tags directly to the stack)
5. Add your desired tags in the format `Key=Value`
6. Complete the stack update process

All new EC2 instances launched after the update will include these tags.

<Note>
  When you update CloudFormation stack tags, the changes don't immediately apply to the existing runner ECS task. To force the runner to pick up the new tags immediately, you need to trigger a new deployment:

  1. In the AWS console, navigate to **Amazon ECS** > **Clusters**
  2. Select the cluster for your runner
  3. Select the runner service
  4. Click the arrow next to **Update** and select **Force new deployment**
  5. Click **Update** to apply the changes

  This will redeploy the runner service with the updated tags without affecting running development environments.
</Note>
