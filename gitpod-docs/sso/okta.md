# Okta

You can set up Single Sign-on (SSO) with Okta for your team.

This section helps you to create an OIDC application with Okta. The *Client ID*, *Client Secret*, and *Issuer URL* of this OIDC application are required to setup SSO in Gitpod. See the [Step-by-step guide](/flex/sso#step-by-step-guide-to-set-up-sso) for the general instructions.

## Prerequisites

As prerequisites you will need the following:

* Access to your Okta instance
* Permission to create an [app integration](https://help.okta.com/oie/en-us/Content/Topics/Apps/apps-overview-get-started.htm)

## Create an OIDC application

1. On the Okta Admin dashboard, navigate to Applications

2. Select `Create App Integration`

   <Frame caption="Applications - Okta Dashboard">
     <img src="https://www.gitpod.io/images/docs/gitpod-dedicated/guides/getting-started/sso/okta/okta-dashboard.webp" />
   </Frame>

3. Select the following options and click *Next*

   * Sign-in method: `OIDC - Open ID Connect`
   * Application type: `Web Application`

   <Frame caption="Create App Integration - Okta Dashboard">
     <img src="https://www.gitpod.io/images/docs/gitpod-dedicated/guides/getting-started/sso/okta/create-app-integration.webp" />
   </Frame>

4. Specify General Settings

   * App integration name, e.g. `Gitpod`
   * Sign-in redirect URIs: `https://app.gitpod.io/auth/oidc/callback`
   * Sign-out redirect URIs: `none`

   <Frame caption="Specify Okta settings - Okta Dashboard">
     <img src="https://www.gitpod.io/images/docs/flex/organizations/sso/okta-general.png" />
   </Frame>

5. Assignments

   * You have to select Okta users or groups which would be allowed to use the integration with Gitpod.
   * Okta let's you [import and synchronize directories](https://help.okta.com/oie/en-us/content/topics/directory/directory-integrations-main.htm?cshid=csh-directory-integrations-main), which then can be assigned to use the integration.

   <Frame caption="Specify Assignments - Okta Dashboard">
     <img src="https://www.gitpod.io/images/docs/flex/organizations/sso/okta-assignments.png" />
   </Frame>

6. Obtain *Client ID*, *Client Secret* from General tab

   <Frame caption="Configure Client Secrets - Okta Dashboard">
     <img src="https://www.gitpod.io/images/docs/gitpod-dedicated/guides/getting-started/sso/okta/client-configs-okta.webp" />
   </Frame>

7. Obtain *Issuer URL*

   <Frame caption="Issuer - Okta Dashboard">
     <img src="https://www.gitpod.io/images/docs/flex/organizations/sso/okta-copy-issuer-url.png" />
   </Frame>

8. Continue with the SSO configuration in Gitpod: [Clicking *Save & Test*](/flex/sso#3-save-and-test-the-configuration)
