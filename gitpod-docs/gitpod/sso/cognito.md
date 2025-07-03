# Amazon Cognito

You can set up Single Sign-on (SSO) with Amazon Cognito for your team.

This section helps you to create an OIDC application with Amazon Cognito. The *Client ID*, *Client Secret*, and *Issuer URL* of this OIDC application are required to setup SSO in Gitpod. See the [Step-by-step guide](/flex/sso#step-by-step-guide-to-set-up-sso) for the general instructions.

## Prerequisites

As prerequisites you will need the following:

* Access to set up a new [Amazon Cognito application](https://console.aws.amazon.com/cognito/home) in your AWS account.

## Create an OIDC application

1. Nagivate to [Amazon Cognito](https://console.aws.amazon.com/cognito/home) service page, then select `Set up your application`.

2. Configure the application by filling out the form:

   * **Application type**: `Traditional web application`

   * **Name**: `Gitpod`

   * **Options for sign-in identifiers**:

     * `Email`

   * **Required attributes for sign-up**:

     * `email`

     * `name`

   * **Return URL**: `https://app.gitpod.io/auth/oidc/callback`

   Click the *Create* button

   <Frame caption="Amazon Cognito - New Application">
     <img src="https://www.gitpod.io/images/docs/flex/organizations/sso/cognito-application.png" />
   </Frame>

3. Obtain *Client ID*, *Client Secret* from the Overview page<br /><br />

   Upon creation of the application, you will be redirected to then also created user pool. Learn more on user pools in Amazon Cognito [here](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools.html?icmpid=docs_cognito_console_help_panel).

   * Feel free to rename the user pool before proceeding!

   * Obtain **Issuer URL**

     * You'll find the **User pool ID** here

     * The pattern for the *Issuer URL* is:<br />
       `https://cognito-idp.<awsregion>.amazonaws.com/<user-pool-id>`

     * Verify to use the correct URL by opening the OIDC Discovery location `<Issuer URL>/.well-known/openid-configuration` in your browser, i.e. open `https://cognito-idp.<awsregion>.amazonaws.com/<user-pool-id>/.well-known/openid-configuration`.

   * Then navigate to *Applications > App clients > Gitpod* to find the details of the newly create application, and copy the information you'll need in Gitpod:

     * **Client ID**

     * **Client secret**

   <Frame caption="Amazon Cognito - Overview">
     <img src="https://www.gitpod.io/images/docs/flex/organizations/sso/cognito-overview.png" />
   </Frame>

4. Configure OIDC Scopes<br /><br />

   The default selection of OIDC scopes in Amazon Cognito doesn't meet the requirements for Gitpod. Please navigate to *App client > Login pages > Edit* to make the necessary changes.

   <Frame caption="Amazon Cognito - Edit Scopes">
     <img src="https://www.gitpod.io/images/docs/flex/organizations/sso/cognito-edit-scopes.png" />
   </Frame>

   * Ensure the `Profile` scope is selected here:

   <Frame caption="Amazon Cognito - Scopes">
     <img src="https://www.gitpod.io/images/docs/flex/organizations/sso/cognito-scopes.png" />
   </Frame>

5. Adjust **Sign-up** settings to your needs

   * Disable **Self-registration** if you want to limit access to your application.

   * With the Sign-up disabled , you may need to manage users under *User management* manually.

   <Frame caption="Amazon Cognito - Sign-up">
     <img src="https://www.gitpod.io/images/docs/flex/organizations/sso/cognito-signup.png" />
   </Frame>

6. Continue with the SSO configuration in Gitpod: [Clicking *Save & Test*](/flex/sso#3-save-and-test-the-configuration)
