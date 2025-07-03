# Updating a Runner

> Learn how to update your AWS runner.

This guide explains how to update your AWS runner to ensure you have the latest features, improvements, and security patches. There are three methods to update your runner:

* [Automatic Updates](#automatic-updates): The AWS runner handles most updates automatically with minimal user intervention.
* [Updating Infrastructure](#updating-infrastructure): For significant changes, manual updates via CloudFormation are required.
* [Updating CloudFormation Parameters](#updating-cloudformation-parameters): Update specific configuration settings through CloudFormation parameters.

Follow the instructions in each section to keep your AWS runner up-to-date and running smoothly.

## Automatic Updates

The AWS runner includes a built-in update mechanism that automatically manages application updates. Here's how it works:

### Update Check Process

* The updater performs version checks periodically
* During each check, the runner:
  * Queries the Gitpod API for the available version
  * Compares the current version with the available version
  * Verifies infrastructure version compatibility

### Update Eligibility

A runner is eligible for updates when:

* It is on the stable channel
* Auto-updates are enabled for the version
* The infrastructure version matches the current runner's infrastructure version
* The available version is newer than the current version
* The runner image is different from the currently running image

### Update Process Flow

When an update is available, the following steps occur:

1. **Preparation**
   * The updater acquires a lock to ensure only one update process runs at a time
   * Creates a new task definition with the updated runner image
   * Maintains all existing configuration and IAM roles

2. **Deployment**
   * Updates the ECS service with the new task definition
   * Monitors the deployment progress
   * Uses circuit breaker protection for failed deployments

3. **Health Checks**
   * New container must pass health checks:

4. **Rollback**
   * If deployment fails, automatic rollback to previous version
   * Failed updates are logged and marked accordingly

### Infrastructure Version

* Ensures compatibility between runner and infrastructure
* Updates only proceed with matching versions

### Monitoring

* All update activities logged to AWS CloudWatch Logs
* Update process visible in AWS ECS console
* Prometheus metrics available (when configured on the runner)

### Important Notes

* Updates are non-disruptive to running workloads
* Process is fully automated with no manual intervention needed
* Failed updates don't impact existing runner functionality
* Runner maintains configuration and credentials through updates

> Tip: View the current version of the runner on the runner card under **Settings > Runners**.

## Updating Infrastructure

Certain updates, particularly those involving significant infrastructural changes, cannot be applied automatically. Follow these steps to apply updates:

<Warning>
  Upgrading CloudFormation templates that were applied from January 2025 or earlier will cause existing environments to no longer be accessible due to SSH port changes. Before upgrading, either stop and discard existing environments, or manually update the security group to allow access from 0.0.0.0/0 to port 22 (in addition to port 29222) after upgrading the stack.
</Warning>

1. Open the CloudFormation stack used for the runner in the AWS console.

2. Select **Update** to modify the stack configuration.

3. Select the **Replace existing template** option and enter the following URL in the **Amazon S3 URL** field:

   ```plaintext
   https://gitpod-flex-releases.s3.amazonaws.com/ec2/stable/gitpod-ec2-runner.json
   ```

   <Frame caption="Replace Existing Template">
     <img src="https://www.gitpod.io/images/docs/flex/runners/update_stack_replace_existing.png" />
   </Frame>

4. Review and adjust the parameters as needed.

5. Follow the remaining steps in the wizard to update the stack.

## Updating CloudFormation Parameters

To update only the CloudFormation (CF) parameters, such as VPC, subnets, or other configuration settings, follow these steps:

1. Open the CloudFormation stack used for the runner in the AWS console.

2. Select **Update** to modify the stack configuration.

3. Choose **Use existing template** when prompted, as shown below:

   <Frame caption="Use Existing Template">
     <img src="https://www.gitpod.io/images/docs/flex/runners/update_stack_use_existing.png" />
   </Frame>

4. Adjust the parameters in the update wizard to reflect the desired changes (e.g., updating VPC or subnet configurations).

5. Complete the remaining steps in the wizard to update the stack.

### Expanding Availability Zones

When expanding to additional availability zones, keep in mind that availability is determined by the subnets where your EC2 instances are running. The availability zones parameter helps you identify available subnets, but modifying this parameter alone will not impact availability. Ensure that your subnets are correctly configured to support the desired availability zones.

Use the **VPC Resource Map** in the AWS console to find subnets corresponding to your desired availability zones.

<Frame caption="VPC Resource Map">
  <img src="https://www.gitpod.io/images/docs/flex/runners/vpc_resource_map.png" />
</Frame>
