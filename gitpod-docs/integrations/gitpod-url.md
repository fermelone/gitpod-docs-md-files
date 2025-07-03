# Gitpod URL

You can open a Gitpod environment directly using a URL. The simplest way to start an environment is by using the format:

```
https://app.gitpod.io/#<repository-url>
```

This provides an alternative to creating environments with the [browser extension](/gitpod/integrations/browser-extension).

## URL Structure

The URL consists of the Gitpod instance URL followed by `#` and the full repository URL.

### Examples

* `https://app.gitpod.io/#https://github.com/gitpod-io/empty`
* `https://app.gitpod.io/#https://gitlab.com/gitpod-io/empty`
* `https://app.gitpod.io/#https://bitbucket.org/gitpod-io/empty`

## Choosing a Runner and Environment Class

When you open a repository in Gitpod, you will be prompted to choose a runner and environment class.

To configure a default for the environment class and runner for a repository, create a Project with your preferred configuration. When a project exists on a repository users in your organization are trying to open, it will be selected automatically.

## Next Steps

* Configure your [user settings](/gitpod/account/user-settings) to set default preferences such as your preferred editor
* Learn about [organization policies](/gitpod/organizations/policies) for team-wide configurations such as requiring users to use a project when creating an environment
