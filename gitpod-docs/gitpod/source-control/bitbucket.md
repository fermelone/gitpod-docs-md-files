# Bitbucket Cloud

Source control integrations can be configured for both [Self-Hosted Runners](/flex/runners) and [Gitpod Desktop](/flex/gitpod-desktop). You can set up a Bitbucket integration during runner creation or in the runner settings. Self-hosted Bitbucket instances are currently not supported.

## Configuring Bitbucket Access

<Note>
  {' '}

  You can skip this step if someone has already set up the runner for you and SCM
  integration with Bitbucket has already been configured. In that case, you can
  go directly to [Authorizing Bitbucket Access](#authorizing-bitbucket-access).
  This step allows administrators to configure what authorization methods (OAuth,
  PATs) and SCM providers (GitHub, GitLab, Bitbucket, Azure DevOps) will be available
  for authorization.
</Note>

### Self-Hosted Runners

For self-hosted runners (like AWS), Bitbucket integration is configured during runner creation or in the runner settings.

We are currently supporting OAuth for authorizing Bitbucket access. Support for Personal Access Tokens (PATs) is planned.

#### Using OAuth

1. Go to **Settings > Runners** and select the runner for which you want to configure OAuth.
2. Navigate to the "Configure repository access" section and click "Add a new provider".
   <Frame caption="Add new provider">
     <img src="https://www.gitpod.io/images/docs/flex/source-control/scm-providers.png" />
   </Frame>
3. Select **Bitbucket** from the list of providers.
4. In the modal that opens, toggle "Enable OAuth".
   <Frame caption="Enable Bitbucket OAuth">
     <img src="https://www.gitpod.io/images/docs/flex/source-control/bitbucket-enable-oauth.png" />
   </Frame>
5. Follow the instructions in [Bitbucket's docs](https://support.atlassian.com/bitbucket-cloud/docs/use-oauth-on-bitbucket-cloud/) to create an OAuth app.
   * The app name can be any name you like
   * You can get the callback URL from the SCM configuration dialog
   * Select the required scopes
     * The *account* scope is required so that the git author name and git author email can be set in the environment
     * The *repository* scope is required so that the repository can be cloned and the context url can be parsed
     * The *repository:write* scope is required so that changes can be pushed to the repository from the environment
     * The *pullrequests* scope is required so that an environment can be started from a pull request
       <Frame caption="Configure Bitbucket OAuth">
         <img src="https://www.gitpod.io/images/docs/flex/source-control/bitbucket-configure-oauth.png" />
       </Frame>
6. After creating the OAuth app, provide the **Client ID** and **Client Secret** in the runner configuration dialog. Bitbucket calls these *Key* and *Secret*. The client secret will be encrypted with the runner's public key, ensuring only the runner can read it.
7. Save your changes

## Authorizing Bitbucket Access

### Using OAuth

1. When creating your first environment, you will be asked to authorize the new application. To use OAuth press the *Connect* button.

   <Frame caption="Connect Bitbucket OAuth">
     <img src="https://www.gitpod.io/images/docs/flex/source-control/bitbucket-connect-oauth.png" />
   </Frame>

   A new window will open that directs you to Bitbucket to authorize the OAuth app. The requested scopes are *account*, *repository*, *repository:write*, *pullrequests* and *issue*.

   * The *account* scope is required so that the git author name and git author email can be set in the environment
   * The *repository* scope is required so that the repository can be cloned and the context url can be parsed
   * The *repository:write* scope is required so that changes can be pushed to the repository from the environment
   * The *pullrequests* scope is required so that an environment can be started from a pull request

   <Frame caption="Authorize Bitbucket OAuth">
     <img src="https://www.gitpod.io/images/docs/flex/source-control/bitbucket-authorize-app.png" />
   </Frame>

2. After you have authorized Gitpod, you can close the window. After a few seconds the you should get a confirmation that Bitbucket is now connected.
   <Frame caption="Connect Bitbucket OAuth">
     <img src="https://www.gitpod.io/images/docs/flex/source-control/bitbucket-connected.png" />
   </Frame>
