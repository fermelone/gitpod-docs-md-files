# Container Registry Secret

Container Registry Secrets allow you to use private Docker images as Dev Containers in your environment by providing authentication credentials for private container registries.

These container registry credentials will also be automatically available inside your environment when you include the `docker` CLI in your Dev Container image, allowing you to interact with private registries directly from your environment. If your Dev Container image does not include the `docker` CLI, you will see a warning in your environment creation page.

## When to use Container Registry Secrets

Use Container Registry Secrets when you need to:

* Pull Dev Container images from private registries
* Authenticate with container registries during your development workflow
* Work with private container images in your environment

> Currently, basic authentication (username/password) is supported for most registry types. AWS ECR is also supported through runner-native authentication when using AWS EC2 runners.

## Creating a Container Registry Secret

To create a Container Registry Secret:

1. Navigate to secret managent in your Gitpod dashboard

* **Project > Secrets > New Secret** for Project secrets
* **Settings > Secrets > New Secret** for User secrets

2. Select **Container Registry Basic Auth** from the type dropdown
3. Configure the following fields:
   * **Type of secret**: Select **Container Registry Basic Auth** from the dropdown. Once created, the type cannot be changed.
   * **Name**: A unique identifier (3-127 characters, only alphanumeric characters, underscores, and hyphens)
   * **Registry hostname**: The hostname of your container registry (cannot be changed after creation)
   * **Registry username**: Your username for the container registry
   * **Registry password**: Your password or access token for the container registry

<Frame caption="Secrets Create Registry">
  <img src="https://www.gitpod.io/images/docs/flex/secrets/secret-create-registry.png" />
</Frame>

#### Common Registry Hostnames

* Docker Hub: `https://index.docker.io/v1/` (note the https\:// prefix)
* GitHub Container Registry: `ghcr.io`
* GitLab Container Registry: `registry.gitlab.com`
* Azure Container Registry: `[registry-name].azurecr.io`
* Google Container Registry: `gcr.io`
* AWS ECR: \[account-id].dkr.ecr.\[region].amazonaws.com (with runner-native support on EC2 runners)

## Using AWS ECR with IAM authentication

Gitpod now supports AWS ECR registries with IAM based authentication when using AWS EC2 runners. This means you can access private ECR repositories without manually managing credentials.

### Prerequisites

* You must be using AWS EC2 runners for your Gitpod environments
* Your ECR registry and EC2 runners must be in the same AWS account or have appropriate cross-account access configured

### Setting up ECR Registry Access

* Navigate to Project > Secrets > New Secret in your Gitpod dashboard
* Select Container Registry Basic Auth from the type dropdown
* For the Registry hostname, enter your ECR registry hostname in the format: \[account-id].dkr.ecr.\[region].amazonaws.com
* When you enter an ECR registry hostname, the username and password fields will automatically be filled with runner-native to indicate that native runner authentication will be used
* Click Add

<Frame caption="ECR Registry Secret Setup">
  <img src="https://www.gitpod.io/images/docs/flex/secrets/secret-create-ecr-registry.png" />
</Frame>

### Configuring IAM Permissions

To enable your EC2 runners to access your ECR repositories, you need to configure the appropriate IAM permissions:

* Locate your runner environment's IAM role from your CloudFormation stack outputs
* Attach appropriate ECR permissions to this role to allow it to pull images from your ECR repositories
* Update the repository policy of your ECR repository to allow access from the runner's IAM role
* Ensure the IAM role's permission boundaries (if configured) include the required ECR permissions

Here's an example policy you can attach to your runner's IAM role:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ecr:GetAuthorizationToken"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "ecr:GetDownloadUrlForLayer",
        "ecr:BatchGetImage",
        "ecr:BatchCheckLayerAvailability"
      ],
      "Resource": "arn:aws:ecr:[region]:[account-id]:repository/[repository-name]"
    }
  ]
}
```

You'll also need to update the repository policy of your ECR repository to allow the runner's IAM role to access it. Here's an example ECR repository policy:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowGitpodRunnerPull",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::[account-id]:role/[runner-role-name]"
      },
      "Action": [
        "ecr:BatchGetImage",
        "ecr:GetDownloadUrlForLayer",
        "ecr:BatchCheckLayerAvailability"
      ]
    }
  ]
}
```

### Limitations

* ECR runner-native registry support is only available for AWS EC2 runners
* Your EC2 runners and ECR registry must have properly configured IAM permissions
* Existing environments must be recreated to apply changes to ECR permissions

## Accessing Container Registry Secrets

Once created, container registry secrets serve two purposes:

1. They authenticate with private registries to pull images for your Dev Container during environment creation.

2. If your Dev Container image includes the `docker` CLI, Gitpod automatically runs `docker login` inside your environment to enable continued access to the registry.

<Note>
  For AWS ECR registries, your Dev Container image needs both the `docker` CLI and `aws` CLI installed to authenticate properly.
</Note>

If authentication fails inside your environment, you'll see a warning in your environment creation dashboard. This won't prevent your environment from starting but will limit your ability to pull additional private images from within your environment.

## Updating a Container Registry Secret

You can update the username and password of a Container Registry Secret at any time:

1. Navigate to secret managent in your Gitpod dashboard

* **Project > Secrets** for Project secrets
* **Settings > Secrets** for User secrets

2. Find your Container Registry Secret and click the `Edit` button
3. Update the username and/or password
4. Click `Save`

<Frame caption="Secrets Update Registry">
  <img src="https://www.gitpod.io/images/docs/flex/secrets/secret-update-registry.png" />
</Frame>

When you update a Container Registry Secret:

* **New environments** will use the updated credentials
* **Existing running environments** will continue to use the old credentials until they are restarted
* **Registry hostname** cannot be modified after creation
* To apply updates to running environments, you must restart them

## Deleting a Container Registry Secret

To delete a Container Registry Secret:

1. Navigate to secret managent in your Gitpod dashboard

* **Project > Secrets** for Project secrets
* **Settings > Secrets** for User secrets

2. Find your Container Registry Secret and click the `Delete` button
3. Confirm the deletion

After deletion:

* New environments launched from the project will no longer have access to the secret
* Existing environments that already have the secret will retain it until those environments themselves are deleted
* This may cause image pull failures if your environment depends on images from that registry

**Note:** When a project is deleted, all its secrets are automatically deleted as well.
