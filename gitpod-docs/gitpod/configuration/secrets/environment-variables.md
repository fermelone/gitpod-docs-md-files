# Environment Variables

Environment variables allow you to store and manage configuration settings that your application needs at runtime. These variables are accessible to your application's processes as standard environment variables, enabling you to:

* Configure your application for different environments (development, staging, production)
* Store configuration settings separate from your code
* Manage API keys and other configuration values

Environment Variable secrets you create in the Gitpod dashboard become accessible as system environment variables in your environment. The name you provide for the secret becomes the environment variable name.

## When to use Environment Variables

**Security Consideration**: For sensitive data (passwords, API tokens, private keys), we strongly recommend using [**files**](/flex/secrets/files) instead of environment variables.

### Comparison: Files vs Environment Variables

| Files                                           | Environment Variables                      |
| ----------------------------------------------- | ------------------------------------------ |
| Support complex structures (JSON, certificates) | Limited to simple string values            |
| Not visible in process listings                 | Visible via `ps auxe` commands             |
| Not included in crash reports or logs           | Often dumped in logs and error reports     |
| Explicitly used by processes                    | Automatically inherited by child processes |

Use environment variables for non-sensitive configuration like feature flags, API endpoints, or application modes.

## Creating an Environment Variable Secret

To create an Environment Variable Secret:

1. Navigate to secret managent in your Gitpod dashboard

* **Project > Secrets > New Secret** for Project secrets
* **Settings > Secrets > New Secret** for User secrets

2. Select **Environment Variable** from the type dropdown
3. Configure the following fields:
   * **Type of secret**: "Environment Variable" (cannot be changed after creation)
   * **Name**: A unique identifier (3-127 characters, only alphanumeric characters, underscores, and hyphens)
   * **Value**: The value to be stored (maximum size: 4KB)

<Frame caption="Secrets Create Environment">
  <img src="https://www.gitpod.io/images/docs/flex/secrets/secret-create-envvar.png" />
</Frame>

## Accessing Environment Variables

Once created, environment variables are automatically available in your Gitpod environment as system environment variables by the name you provided. No special code is required to access them.

## Updating an Environment Variable Secret

You can update the value of an environment variable at any time:

1. Navigate to secret managent in your Gitpod dashboard

* **Project > Secrets** for Project secrets
* **Settings > Secrets** for User secrets

2. Click the `Edit` button
3. Update the value
4. Click `Save`

<Frame caption="Secrets Update Environment">
  <img src="https://www.gitpod.io/images/docs/flex/secrets/secret-update-envvar.png" />
</Frame>

When you update a secret value:

* **New environments** will receive the updated value
* **Existing running environments** will continue to use the old value until they are restarted
* To apply updates to running environments, you must restart them

## Deleting an Environment Variable Secret

To delete an environment variable:

1. Navigate to secret managent in your Gitpod dashboard

* **Project > Secrets** for Project secrets
* **Settings > Secrets** for User secrets

2. Click the `Delete` button
3. Confirm the deletion

After deletion:

* New environments launched from the project will no longer have access to the secret
* Existing environments that already have the secret will retain it until those environments themselves are deleted

**Note:** When a project is deleted, all its secrets are automatically deleted as well.
