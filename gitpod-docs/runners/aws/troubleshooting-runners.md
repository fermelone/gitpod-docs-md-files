# Troubleshooting AWS runners

> Learn how to troubleshoot AWS runners.

If you encounter any issues while setting up or operating a Runner, please follow these steps:

* Review [the common problems](#common-problems).
* If the issue persists, [reach out to support](#contacting-support).

## Contacting Support

To start a support chat, use the bubble icon located in the bottom right corner of the application. When contacting support, please include the following information:

* Any error messages and relevant screenshots.
* [Runner ID and Version](#copy-runner-id-and-version) and [AWS Region](#find-cloudformation-stack).
* [Runner Logs](#retrieve-runner-logs-ecs-task-logs).

  <Frame caption="Report Issue">
    <img src="https://www.gitpod.io/images/docs/flex/desktop/report_issue.png" />
  </Frame>

### Copy Runner ID and Version

* Navigate to **Settings > Runners**.
* Locate your Runner card.
* Click `...` in the top right corner and select `Copy ID`.
* The Runner Version is displayed as the last item in the menu.

  <Frame caption="Find Runner ID and Version">
    <img src="https://www.gitpod.io/images/docs/flex/runners/runner_id_and_version.png" />
  </Frame>

### Find CloudFormation Stack

* Navigate to **Settings > Runners**.
* Open the Runner card to find the Stack Name, URL, and region.

### Retrieve Runner Logs (ECS Task Logs)

You can adjust the log level of your Runner from the Runner Configuration section to get more detailed logs for troubleshooting. See [Setting up an AWS Runner](/flex/runners/aws/setup-aws-runners#log-level-configuration) for log level configuration options.

#### Using ECS Console

To view the logs for the Runner using the ECS console:

* Navigate to [the AWS ECS console](https://console.aws.amazon.com/ecs).
* Locate the cluster by [the stack name](#find-cloudformation-stack).
* Select the service associated with the Runner.
* Go to the **Tasks** tab and find the most recent failed or active task.
* Click the task ID to open the details.
* Check the **Logs** tab or find the CloudWatch log stream.

> Note that each task has two log groups: one for the Runner itself and another for Prometheus (monitoring); we need the former.

#### Using AWS CLI

To look up the cluster name and task ID using AWS CLI, follow these commands:

1. To list all clusters and find your cluster name by [the stack name](#find-cloudformation-stack):

```sh
aws ecs list-clusters
```

2. To list tasks in a specific cluster and find your task ID:

```sh
aws ecs list-tasks --cluster <cluster-name>
```

3. Once you have the cluster name and task ID, you can view the logs for the Runner:

```sh
aws ecs describe-tasks --cluster <cluster-name> --tasks <task-id>
```

### Monitoring and Metrics

If you have configured metrics collection, your monitoring system will receive Runner metrics. For information on configuring metrics collection, see [Setting up an AWS Runner](/flex/runners/aws/setup-aws-runners#enable-metrics-collection).

## Common Problems

Network misconfigurations are the most frequent causes of installation issues. Please refer to the [infrastructure prerequisites](/flex/runners/aws/aws-infrastructure-prerequisites) to ensure all requirements are met. Below are common problems along with their diagnostics.

### CloudFormation Stack Fails

* **Symptoms:**

  * Stack Event Status: `ROLLBACK_COMPLETE` or `ROLLBACK_IN_PROGRESS` due to missing VPC, availability zones, or subnets.
  * Stack Event Status Reasons:
    * `Parameter validation failed: parameter value for EC2RunnerInstancesSubnet does not exist.`
    * `Parameter validation failed: parameter value for parameter name EC2RunnerInstancesSubnet does not exist.`
    * `Parameter validation failed: parameter value for parameter name EC2RunnerAzs does not exist.`

* **Diagnostics:**

  * On the initial page of the CloudFormation stack creation, ensure you select a VPC, at least one availability zone, and a subnet.
  * Choose subnets across multiple availability zones for fault tolerance.

### Runner Task Fails

* **Symptoms:**

  * Stack Event Status: `CREATE_FAILED` or `ROLLBACK_IN_PROGRESS` because the [Runner task fails](#retrieve-runner-logs-ecs-task-logs) to launch or is stuck in a pending state.
  * Stack Event Status Reason: `ECS Deployment Circuit Breaker was triggered.`
  * [Runner task fails](#retrieve-runner-logs-ecs-task-logs) initialization with errors such as `ResourceInitializationError: ...`.
  * Secrets Manager or other AWS services are inaccessible to the Runner.
  * The Runner cannot pull container images or resolve DNS queries.

* **Diagnostics:**

  * Verify that the VPC has an **Internet Gateway** or **NAT Gateway** configured.
  * Update the route tables to direct public subnets to the Internet Gateway and private subnets to the NAT Gateway.
  * For private subnets, add VPC endpoints for services like Secrets Manager, S3, and ECR.
  * Confirm that security groups allow outbound traffic to the required services.

### Instance Type Not Available

If you encounter an error stating that the requested instance type is unavailable in a specific availability zone (e.g., "The selected instance type m6i.xlarge is not available in the automatically assigned zone us-east-1e"), this is often due to regional or zone-specific availability constraints within AWS.

> Some zones, like `us-east-1d` and `us-east-1e`, have been reported to experience resource shortages more frequently. If possible, avoid using these zones exclusively and instead install your runners across multiple zones or regions.

Here's how you can address this:

1. **Install a Runner to a Different Region**:

   * Some instance types may be unavailable in certain regions or zones due to resource constraints. Refer to [AWS instance type availability](https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-instance-regions.html) for details. If necessary, install runners to use a different AWS region that supports your preferred instance type.

2. **Select Multiple Availability Zones**:

   * When installing a Runner using the [AWS CloudFormation Stack](/flex/runners/aws/setup-aws-runners#cloudformation-template), ensure that you select multiple subnets. For example, instead of restricting your Environment to only the subnet corresponding to `us-east-1e`, include subnets corresponding to `us-east-1a` and `us-east-1b` zones to improve availability.
     * You can also [update the existing stack parameters](/flex/runners/aws/update-runner#updating-cloudformation-parameters).

3. **Use an Alternate Instance Type**:

   * If the desired instance type (e.g., `m6i.xlarge`) is unavailable, consider using a different instance type, such as `c5.xlarge`, which may have better availability.
   * To update, [create a new Environment class](/flex/runners/aws/environment-classes) using the alternate instance type and disable the existing class.

4. **Retry Later**:

   * Instance availability can be transient. If none of the above options resolve the issue, wait and try again later, as AWS resources might become available after a brief period.

### Unexpected Costs

* **Symptoms:**

  * You notice unexpected charges in your AWS bill that you believe are related to the Runner infrastructure.
  * You continue receiving bills for resources even after deleting a Runner.

* **Diagnostics:**

  * Use the [Controls for Managing Costs](/flex/runners/aws/aws-runner-costs#controls-for-managing-costs) guide to investigate the specific AWS resources contributing to the charges.
  * After [deleting a runner](/flex/runners/aws/delete-runner), verify that the associated CloudFormation stack has been fully deleted. Additionally, check for any residual resources such as EC2 instances or EBS volumes associated with Environment IDs, and manually delete them if necessary to avoid ongoing costs.

### AWS SSM Access Requirements

* **Symptoms:**

  * New Environments fail to start with error message: `AWS account policy blocks ssm:SendCommand, which is required for starting Environments. See our docs for details on how to resolve this: https://www.gitpod.io/docs/gitpod/runners/aws/troubleshooting#aws-ssm-access-requirements`
  * Runner is marked as degraded with the above error message
  * Devcontainer build cache credentials cannot be set/refreshed, resulting in slower startup times

* **Diagnostics:**

  * Gitpod Environments require AWS Systems Manager (SSM) access to properly initialize and manage development Environments.
  * The `ssm:SendCommand` permission is used to send the initial Environment configuration and refresh devcontainer build cache credentials in Environments, and `ssm:GetCommandInvocation` to verify the result.
  * These permissions can be blocked by Service Control Policies (SCPs) at the AWS account level.
  * Check if your AWS account has Service Control Policies (SCPs) that might be blocking SSM access. The Runner role (containing `gitpodflexrunnerrole`) must be able to run these commands against EC2 instances in the account.
  * Test if SSM access is working by attempting to send a command to an EC2 instance or starting a new Environment.

* **Resolution:**

  * Contact your AWS administrator to review the current SCP that's blocking SSM access.
  * Request an exception for the Gitpod Runner's IAM role to allow:
    ```json
    {
    	"Version": "2012-10-17",
    	"Statement": [
    		{
    			"Effect": "Allow",
    			"Action": ["ssm:SendCommand", "ssm:GetCommandInvocation"],
    			"Resource": [
    				"arn:aws:ec2:*:*:instance/*",
    				"arn:aws:ssm:*:*:command/*"
    			]
    		}
    	]
    }
    ```
    Alternatively, if your existing policy denies the permission for all accounts, add an exception for your Gitpod Runner account:
    ```json
    {
    	"Version": "2012-10-17",
    	"Statement": [
    		{
    			"Effect": "Deny",
    			"Action": ["ssm:SendCommand", "ssm:GetCommandInvocation"],
    			"Resource": [
    				"arn:aws:ec2:*:*:instance/*",
    				"arn:aws:ssm:*:*:command/*"
    			],
    			"Condition": {
    				"StringNotEquals": {
    					"aws:PrincipalAccount": [
    						"<GITPOD_RUNNER_AWS_ACCOUNT_ID>"
    					]
    				}
    			}
    		}
    	]
    }
    ```

* **Security Note:**

  * The SSM commands are only used for Environment initialization and configuration.
  * They are sent over encrypted channels and follow AWS security best practices.

### Network Connectivity Issues

If you experience connectivity issues with your AWS Runner, follow these troubleshooting steps to diagnose and resolve common networking problems.

#### Common Network Issues

If you experience connectivity issues:

1. **Verify security group configurations**
   * Ensure port 29222 is open for SSH access to development Environments
   * Check that outbound rules allow HTTPS traffic to required endpoints
   * Verify internal communication on port 22999 is allowed

2. **Check route table configurations**
   * Confirm routes to internet gateway (for public subnets) or NAT gateway (for private subnets)
   * Verify default routes are properly configured

3. **Validate network ACL settings**
   * Ensure Network ACLs aren't blocking required traffic
   * Check both inbound and outbound rules

4. **Confirm DNS resolution is working**
   * Test DNS resolution for `app.gitpod.io` and `*.us01.gitpod.dev`
   * Verify VPC DNS resolution and DNS hostnames are enabled

5. **Test connectivity to Gitpod services**
   * From an EC2 instance in your Runner's subnet, test connectivity to required endpoints
   * Use tools like `curl` or `telnet` to verify connectivity

#### Required Endpoints Connectivity Test

Test connectivity to these critical endpoints from your Runner's subnet:

```bash
# Test HTTPS connectivity to Gitpod services
curl -I https://app.gitpod.io
curl -I https://api.us01.gitpod.dev

# Test connectivity to AWS services
curl -I https://public.ecr.aws
curl -I https://s3.amazonaws.com
```

#### Restarting the Runner After Networking Changes

After applying networking changes (such as security group updates, route table modifications, or VPC endpoint configurations), you may need to restart the Runner ECS task to ensure the changes take effect.

##### Using the AWS Console

1. Navigate to the [AWS ECS console](https://console.aws.amazon.com/ecs)
2. In the left sidebar, click **Clusters**
3. Locate and click on the cluster with your stack name (found in **Settings > Runners** in Gitpod)
4. In the **Services** tab, click on the service associated with your Runner
5. Click the **Update** button
6. In the **Deployment configuration** section, check the box for **Force new deployment**
7. Click **Update** at the bottom of the page
8. ECS will start a new task with the updated networking configuration and gracefully stop the old one

##### Using AWS CLI

You can also restart the Runner using the AWS CLI:

```bash
# Get your cluster name and service name
aws ecs list-clusters
aws ecs list-services --cluster YOUR_CLUSTER_NAME

# Force a new deployment
aws ecs update-service \
  --cluster YOUR_CLUSTER_NAME \
  --service YOUR_SERVICE_NAME \
  --force-new-deployment
```

#### Verification Steps

After making networking changes and restarting the Runner:

1. **Check Runner status in Gitpod**
   * Go to **Settings > Runners** in your Gitpod dashboard
   * Verify the Runner shows as "Connected"

2. **Test Environment creation**
   * Create a new Environment using the Runner
   * Verify the Environment starts successfully

3. **Monitor CloudWatch logs**
   * Check ECS task logs for any connectivity errors
   * Look for successful connections to Gitpod services
