# Google

You can set up Single Sign-on (SSO) with Google for your team.

This section helps you to create an OIDC application with Google. The *Client ID*, *Client Secret*, and *Issuer URL* of this OIDC application are required to setup SSO in Gitpod. See the [Step-by-step guide](/flex/sso#step-by-step-guide-to-set-up-sso) for the general instructions.

## Prerequisites

As prerequisites you will need the following:

* Access to setup a new [API Credentials](https://console.cloud.google.com/apis/credentials) in your GCP Account

## Create an OAuth/OIDC application

The OAuth/OIDC application allows you to integrate with Gitpod.

1. Navigate to your *Google Cloud Console > API Credentials*

2. Select *Create Credentials*, and choose *OAuth Client ID*

   <Frame caption="Create credentials - Google Cloud Dashboard">
     <img src="https://www.gitpod.io/images/docs/gitpod-dedicated/guides/getting-started/sso/google/create-credentials.webp" />
   </Frame>

3. Configure your *OAuth Client ID* by specifying the *Authorized Redirect URI*: `https://app.gitpod.io/auth/oidc/callback`

4. Obtain the *Client ID* & *Client Secret* and input these into your Gitpod Setup page

   <Frame caption="OAuth Client Created - Google Cloud Dashboard">
     <img src="https://www.gitpod.io/images/docs/gitpod-dedicated/guides/getting-started/sso/google/OAuth-client-created.webp" />
   </Frame>

5. Use Google's global *Issuer URL*: `https://accounts.google.com`

6. Continue with the SSO configuration in Gitpod: [Clicking *Save & Test*](/flex/sso#3-save-and-test-the-configuration)
