# Microsoft Entra ID

You can set up Single Sign-on (SSO) with Microsoft Entra ID for your team.

This section helps you to create an OIDC application with Microsoft Entra ID. The *Client ID*, *Client Secret*, and *Issuer URL* of this OIDC application are required to setup SSO in Gitpod. See the [Step-by-step guide](/flex/sso#step-by-step-guide-to-set-up-sso) for the general instructions.

## Prerequisites

As prerequisites you will need the following:

* Access to [Microsoft Entra admin center](https://entra.microsoft.com/)

## Create an OIDC application

1. On the [Microsoft Entra admin center](https://entra.microsoft.com/), navigate to *Identity > Applications*

2. Select `New Registration`

   <Frame caption="New Registration">
     <img src="https://www.gitpod.io/images/docs/flex/organizations/sso/entra-1-new-app.png" />
   </Frame>

3. Specify General Settings

   * App name, e.g. `Gitpod`

   * Platform: `Web`

   * Redirect URI: `https://app.gitpod.io/auth/oidc/callback`

   * <Frame caption="Register Application">
       <img src="https://www.gitpod.io/images/docs/flex/organizations/sso/entra-2-register-app.png" />
     </Frame>

4. Obtain *Client Secret* from the *Certificates & secrets* page

   * Once the application is registered, navigate to the subpage *Certificates & secrets* to create and obtain a new client secret.

     * Click the *New client secret* button
       <Frame caption="New client secret">
         <img src="https://www.gitpod.io/images/docs/flex/organizations/sso/entra-3-client-secret.png" />
       </Frame>

     * Adjust the expiry of the client secret
       <Frame caption="Client secret expiry">
         <img src="https://www.gitpod.io/images/docs/flex/organizations/sso/entra-4-client-secret-expires.png" />
       </Frame>

     * Then copy the value of the client secret to be pasted in Gitpod's SSO setup
       <Frame caption="Client secret expiry">
         <img src="https://www.gitpod.io/images/docs/flex/organizations/sso/entra-5-client-secret-copy.png" />
       </Frame>

5. Configure OIDC Scopes

   * The default selection of OIDC scopes in Microsoft Entra ID doesn't meet the requirements for Gitpod. Please navigate to *API permissions > Add a permission* to make the necessary changes.

     <Frame caption="Add a permission">
       <img src="https://www.gitpod.io/images/docs/flex/organizations/sso/entra-7-permissions-openid.png" />
     </Frame>

     * Select *Delegated permissions* and *OpenId*, then ensure to enable the following scopes:

       * `email`

       * `openid`

       * `profile`

       * <Frame caption="OpenID Scopes">
           <img src="https://www.gitpod.io/images/docs/flex/organizations/sso/entra-6-permissions.png" />
         </Frame>

   * Although the `email` claim is part of the standard OIDC specification, depending on the setup, Microsoft Entra ID does not include it by default in ID tokens. Under *Manage*, select *Token configuration* and fix this:

     * Click *Add optional claim*

     * Add the `email` scope

     * <Frame caption="Add email scope">
         <img src="https://www.gitpod.io/images/docs/flex/organizations/sso/entra-10-id-email-claim.png" />
       </Frame>

6. Obtain *Issuer URL* from *Endpoints* tab

   * Navigate to the *Overview* page and select *Endpoints*

     <Frame caption="Endpoints tag">
       <img src="https://www.gitpod.io/images/docs/flex/organizations/sso/entra-8-endpoints-tab.png" />
     </Frame>

   * Copy the *Authority URL* to be used as *Issuer URL* in Gitpod's SSO setup

     <Frame caption="Endpoints tag">
       <img src="https://www.gitpod.io/images/docs/flex/organizations/sso/entra-8-endpoints-tab-issuer.png" />
     </Frame>

     > **Note**: Validate the **Issuer URL** by checking the [OIDC Discovery](https://learn.microsoft.com/en-us/entra/identity-platform/v2-protocols-oidc#find-your-apps-openid-configuration-document-uri) location. In some configurations, the **Issuer URL** needs to be adjusted.

     * If the *Authority URL* reads like `https://login.microsoftonline.com/{tenant}/v2.0`, the OIDC Discovery location is `https://login.microsoftonline.com/{tenant}/v2.0/.well-known/openid-configuration`. Open this URL in your browser and check the `issuer` field.

     * Check the `issuer` field in the OIDC Discovery output and ensure this matches the *Authority URL* (*Issuer URL*).
       If not, e.g. if it reads like `https://sts.windows.net/{tenant}`, please try again with`{authority_url}/v2.0/.well-known/openid-configuration` and use `{authority_url}/v2.0` as **Issuer URL** in Gitpod's SSO setup.

7. Obtain the *Client ID* from the *Overview* page

   * Navigate to the *Overview* page and copy the *Application (client) ID* value to be used as *Client ID* in Gitpod's SSO setup

     <Frame caption="Client ID">
       <img src="https://www.gitpod.io/images/docs/flex/organizations/sso/entra-9-client-id.png" />
     </Frame>

8. Continue with the SSO configuration in Gitpod: [Clicking *Save & Test*](/flex/sso#3-save-and-test-the-configuration)
