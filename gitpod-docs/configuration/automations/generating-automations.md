# Generating Automations

> Explore Gitpod's automation features: Services and Tasks. Learn how to configure long-running services and execute specific tasks to streamline your development workflow. Understand execution options, dependencies, and best practices for efficient environment management.

Dynamic Automations in Gitpod allow you to create and update environment Automations on the fly, adapting your development environment to changing needs without manually editing configuration files.

## Creating Automations

To create a dynamic automation, use the Gitpod CLI to generate or obtain the automation configuration and pipe it directly into the `gitpod automations update -` command. Notice the `-` at the end which signals that we want to read the Automations from stdin.

> When generating tasks and services, keep in mind that their IDs can only contain alphanumeric characters, underscores, and hyphens, and must be between 1 and 128 characters long.

Basic example:

```bash
echo '{"tasks": {"update_deps": {"name": "Update dependencies", "command": "npm update"}}}' | gitpod automations update -
```

## Example uses

* **Exposing Package Scripts**: Create tasks from scripts in a `package.json` file:

  ```bash
  jq -r '.scripts | to_entries[] | {(.key | gsub("[^a-zA-Z0-9_-]"; "_")): {"name": .key, "command": .value}}' package.json |
  jq -s 'add | {"tasks": .}' |
  gitpod automations update
  ```

  This example uses `gsub` to ensure all task IDs comply with the required format.

* **Dynamic Service Creation**: Create services for components in a specific directory:

  Suppose you have a `components` directory which contains a set of Go components. The following command creates services
  for each of those components.

  ```bash
  find ./components -type d -maxdepth 1 -mindepth 1 |
  jq -R '{(. | gsub("[^a-zA-Z0-9_-]"; "_")): {"name": "Start " + ., "command": "cd " + . + " && go run ."}}' |
  jq -s 'add | {"services": .}' |
  gitpod automations update -
  ```

* **Remote Automation Configuration**: Download and apply Automations from a remote source:

  ```bash
  curl https://example.com/gitpod-automations.json | gitpod automations update -
  ```

  > Only ever download Automations from sources you trust; better yet, verify the integrity of the Automations file before applying it.

  Make sure that the remote configuration file uses compliant task and service IDs.

## Interacting with Dynamic Automations from Outside an Environment

One of Gitpod's most powerful features is the ability to interact with and control Automations from outside the environment itself. This capability, combined with Gitpod's environment management features, transforms Gitpod into a flexible automation and execution platform. You can orchestrate complex workflows and tasks without needing to be actively connected to an environment.

When interacting with Automations from outside an environment, you can perform the same operations as from within an environment:

* **Execute Tasks**: Start, monitor, and manage automation tasks in remote environments.
* **Control Services**: Start, stop, and manage long-running automation services.
* **Access Logs**: Retrieve and monitor logs from tasks and services running in the environment.
* **Update Automations**: Modify automation configurations for environments on the fly.

These operations can all be performed using the Gitpod CLI from your local machine or integrated into your CI/CD pipelines for even greater automation potential.

### Example Workflow: Create, Execute Automation, and Clean Up

Here's a concrete example of how you might use these capabilities along with Gitpod's environment management to create an environment, run an automation task, and then clean up:

```bash
# 1. Create a new environment (find an environment class using \"gitpod environment list-classes\")
ENV_ID=$(gitpod environment create https://github.com/your-repo/your-project --dont-wait --class-id some-env-class-id)

# 2. Start a specific automation task in the environment
TASK_ID=$(gitpod automations task start build-and-test --environment-id $ENV_ID)

# 3. Wait for the automation task to complete
gitpod automations task logs $TASK_ID --environment-id $ENV_ID

# 4. Check the automation task status
TASK_STATUS=$(gitpod automations task get $TASK_ID --environment-id $ENV_ID -o json | jq -r .status)

# 5. Clean up the environment
if [ "$TASK_STATUS" = "succeeded" ]; then
    echo "Automation task completed successfully. Cleaning up environment."
    gitpod environment delete $ENV_ID
else
    echo "Automation task failed. Environment left running for inspection."
fi
```

This script demonstrates how you can:

1. Create a new environment based on a Git repository.
2. Start a specific automation task (in this case, 'build-and-test') in that environment.
3. Stream the logs of the automation task to monitor its progress.
4. Check the final status of the automation task.
5. Based on the task's outcome, either clean up the environment or leave it running for further investigation.

### Benefits of External Automation Control

1. **CI/CD Integration**: Easily integrate Gitpod Automations into your existing CI/CD pipelines.
2. **Batch Processing**: Set up and run multiple automation tasks across different environments in parallel for large-scale operations.
3. **Automated Testing**: Create ephemeral environments for running automated test suites without manual intervention.
4. **Resource Optimization**: Run Automations in environments only when needed and automatically clean them up after use.

By leveraging these external automation capabilities alongside Gitpod's environment management features, you can create powerful, flexible workflows. This enables you to automate complex development and testing processes with ease, all while maintaining full control from outside the environment.
