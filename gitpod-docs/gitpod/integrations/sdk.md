# Gitpod SDK

The Gitpod SDK provides powerful tools for developers to interact programmatically with Gitpod environments. It allows you to automate environment creation, run tasks, manage automations, and scale infrastructure with Gitpod runners. Available in Python, Node/Typescript, and Go, the SDK gives developers flexibility in their choice of language.

### SDKs Available

* **[Python SDK](https://pypi.org/project/gitpod-sdk/)**: For Python developers interacting with Gitpod environments.
* **[Node/Typescript SDK](https://www.npmjs.com/package/@gitpod/sdk)**: For JavaScript and TypeScript developers.
* **[Go SDK](https://github.com/gitpod-io/gitpod-sdk-go)**: For Go developers integrating with Gitpod.

For detailed API references, consult the [Gitpod API Reference](https://www.gitpod.io/docs/api-reference).

## End-to-End Walkthrough

Watch the video below to see an end-to-end walkthrough of how to use the Gitpod SDK. The steps below are based on the video.

<div className="mux-player-container" data-playback-id="qY6SHjCM4mU76W45NtOmf7tiZ6ZMACY4whYe59blaUc" data-title="Gitpod SDK" />

<br />

### 1. **Sign Up at Gitpod**

* Go to [app.gitpod.io](https://app.gitpod.io) and sign up for a Gitpod account.
* Once logged in, generate a **Personal Access Token** for SDK authentication under your account settings at [Gitpod Personal Access Tokens](https://app.gitpod.io/settings/personal-access-tokens).

### 2. **Install the SDK**

You need to install the Gitpod SDK for your preferred language. Here’s how to do it for the three SDKs:

* **Python SDK**:
  ```bash
  pip install gitpod-sdk
  ```
* **Node/Typescript SDK**:
  ```bash
  npm install @gitpod/sdk
  ```
* **Go SDK**:
  ```bash
  go get github.com/gitpod-io/gitpod-sdk-go
  ```

### 3. **Authenticate with Gitpod**

Once you’ve installed the SDK, authenticate using your personal access token. You can either set it via the environment variable or explicitly pass it in your code.

* **Option 1**: Set the environment variable `GITPOD_API_KEY`:

  ```bash
  export GITPOD_API_KEY="your_token_here"
  ```

* **Option 2**: Authenticate directly in your code:

  * **For Python SDK**:

    ```python
    from gitpod_sdk import Gitpod

    gitpod = Gitpod(bearer_token="your_token_here")
    ```

  * **For Go SDK**:

    ```go
    package main

    import (
        "github.com/gitpod-io/gitpod-sdk-go"
    )

    func main() {
        gitpod := gitpod.NewGitpod("your_token_here")
    }
    ```

  * **For Node/Typescript SDK**:

    ```typescript
    import { Gitpod } from '@gitpod/sdk';

    const gitpod = new Gitpod({ bearerToken: 'your_token_here' });
    ```

### 4. **Run an Example**

Once authenticated, you can start experimenting with the SDK by running one of the examples. Here’s an example of how to create an environment and run a command inside it using the Python SDK:

```python
import asyncio
from gitpod import AsyncGitpod
import gitpod.lib as util

repo_url = "https://github.com/containerd/containerd"
command_to_execute = "go test -v -short ./..."

async def execute_command_in_environment():
    client = AsyncGitpod()

    machine_class_id = (await util.find_most_used_environment_class(client)).id

    create_params = {
        "machine": {"class": machine_class_id},
        "content": {"initializer": {"specs": [{"context_url": {"url": repo_url}}]}}
    }

    environment = (await client.environments.create(spec=create_params)).environment

    await util.wait_for_environment_running(client, environment.id)

    async for line in await util.run_command(client, environment.id, command_to_execute):
        print(line)

    await client.environments.delete(environment_id=environment.id)

if __name__ == "__main__":
    asyncio.run(execute_command_in_environment())
```

This example demonstrates:

* Creating a new environment initialized from a Git repository.
* Running a command inside the environment.
* Deleting the environment once the task is completed.

## Available Examples

Here are the available examples in the SDK repositories, with descriptions of what they demonstrate:

### 1. **Run a Command in an Environment**

* **Description**: Demonstrates how to initialize an environment from a Git repository and run a command inside it.
* **Location**: [Python SDK Example - Run Command](https://github.com/gitpod-io/gitpod-sdk-python/tree/main/examples/run_command.py)

### 2. **Run a Service in an Environment**

* **Description**: Demonstrates how to run a long-lived service (such as a database or message queue) inside a Gitpod environment.
* **Location**: [Python SDK Example - Run Service](https://github.com/gitpod-io/gitpod-sdk-python/tree/main/examples/run_service.py)

### 3. **Access the File System in an Environment**

* **Description**: Shows how to access and interact with the file system inside a Gitpod environment programmatically.
* **Location**: [Python SDK Example - File System Access](https://github.com/gitpod-io/gitpod-sdk-python/tree/main/examples/fs_access.py)

### 4. **Use the Anthropic Tool in a Gitpod Environment**

* **Description**: Demonstrates how to use the Anthropic tool within a Gitpod environment and interact with the **Model Context Protocol (MCP)**.
* **Location**: [Python SDK Example - Anthropic Tool Use](https://github.com/gitpod-io/gitpod-sdk-python/tree/main/examples/anthropic_tool_use.py)

### 5. **MCP Server Example**

* **Description**: Demonstrates the integration of the **Model Context Protocol (MCP)** in a Gitpod environment, used for managing model contexts.
* **Location**: [Go SDK Example - MCP Server](https://github.com/gitpod-io/gitpod-sdk-go/tree/main/examples/mcp-server)
