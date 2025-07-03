# GitHub

Source control integrations can be configured for both [Self-Hosted Runners](/flex/runners) and [Gitpod Desktop](/flex/gitpod-desktop). You can set up a GitHub integration during runner creation or in the runner settings. Self-hosted GitHub instances are supported by changing the Host during setup.

## Configuring GitHub Access

<Note>
  {' '}

  You can skip this step if someone has already set up the runner for you and SCM
  integration with GitHub has already been configured. In that case, you can go
  directly to [Authorizing GitHub Access](#authorizing-github-access). This step
  allows administrators to configure what authorization methods (OAuth, PATs) and
  SCM providers (GitHub, GitLab, Bitbucket, Azure DevOps) will be available for
  authorization.
</Note>

### Self-Hosted Runners

For self-hosted runners (like AWS), GitHub integration is configured during runner creation or in the runner settings.

There are two ways to integrate with GitHub. Both can be used simultaneously:

1. **OAuth App (Recommended):** Using an OAuth app allows users to sign in more quickly. You'll need to set up an OAuth app within Gitpod.
2. **Personal Access Token (PAT):** Each user will need to create a Personal Access Token. They will be provided with a deep link to do so on their first environment creation.

#### Using OAuth

1. Go to **Settings > Runners** and select the runner for which you want to configure OAuth.
2. Navigate to the "Configure repository access" section and click "Add a new provider".
   <Frame caption="Add new provider">
     <img src="https://www.gitpod.io/images/docs/flex/source-control/scm-providers.png" />
   </Frame>
3. Select **GitHub** from the list of providers.
4. In the modal that opens, toggle "Enable OAuth".
   <Frame caption="Enable GitHub OAuth">
     <img src="https://www.gitpod.io/images/docs/flex/source-control/github-enable-oauth.png" />
   </Frame>
5. Follow the instructions in [GitHub's docs](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app) to create an OAuth app.
   * The app name can be any name you like
   * For the homepage URL, you can use [https://app.gitpod.io/](https://app.gitpod.io/)
   * You can get the callback URL from the SCM configuration dialog
6. After creating the OAuth app, provide the **Client ID** and **Client Secret** in the runner configuration dialog. The client secret will be encrypted with the runner's public key, ensuring only the runner can read it.
7. Save your changes

#### Using Personal Access Tokens (PATs)

1. Go to **Settings > Runners** and select the runner for which you want to configure the PAT.
2. Navigate to the "Configure repository access" section and click "Add a new provider".
   <Frame caption="Add new provider">
     <img src="https://www.gitpod.io/images/docs/flex/source-control/scm-providers.png" />
   </Frame>
3. Select **GitHub** from the list of providers.
4. In the modal that opens, toggle "Enable Personal Access Token".
   <Frame caption="Enable GitHub PAT">
     <img src="https://www.gitpod.io/images/docs/flex/source-control/github-enable-pat.png" />
   </Frame>
5. Save your changes

### Gitpod Desktop

For Gitpod Desktop, GitHub authentication is managed through organization settings:

1. Organization administrators configure GitHub access in Settings -> Runners -> Gitpod Desktop
2. `github.com` is configured by default
3. For self-hosted GitHub instances:
   * Administrators must add the custom host in the settings
   * Users cannot authenticate with these hosts until they are configured
4. Users authenticate using **Personal Access Tokens**:
   * Gitpod checks for existing Git credentials first on the user's machine (using the git credential manager)
   * If none exist, users are prompted to provide a PAT during environment creation
   * Tokens can be managed under Settings -> Git Authentications

<Frame caption="Desktop Settings">
  <img src="https://www.gitpod.io/images/docs/flex/desktop/desktop_settings.png" />
</Frame>

## Authorizing GitHub Access

### Using OAuth

1. When creating your first environment, you will be asked to authorize the new application. A new window will open that directs you to GitHub to authorize the OAuth app.

* The requested scopes are *repo*, *read:user*, *user:email*, and *workflow*.
* The *repo* permission is required so that your environment can clone the repository.
* The *read:user* permission is required so that the git author name can be set in the environment.
* The *user:email* permission is required so that the git author email can be set in the environment.
* The *workflow* permission is required so that GitHub Action YAML files can be edited in the environment.

2. After you have authorized Gitpod, you can close the window and go back to the environment details screen.

### Using Personal Access Tokens (PATs)

1. The first time a user creates an environment, they will be asked to enter a Personal Access Token.

   * Click the link provided on the screen to access the configuration dialog for creating a GitHub token.
   * The name of the token and all required scopes are pre-set.
   * By default, the token is valid for 30 days, but you can change the duration if needed.
     <Frame caption="Set GitHub PAT">
       <img src="https://www.gitpod.io/images/docs/flex/source-control/github-set-pat.png" />
     </Frame>

2. After creating the token, return to the dialog and paste the token.

3. The environment will now be created using the provided token.
