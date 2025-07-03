# Configuring Repository Access

Repository access configuration is only required if you want to create Environments from repositories (GitHub, GitLab, etc.). If you only need to create empty Environments, you can skip this configuration. However, to launch Environments from any repository, the Runner **must** be configured with a provider that can access your repos (this includes public repositories).

Press **Add a provider** and select one of the supported providers such as GitHub:

<Frame caption="Repository provider">
  <img src="https://www.gitpod.io/images/docs/flex/runners/repository-provider.png" />
</Frame>

Configure the host, or leave the default if using github.com. If you want to support multiple hosts, you can add a separate provider for each host.

<Frame caption="GitHub OAuth">
  <img src="https://www.gitpod.io/images/docs/flex/source-control/github-enable-oauth.png" />
</Frame>

Next, choose at least one of OAuth or Personal Access Token support. You can set up an **OAuth** app to make it easy for users to sign in quickly. **Personal Access Token** allows users to provide their own PAT to sign in. Users will be prompted to authenticate before they start a new Environment on the Runner.

<Frame caption="Setup OAuth">
  <img src="https://www.gitpod.io/images/docs/flex/runners/setup-oauth.png" />
</Frame>

Press **Save** once done. You can now start Environments for repos on the specified host:

<Frame caption="AWS runner setup done">
  <img src="https://www.gitpod.io/images/docs/flex/runners/aws-runner-setup-done.png" />
</Frame>

Whenever a user starts an Environment for the first time for that host, they will get prompted to authenticate first, and get the option to authenticate through the OAuth app or using a PAT token (whichever is configured in the integration). Once authenticated, the token is encrypted and stored to be remembered for the next time the user creates an Environment for this host.

When an admin disables OAuth/PAT support in an integration, or deletes an integration entirely for a host, any existing tokens obtained for the host through the disabled/deleted authentication method will get deleted and users might have to re-authenticate before they can create Environments again for that host.
