# Files

File secrets mount sensitive data as actual files in your Gitpod environment at a specified location. These files are automatically created when your environment starts, allowing your applications to read them like any other file on the filesystem.

## When to use File Secrets

File secrets are the recommended choice for:

* **Complex data structures** - JSON configurations, certificates, or other multi-line content
* **Sensitive credentials** - API keys, authentication tokens, and passwords
* **Binary data** - Certificates, keystore files, or other non-text content
* **Configuration that applications expect in file format** - Many applications look for specific configuration files

## Creating a File Secret

To create a File Secret:

1. Navigate to secret managent in your Gitpod dashboard

* **Project > Secrets > New Secret** for Project secrets
* **Settings > Secrets > New Secret** for User secrets

2. Select **File** from the type dropdown
3. Configure the following fields:
   * **Type of secret**: "File" (cannot be changed after creation)
   * **Name**: A unique identifier (3-127 characters, only alphanumeric characters, underscores, and hyphens)
   * **Value**: The content to be stored in the file (maximum size: 4KB)
   * **Mount Path**: The filepath where the secret will be mounted in your environment (cannot be changed after creation)

<Frame caption="Secrets Create File">
  <img src="https://www.gitpod.io/images/docs/flex/secrets/secret-create-filepath.png" />
</Frame>

## Accessing File Secrets

Once created, the file secret is automatically mounted at the specified path in your Gitpod environment. Your application can read it like any other file on the filesystem. No special code is required to access the file beyond normal file system operations.

## Updating a File Secret

You can update the content of a file secret at any time, although the mount path cannot be changed once the secret is created.

1. Navigate to the **Project > Secrets** page in your Gitpod dashboard
2. Click the `Edit` button
3. Update the value
4. Click `Save`

<Frame caption="Secrets Update File">
  <img src="https://www.gitpod.io/images/docs/flex/secrets/secret-update-filepath.png" />
</Frame>

When you update a secret value:

* **New environments** will receive the updated file content
* **Existing running environments** will continue to use the old file content until they are restarted
* To apply updates to running environments, you must restart them
* The mount path cannot be changed after creation

## Deleting a File Secret

To delete a file secret:

1. Navigate to the **Project > Secrets** page in your Gitpod dashboard
2. Click the `Delete` button
3. Confirm the deletion

After deletion:

* New environments launched from the project will no longer have access to the secret
* Existing environments that already have the secret will retain it until those environments themselves are deleted

**Note:** When a project is deleted, all its secrets are automatically deleted as well.
