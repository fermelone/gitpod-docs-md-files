# Dotfiles

> Dotfiles are a way to customize your developer environment according to your personal needs.

Dotfiles are a way to customize your developer environment according to your personal needs. This guide explains how to configure and troubleshoot dotfiles in Gitpod.

## What are dotfiles?

Dotfiles are configuration files that customize your shell, editor, and other applications. They're called "dotfiles" because they typically begin with a dot (`.`) in Unix-like systems. Common examples include `.zshrc`, `.vimrc`, and `.gitconfig`.

## Why use dotfiles with Gitpod?

Gitpod standardizes developer environments to ensure consistency across your team - every colleague gets the same environment configuration when they start a new environment. This is great as it means you have everything you need to start coding on a project. However, because it's shared by all colleagues you might be missing some of the customizations you're used to when working locally on your own machine.

This is where dotfiles come in. They allow you to customize your standardized Gitpod environment according to your personal needs and preferences, making you feel right at home while still maintaining the benefits of a consistent base environment. When you configure dotfiles with Gitpod, your personal customizations are automatically applied every time you start a new environment, regardless of the repository you're working on.

## Setting up your dotfiles repository

To configure Gitpod to use your dotfiles for all your environments:

1. Create a Git repository with your dotfiles. If you're unfamiliar with dotfiles, check out [GitHub's dotfiles guide](https://dotfiles.github.io) or [awesome-dotfiles](https://github.com/webpro/awesome-dotfiles) for inspiration and examples.
2. Navigate to [Settings > Preferences][dotfiles-preferences]
3. Enter the URL of your dotfiles repository

When you start a new environment, Gitpod will:

1. Clone your dotfiles repository to `~/.dotfiles`
2. Execute the first of the following files:
   * `install.sh` or `install`
   * `bootstrap.sh` or `bootstrap`
   * `setup.sh` or `setup`

## Best practices for dotfiles in Gitpod

For the best experience with dotfiles in Gitpod:

* Keep your install script lightweight to minimize environment startup time. Smaller repositories and simpler scripts lead to faster environment creation.
* Ensure your install script runs without requiring user interaction, otherwise the environment creation will hang (see troubleshooting section for more details).
* Don't store secrets in your dotfiles repository. Use Gitpod's [secret feature](https://app.gitpod.io/settings/secrets) instead for sensitive information.
* Remember that you're limited to one dotfiles repository per user.

## Managing changes to your dotfiles

When you make changes to your dotfiles repository:

* Changes will be automatically applied when creating new environments
* Existing running environments won't automatically pick up the changes
* To apply changes to an existing environment, you'll need to manually `git pull` and re-run your installation script, e.g. `(cd ~/dotfiles && git pull && ./bootstrap.sh)`

If you're actively iterating on your dotfiles, then the following workflow can be helpful:

* Create a new environment from your dotfiles repository
* Make changes to your files and run your install script to validate the changes
* If you need to reset the environment, e.g. if you're iterating on something that changes the state of the environment such as installing tools, then you can run `gitpod environment devcontainer rebuild` to remove any manual modifications you've made.

## Troubleshooting

### My dotfiles failed to install

Dotfiles are installed during dev container creation. If your dotfiles failed to apply, check the environment logs section "Creating dev container" for any errors or messages that can help you debug the issue.

### Failed to clone

If it failed to clone your dotfiles, you should see an error message like the one below:

```
fatal: repository 'https://github.com/mads-hartmann/gitpod-dotfiles-does-not-exist/' not found
```

Please validate that the repository URL you have configured points to an existing repository.

### Failed to install

If it manged to clone your dotfiles, but failed while running your install script, then you likely won't see much information in the logs. Instead you can try to reproduce the error by manually running the install script

```sh
cd ~/dotfiles
# Replace install.sh with the install script you have in your dotfiles repository
./install.sh
```

If you're seeing failures in some repositories but not other it could be because your dotfiles have system dependencies that are not covered in the dev container configuration of the repository. In that case, you can make your dotfiles self-contained by having them check for the existence of the dependencies and install them if they're missing.

Here's an example where [fzf](https://github.com/junegunn/fzf) is installed only if it doesn't exist already:

```sh
FZF_VERSION="0.60.3"
if ! command -v fzf >/dev/null 2>&1; then
    echo "Installing fzf..."
    curl -L https://github.com/junegunn/fzf/releases/download/v${FZF_VERSION}/fzf-${FZF_VERSION}-linux_amd64.tar.gz | tar xzvf -
    sudo mv fzf /usr/local/bin
    echo "fzf installation completed"
else
    echo "fzf is already installed"
fi
echo "Configuring fzf..."
echo "source <(fzf --zsh)" >> $HOME/.zshrc
```

### My dotfiles cause the environment to hang during startup

Your install script is executed in a non-interactive shell without a TTY. This means that commands which require user interaction or expect an interactive terminal can cause the dev container creation to hang.

Make sure your install script can run non-interactively without requiring terminal input. You may need to modify commands that assume an interactive terminal is available, like `read` prompts or interactive installers.

The easiest way to resolve this is to:

1. Remove your Dotfiles repository from [Settings > Preferences](https://app.gitpod.io/settings/preferences)
2. Start a fresh environment
3. Manually clone your Dotfiles repository and run your install script to see where it's getting stuck
4. Resolve the issues, commit and push your changes to your Dotfiles repository
5. Re-add your Dotfiles repository URL in [Settings > Preferences](https://app.gitpod.io/settings/preferences)
6. Start a new environment to see if the issue is resolved

## FAQs

### How do I configure the default shell?

You can use the `chsh` command to change the login shell for your user by adding the following to your dotfiles install script. The example below sets the default shell to `zsh` for the active user.

```sh
sudo chsh "$(id -un)" --shell "/usr/bin/zsh"
```

The `chsh` command modifies the user's login shell in `/etc/passwd` which persists across sessions since `/etc/passwd` defines the default shell.

[dotfiles-preferences]: https://app.gitpod.io/settings/preferences
