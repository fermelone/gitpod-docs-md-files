# Manage organization

If you are an admin of the current organization, you can modify the general settings. This includes:

* Changing the display name of your organization.
* Adjusting the email domains of users who can discover and join your organization.

In the Danger Zone, you have the option to delete the organization.

<Frame caption="Delete organization">
  <img src="https://www.gitpod.io/images/docs/flex/organizations/delete-organization.png" />
</Frame>

## Allowed email domains

You can allow others to join your organization if their email address matches one of the allowed email domains in organization settings. Gitpod enforces a validation rule that only permits email domains provided by the identity provider (IdP) during sign-in. This means you can't add domains to the list unless they are used by members of your organization.

<Frame caption="Type the email domain and confirm by pressing the Enter key.">
  <img src="https://www.gitpod.io/images/docs/flex/organizations/allowed-email-domains.png" />
</Frame>

<br />

<Frame caption="Now the input field changed to a tag.">
  <img src="https://www.gitpod.io/images/docs/flex/organizations/selected-email-domains.png" />
</Frame>

<br />

<Frame caption="Select Update to validate and update the email domains. Here it is rejected because no existing user shares this email domain.">
  <img src="https://www.gitpod.io/images/docs/flex/organizations/failed-email-domain-update.png" />
</Frame>
