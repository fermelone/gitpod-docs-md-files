# Deleting a runner

> Learn how to delete runners in Gitpod.

To delete a runner, go to the runners page, and select **Delete** from the overflow menu.

<Frame caption="Delete a runner">
  <img src="https://www.gitpod.io/images/docs/flex/runners/delete-runner.png" />
</Frame>

This will start deletion of the runner and all its environments. The runner will move into a **Pending deletion** phase, and stop + delete any existing environments on the runner. Once all environments are deleted, the runner itself will get deleted, which can take a few more minutes.

Once deleted, you can clean up the CloudFormation stack in your AWS account associated with the runner.
