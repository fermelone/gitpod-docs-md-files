# PingFederate

You can set up Single Sign-on (SSO) with PingFederate for your team.

This section helps you to create an OIDC application with PingFederate. The *Client ID*, *Client Secret*, and *Issuer URL* of this OIDC application are required to setup SSO in Gitpod. See the [Step-by-step guide](/flex/sso#step-by-step-guide-to-set-up-sso) for the general instructions.

## Prerequisites

As prerequisites you will need the following:

* Access to your PingFederate instance
* Administrator permissions on PingFederate to create and configure OAuth clients
* Understanding of your organization's authentication flow requirements

## Create an OAuth Client

The OAuth client allows you to integrate with Gitpod using the OpenID Connect protocol.

Please refer to the [official PingFederate documentation](https://docs.pingidentity.com/pingfederate/12.2/administrators_reference_guide/pf_configuring_oauth_clients.html) for detailed configuration steps.

1. Log in to your PingFederate Administrative Console.

2. Navigate to **Applications > OAuth > Clients**.

3. Click **Add Client** to create a new OAuth client.

4. Configure the OAuth client with the following settings:

   * **Client ID**: Generate or specify a unique identifier (you'll need this for Gitpod)
   * **Client Authentication**: Select `Client Secret`
   * **Client Secret**: Generate a secure secret (you'll need this for Gitpod)
   * **Allowed Grant Types**: Select `Authorization Code`
   * **Redirect URIs**: `https://app.gitpod.io/auth/oidc/callback`
   * **Allowed Scopes**: Include at minimum:
     * `openid`
     * `profile`
     * `email`

5. **Configure Token Settings**:
   * Set appropriate token lifetimes based on your security policies
   * Ensure ID tokens include necessary claims (`sub`, `email`, `name`)

6. **Save the Configuration** and note down:
   * **Client ID**: The unique identifier you specified
   * **Client Secret**: The generated secret
   * **Issuer URL**: Your PingFederate base URL (e.g., `https://your-pingfederate.company.com`)

## Additional Configuration

Depending on your PingFederate setup, you may need to:

* Configure attribute mapping to ensure user information (email, name) is properly passed to Gitpod
* Set up any required authentication policies or adapters
* Configure session management settings
* Review and adjust any security policies that might affect the integration

## Troubleshooting

Common issues and solutions:

* **Invalid Redirect URI**: Ensure the redirect URI in PingFederate exactly matches `https://app.gitpod.io/auth/oidc/callback`
* **Missing Claims**: Verify that your PingFederate configuration includes the required OpenID Connect claims (`sub`, `email`, `profile`)
* **Authentication Failures**: Check PingFederate logs for detailed error information

For detailed configuration instructions and troubleshooting, refer to the [PingFederate OAuth Configuration Guide](https://docs.pingidentity.com/pingfederate/12.2/administrators_reference_guide/pf_troubleshooting.html).

## Continue with Gitpod Configuration

Once you have obtained the *Client ID*, *Client Secret*, and *Issuer URL* from your PingFederate configuration, continue with [Step 1. Configure SSO](/flex/sso#step-1-configure-sso) in Gitpod.
