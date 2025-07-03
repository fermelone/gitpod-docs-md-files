# Dev Container Image Cache

> Learn how to use the dev container image cache feature for AWS runners to significantly reduce environment startup times by automatically caching built devcontainer images in AWS ECR.

The dev container image cache feature automatically stores built devcontainer images in AWS ECR (Elastic Container Registry), enabling environments with identical devcontainer configurations to reuse previously built images. This significantly reduces startup times by eliminating the need to rebuild containers from scratch.

## Overview

When you create an environment with a devcontainer configuration, Gitpod typically needs to build the container image, which can take several minutes depending on complexity. The dev container image cache stores these built images in a secure container registry, allowing subsequent environments with the same configuration to start in seconds rather than minutes.

## How it works

1. **Hash computation**: When starting an environment, Gitpod computes a hash based on your devcontainer configuration, including:
   * Contents of `devcontainer.json`
   * Contents of any referenced `Dockerfile`

2. **Cache lookup**: Gitpod checks if an image with this hash already exists:
   * If found in registry: Pulls and uses the cached image
   * If not found: Builds new image, pushes to registry, then uses it

3. **Shared caching**: The cache is shared across all users within a project. The first team member who creates an environment with a new devcontainer configuration builds and caches the image. All subsequent environments created by any team member in the same project with identical configuration use the shared cached version. When rebuilding an existing environment's dev container, it will also try to pull from the cache but won't push new images (only the initial dev container build when an environment gets created can push to the cache).

<Note>
  Non-project environments (such as those started directly from a context URL) do not use the cache.
</Note>

## Enabling and disabling the cache

### For new runners

The dev container image cache is **enabled by default** for new AWS runners.

<Note>
  Disabling the cache is only available on Core and Enterprise tiers.
</Note>

### For existing runners

To enable the cache for existing runners:

1. [Update your CloudFormation stack](/gitpod/runners/aws/update-runner#updating-infrastructure) to the latest version that supports the cache
2. Go to **Settings → Runners** in your Gitpod organization
3. Select your AWS runner
4. Toggle **Dev container image cache** to enabled
5. Click **Save**

<Warning>
  Upgrading CloudFormation templates that were applied from January 2025 or earlier will cause existing environments to no longer be accessible due to SSH port changes. Before upgrading, either stop and discard existing environments, or manually update the security group to allow access from 0.0.0.0/0 to port 22 (in addition to port 29222) after upgrading the stack.
</Warning>

<Frame caption="Configuring an AWS runner">
  <img src="https://www.gitpod.io/images/docs/flex/runners/aws-runner-configuration.png" />
</Frame>

### Disabling the cache

To disable caching:

1. Go to **Settings → Runners** in your Gitpod organization
2. Select your AWS runner
3. Toggle **Dev container image cache** to disabled
4. Click **Save**

<Note>
  Disabling the cache prevents new images from being cached and stops existing environments from pulling from the cache on rebuild. Existing cached images remain in ECR until they expire (30 days) or are manually deleted.
</Note>

## What gets cached

The cache includes everything from a `devcontainer build` of your configuration:

* **Base image layers**: Your specified base image and any modifications
* **Dev container features**: All configured features are pre-installed
* **Build steps**: RUN commands, COPY operations, and other Dockerfile instructions
* **Tool installations**: Package managers, development tools, and dependencies

**What is NOT cached:**

* Lifecycle hooks (`onCreateCommand`, etc.) - these run after the container starts
* User-specific configurations applied at runtime
* Files that change after container creation

## Shared cache considerations

The dev container image cache is designed as a shared resource within each project to maximize efficiency and reduce build times across your team. This shared approach means:

* **Team efficiency**: Only the first team member to use a new devcontainer configuration experiences the full build time
* **Consistent environments**: All team members use identical container images, ensuring environmental consistency
* **Resource optimization**: Eliminates redundant builds across team members

### Enterprise security considerations

For organizations with strict security requirements, it's important to understand the shared nature of the cache:

* **Configuration integrity**: Images are cached based on exact configuration hashes, ensuring consistency
* **Limited push access**: Only the initial dev container build when an environment gets created can push images to the cache, and push credentials are removed from the environment afterward
* **Immutable storage**: ECR's immutability feature prevents modification of cached images once stored
* **Project isolation**: Cache access is strictly limited to the same project, preventing cross-project contamination

Organizations with enhanced security policies may choose to disable the cache to maintain complete control over container image provenance, though this comes with the trade-off of longer environment startup times.

## Security considerations

The dev container image cache implements several security measures:

### Access isolation

* **Project-scoped access**: Images are only accessible within the same project
* **Hash-based immutability**: Once pushed, images cannot be modified
* **Credential separation**: Distinct push and pull permissions

### Credential management

* **Push credentials**: Only granted during the initial dev container build when an environment gets created, then removed from the environment
* **Pull credentials**: Provided to all environments in the project, refreshed periodically
* **Temporary access**: All credentials use AWS IAM temporary credentials with minimal required permissions

### Registry security

* **Immutable repositories**: ECR repositories prevent image tampering once pushed
* **AWS IAM controls**: Access controlled through AWS session tags and IAM policies
* **Regional isolation**: Images stored in the same AWS region as your runner

## Image lifecycle

### Automatic expiry

Cached images automatically expire after **30 days** to:

* Prevent unlimited storage growth
* Ensure images are periodically rebuilt with security updates
* Reduce storage costs

### Cache invalidation

A new image is built and cached when:

* The devcontainer configuration hash changes (any modification to `devcontainer.json` or referenced `Dockerfile`)
* The cached image has expired
* The cached image is manually deleted from ECR

## Forcing a new image build

To force rebuilding and re-caching an image, you need to change the configuration hash. You can:

### Method 1: Modify devcontainer configuration

Add or modify any content in your `devcontainer.json` or `Dockerfile`, such as:

```json
{
  "name": "My Dev Container",
  "image": "mcr.microsoft.com/devcontainers/typescript-node:0-18",
  // Add a comment to force rebuild: 2024-01-15
  "features": {
    "ghcr.io/devcontainers/features/git:1": {}
  }
}
```

### Method 2: Add a comment to Dockerfile

If using a custom Dockerfile:

```dockerfile
FROM node:18
# Force rebuild: 2024-01-15
RUN npm install -g typescript
```

### Method 3: Delete the image from ECR

1. Go to AWS ECR console
2. Navigate to your runner's repository: `gitpod-runner-{runnerID}/projects/{projectID}/image-build`
3. Delete the specific image tag
4. The next environment creation will rebuild and cache the image

## Troubleshooting

### Cache not working

If images aren't being cached:

1. **Check runner configuration**: Ensure the dev container image cache is enabled in runner settings
2. **Verify CloudFormation version**: Older CloudFormation templates don't support caching
3. **Check AWS permissions**: Ensure the runner has ECR access permissions
4. **Check runner logs**: Look for cache-related errors in the runner's CloudWatch logs
5. **Review environment logs**: Look for cache-related error messages

### Slow startup despite cache

If environments are still slow to start:

1. **Check cache hit**: Look for "Using pre-built dev container" in environment logs
2. **Verify image size**: Large images take longer to pull
3. **Check environment type**: Docker Compose-based devcontainers are not supported by the cache
4. **Review lifecycle hooks**: Lifecycle hooks (`onCreateCommand`, etc.) are not cached and may install tools that increase startup time. Consider moving these steps to the Docker build where possible
5. **Verify project-based environment**: Non-project environments do not use the cache

## Supported configurations

### Supported

* Standard devcontainer configurations with `Dockerfile` or `image` reference
* Dev container features from any registry

### Not supported

* Docker Compose-based devcontainers (due to limited devcontainer CLI support)
* Non-project environments (e.g. environments started directly from a context URL)
* Runners other than AWS EC2 runners

## Storage and costs

### Storage costs

* Images are stored in AWS ECR in your account
* Storage costs depend on image size and number of unique configurations
* 30-day automatic expiry helps manage costs
* ECR repositories inherit all tags from the CloudFormation stack (useful for cost allocation and AWS MAP programs)

### Cost optimization

* Similar devcontainer configurations share base layers, reducing storage
* Regional storage (same region as runner) minimizes transfer costs
* Automatic expiry prevents accumulation of unused images

### Repository location

Cached images are stored in ECR repositories with the naming pattern:
`gitpod-runner-{runnerID}/projects/{projectID}/image-build`

Each project gets its own repository within the runner's ECR namespace, ensuring proper isolation and organization.

## Monitoring and visibility

### Environment logs

Cache operations are logged during environment creation in the `Creating dev container` log section when a cache hit occurs:

```
⚡️ Using pre-built dev container (saved ~3m45s build time)
```

The cache provides significant performance improvements while maintaining security and cost efficiency through automated management.
