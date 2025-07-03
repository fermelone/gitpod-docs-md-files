# Editors & IDEs

Gitpod development environments are accessible through your preferred editor or CLI. You can connect your favorite code editor to Gitpod environments, allowing you to work in a familiar interface while leveraging Gitpod's cloud infrastructure.

## Connecting Your Editor

Gitpod supports multiple ways to connect your editor to development environments:

* **Direct Launch**: VS Code, VS Code Browser, Cursor, and JetBrains IDEs can be launched directly from the Gitpod user interface. Use the "Open in VS Code" button for VS Code, or buttons like "Open IntelliJ IDEA Ultimate" for JetBrains IDEs.

* **SSH Configuration**: Editors like Zed can connect via SSH. Simply run `gitpod env ssh-config` to set up the SSH configuration for your environment.

Gitpod works with any editor that supports SSH connections to remote backends, giving you flexibility to use your preferred development tools.

## Supported Editors

Gitpod officially supports these editors:

* **VS Code**: Launches directly from the Gitpod interface with required extensions automatically installed
* **VS Code Browser**: Launches directly in the Browser without the need to install additional tools
* **Cursor**: Similar to VS Code with direct integration through the Gitpod interface
* **JetBrains IDEs**: Connect through JetBrains Toolbox
* **Zed**: Connect using SSH configuration

## Prerequisites

Each editor has specific requirements:

* **VS Code/Cursor**: Requires extensions (Gitpod, Remote-SSH, Dev Containers) which are automatically installed when launching from Gitpod
* **JetBrains IDEs**: Requires [JetBrains Toolbox](https://www.jetbrains.com/toolbox-app/) installed
* **SSH-based editors**: Requires running `gitpod env ssh-config` to configure the connection

See [the integrations](/flex/editors) page for detailed setup instructions for each supported editor.
