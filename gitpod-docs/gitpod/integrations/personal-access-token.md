# Personal Access Tokens

Personal access tokens (PATs) provide a way to authenticate and authorize programmatic access to Gitpod. You can use PATs as an alternative to using your password for authentication when using the Gitpod CLI or API.

## Creating a PAT

To create a personal access token:

1. Go to [Personal access tokens in the settings](https://app.gitpod.io/projects#/settings/personal-access-tokens)
2. Click "New Token"
3. Enter a description for your token
4. Select an expiration period (30, 60, or 90 days)
5. Click "Create"
6. Copy the generated token immediately. For security reasons, you won't be able to see it again.

## Using a PAT

You can use a personal access token to authenticate with the Gitpod CLI:

```sh
gitpod login --token <your-token>
```

## Token Permissions

Personal access tokens currently have the same permissions as your user account. They cannot be scoped down to specific actions or resources.

## Managing PATs

You can view and manage your personal access tokens at [https://app.gitpod.io/projects#/settings/personal-access-tokens](https://app.gitpod.io/projects#/settings/personal-access-tokens).

From this page, you can:

* View existing tokens
* Create new tokens
* Remove/Revoke tokens

## Security Considerations

* Treat personal access tokens like passwords. Do not share them or store them in insecure locations.
* Use the shortest expiration period that meets your needs.
* Revoke tokens that are no longer needed.
* Actions performed using a PAT will be logged in the audit logs, referencing the token ID.

## Example Use cases for PATs

### CI/CD Integration

Use a PAT to authenticate your CI/CD pipeline with Gitpod. This allows your automated workflows to create, manage, or interact with Gitpod environments without requiring manual authentication.

Example:

```yaml
name: Gitpod Integration
on: [push]
jobs:
    create-environment:
    runs-on: ubuntu-latest
    steps:
        - name: Create Gitpod Environment
        env:
            GITPOD_TOKEN: ${{ secrets.GITPOD_PAT }}
            GITPOD_CLASS: some-class-id
        run: |
            gitpod login --token $GITPOD_TOKEN
            gitpod environment create --class-id $GITPOD_CLASS https://github.com/your-repo
```

### Scripted Environment Management

Write scripts to manage your Gitpod environments programmatically. This is useful for tasks like bulk operations or scheduled maintenance.

Example:

```python
import subprocess
import json

GITPOD_PAT = "your_personal_access_token"

def run_gitpod_command(*args):
    result = subprocess.run(
        ["gitpod"] + list(args),
        capture_output=True,
        text=True,
        check=True
    )
    return result.stdout.strip()

# Login to Gitpod CLI using PAT
run_gitpod_command("login", "--token", GITPOD_PAT)

# List all environments
environments_json = run_gitpod_command("environment", "list", "-o", "json")
environments = json.loads(environments_json)

# Stop all running environments
for env in environments:
    if env['status']['phase'] == 'ENVIRONMENT_PHASE_RUNNING':
        print(f"Stopping environment {env['id']}")
        run_gitpod_command("environment", "stop", env['id'])

print("All running environments have been stopped.")
```

### Third-Party Tool Integration

Integrate Gitpod with third-party development tools or services that need to access your Gitpod account. The PAT allows these tools to authenticate and perform actions on your behalf using the Gitpod CLI.

Example (using a hypothetical code review tool):

```python
import subprocess
from code_review_tool import CodeReviewClient

# Initialize code review client
cr_client = CodeReviewClient(api_key="code_review_api_key")

# Gitpod PAT
GITPOD_PAT = "your_gitpod_pat"

# When a new code review is created
def on_new_review(review):
    # Login to Gitpod CLI using PAT
    subprocess.run(["gitpod", "login", "--token", GITPOD_PAT], check=True)

    # Create a Gitpod environment for the review
    result = subprocess.run(
        ["gitpod", "environment", "create", review.repo_url, "--dont-wait"],
        capture_output=True,
        text=True,
        check=True
    )

    # Extract the environment ID from the CLI output
    env_id = result.stdout.strip()

    # Get the environment details
    result = subprocess.run(
        ["gitpod", "environment", "get", env_id, "-o", "json"],
        capture_output=True,
        text=True,
        check=True
    )

    import json
    env_details = json.loads(result.stdout)

    # Add the Gitpod environment URL to the review
    cr_client.add_comment(review.id, f"Gitpod environment: {env_details['url']}")
```
