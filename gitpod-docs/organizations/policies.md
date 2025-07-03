# Organization Policies

> Control how Gitpod is used in your organization with powerful policy settings that help manage resources, control costs, and ensure consistency.

<Warning>
  Organization policies are only available on Core and Enterprise plans. Free tier organizations will not have access to these features.
</Warning>

## What are Organization Policies?

Organization policies give administrators control over how Gitpod is used within their organization. With these policies, you can:

* Set limits on resource usage to control costs
* Enforce consistent development environments
* Implement security restrictions
* Streamline the user experience for your team

This guide explains each available policy and how to use them effectively.

## Getting Started with Policies

### Where to Find Policies

1. Ensure you have selected your organization
2. Navigate to [Settings > Organization > Policies](https://app.gitpod.io/settings/policies)

<Frame caption="Organization Policies">
  <img src="https://www.gitpod.io/images/docs/flex/organizations/organization-policies.png" />
</Frame>

### Who Can Access Policies?

Only organization **administrators** can view and modify policies. Regular **members** do not have access to organization policies.

### How Policies Work

* Most policies apply to all organization members
* Changes take effect immediately for new actions
* Existing environments are not affected by policy changes
* Administrators can override certain policies (like environment creation restrictions)

## Available Policies

### Local Environments using Gitpod Desktop

Control whether team members can use the Gitpod Desktop application to create environments using local compute resources.

This policy helps you:

* Enforce the use of remote runners for all environments
* Ensure consistent computing resources across your team
* Maintain centralized control over environment creation

**Configuration**

1. Go to your [Organization Policies](https://app.gitpod.io/settings/policies) page
2. Toggle the switch next to `Allow local environments using Gitpod Desktop` option to enable or disable Gitpod Desktop usage for your organization

> **Note:** For more information about the Gitpod Desktop application and how it works, see the [Gitpod Desktop documentation](https://www.gitpod.io/docs/flex/gitpod-desktop/overview).

<Frame caption="Enable or disable local environments">
  <img src="https://www.gitpod.io/images/docs/flex/organizations/gitpod-desktop-toggle.png" />
</Frame>

**Effect on users**

* Desktop application environments are disabled by organization policy
* Local Desktop runners will not appear in the Environment class selection list
* Users attempting to create local environments will see a policy restriction message
* Existing environments will continue running to allow for clean commit and shutdown
* Administrators can monitor and manage any running local environments via [Settings > Environments](https://app.gitpod.io/settings/environments)

### Editor Restrictions

This policy lets you standardize which code editors your team can use, creating consistency across development environments, enforcing company standards, and simplifying onboarding with standardized tools. You can also set a default editor that will be pre-selected for all users.

**Configuration**

1. In your [Organization Policies](https://app.gitpod.io/settings/policies) page, click on `Manage Editors` button
2. Select the editors you want to allow from the list
3. Choose a default editor that will be pre-selected for users
4. Save your changes

> **Remember:** You must keep at least one editor selected.

<Frame caption="You can toggle the editors you want to limit your organization from using and choose an org default">
  <img src="https://www.gitpod.io/images/docs/flex/organizations/available-editors.png" />
</Frame>

**Effect on users**

* Users will only see the allowed editors in the editor selection dropdown
* The default editor you selected will be pre-selected automatically
* Attempts to use a non-allowed editor (for example: via CLI) will be met with an error indicating the reason

### Maximum Environment Timeout

Limit the auto-stop timeout options that users can select for their environments to prevent unnecessary resource usage and control computing costs.

**Configuration**

1. In your [Organization Policies](https://app.gitpod.io/settings/policies) page, click on dropdown under `Maximum timeout duration` option
2. Choose from the following available maximum values:
   * 30 minutes
   * 1 hour
   * 3 hours
   * 8 hours
   * No Max Timeout (all options available, including `Never` Timeout)

<Frame caption="You can choose what is the maximum timeout that is available to the users">
  <img src="https://www.gitpod.io/images/docs/flex/organizations/maximum-timeout-duration.png" />
</Frame>

**Effect on users**

* Users will only see timeout options up to the maximum allowed by your policy in the dropdown menu
  For example, if you select "3 hours" as the maximum timeout, users will only see these options when starting an environment:
  * 30 minutes
  * 1 hour
  * 3 hours
* If you select "No maximum," users will see all timeout options including "Never."

<Frame caption="The policy will limit what users see as available timeout options">
  <img src="https://www.gitpod.io/images/docs/flex/organizations/max-timeout-limited.png" />
</Frame>

### Environment Creation Restrictions

<Note>
  This is one of the policies that only affects organization members and not organization admins.
</Note>

This policy controls whether regular organization members can create environments directly from repository URLs or if they are restricted to only creating environments from pre-defined projects.

This policy ensures that regular members work only within approved projects that administrators have set up, maintaining organizational control over which repositories are used for development.

**Configuration**

1. Go to your [Organization Policies](https://app.gitpod.io/settings/policies) page
2. Check "Environments can only be created from projects" option under `Environment creation restrictions` to enable this restriction

<Frame caption="Environment creation restrictions">
  <img src="https://www.gitpod.io/images/docs/flex/organizations/members-require-project.png" />
</Frame>

**Effect on users**

* Organization Members:
  * Can only create environments within existing projects
  * Will see "Create Environment" button restricted to existing projects only
  * Cannot create new projects
  * Will receive a policy notification when attempting to use repository URLs directly

* Organization Administrators:
  * Can create environments from any source, including direct repository URLs
  * Have exclusive permission to create new projects
  * Retain full access to all environment creation features

### Port Sharing Restrictions

This policy controls whether organization members can share ports from their environments to make services publicly accessible on the internet. If enforced, this restriction prevents users from exposing any ports from their Gitpod environments.

This policy helps you:

* Maintain security by preventing unauthorized exposure of development services
* Ensure compliance with organizational security policies
* Prevent accidental exposure of sensitive applications or data
* Control network access patterns within your organization

**Configuration**

1. Go to your [Organization Policies](https://app.gitpod.io/settings/policies) page
2. Check "Disable port sharing" option under `Port sharing restrictions` to prevent users from sharing ports

<Frame caption="Port sharing restrictions">
  <img src="https://www.gitpod.io/images/docs/flex/organizations/port-sharing-restrictions.png" />
</Frame>

**Effect on users**

* Users will not be able to share ports using either the UI or CLI methods
* Attempts to use `gitpod environment port open` CLI commands will be blocked with a policy restriction message
* Users will not be able to use VS Code Browser
* Users will see a notification explaining that port sharing is disabled by organization policy

> **Note:** For more information about port sharing functionality, see the [Port sharing documentation](https://www.gitpod.io/docs/gitpod/integrations/ports#port-sharing).

### Maximum Concurrent and total environments a user can have

<Note>
  {' '}

  This policy only applies to remote environments. Local environments created with Gitpod Desktop are not affected by these limits and can still be created if local environments are enabled for your organization.
</Note>

This policy helps administrators manage resource usage and control costs by setting two important limits:

* **Maximum total environments per user**: Limits how many total environments (running or stopped) each user can have
* **Maximum running environments per user**: Limits how many environments each user can have running simultaneously

By setting reasonable limits, you can:

* Prevent resource overuse that might impact your organization's infrastructure
* Control cloud computing costs, especially with AWS EC2 runners
* Encourage users to clean up environments they're no longer using
* Ensure resources are distributed fairly across your team

**Configuration**

1. Go to your [Organization Policies](https://app.gitpod.io/settings/policies) page
2. Set appropriate values for both `Maximum concurrent environments` and `Maximum total environments`
   * Both values must be between 1 and 100
3. These are set to 10 and 50 respectively by default

<Frame caption="Restrict maximum environments a user can have running or in total">
  <img src="https://www.gitpod.io/images/docs/flex/organizations/max-environments-limit.png" />
</Frame>

**Effect on users**

* A notification will appear when they attempt to create a new remote environment beyond the limit
* The notification will explain the policy limit and suggest stopping unused environments
* **Local environments** created with Gitpod Desktop are **not affected by these limits** and can be created without restriction

<Warning>
  If you are using EC2 runners, note that undeleted environments (running or stopped) will incur usage costs as per AWS pricing.
</Warning>

<Frame caption="A warning received due to the policy enforcement">
  <img src="https://www.gitpod.io/images/docs/flex/organizations/max-environments-reached.png" />
</Frame>

### Default Environment Image

This setting controls the default devcontainer configuration that Gitpod automatically generates when users open repositories without existing devcontainer configurations, or when starting blank environments. Administrators can customize this organization-wide template to:

* Provide a standard starting point for new environments
* Replace Gitpod's system defaults with organization-specific standards
* Ensure consistency across your organization
* If your runner network limits public Internet access, you will be able to start configuring devcontainer with images available in your network

**Configuration:**

1. Go to your [Organization Policies](https://app.gitpod.io/settings/policies) page
2. Enter a valid container image reference under `Default environment image` option (for example: `mcr.microsoft.com/devcontainers/base:ubuntu-24.04`)

If no value is provided, the system default (`mcr.microsoft.com/devcontainers/base:ubuntu-24.04`) will be used.

> **Using private images?** Make sure to [set up proper access](/gitpod/configuration/devcontainer/getting-started#using-private-container-images) for your container registry.

<Frame caption="Set default devcontainer image">
  <img src="https://www.gitpod.io/images/docs/flex/organizations/default-image.png" />
</Frame>

**Effect on users**

* The configured image will be used automatically when repositories don't specify an image
* Users won't need to take any additional action

## Tracking Policy Changes

All policy changes are automatically recorded in your organization's audit logs. This gives you:

* A complete history of who changed which policies and when
* Records of any policy violation attempts
* Visibility into how policies are being enforced

To review policy-related activities, check your [organization's audit logs](/gitpod/audit-logs/overview).

## Best Practices for Managing Policies

### Start Gradually

* Begin with moderate limits and adjust based on actual usage
* Inform your team before implementing new restrictions
* Use [audit logs](/gitpod/audit-logs/overview) to see how policies affect workflow

### Optimize Resource Management

* Set limits appropriate for your team size and available resources
* Regularly review usage patterns and adjust as needed
* Consider creating a policy review schedule (quarterly or after significant team changes)

### Balance Security and Productivity

* Choose editor restrictions that align with security requirements without hampering productivity
* Consider limiting local desktop access only for highly sensitive projects
* Use project-based environment creation to maintain organization without excessive restrictions

## Common Questions

### What happens to existing environments when I change a policy?

Existing environments aren't affected by policy changes. The new rules only apply to new environments or actions.

### Will users lose work when hitting a policy limit?

No. When users reach a policy limit (like maximum concurrent environments), they'll see a message explaining the limit and suggesting actions they can take, such as stopping unused environments.

### Can I set different policies for different teams?

Currently, policies apply to the entire organization. Team-specific policies aren't available yet.

### Do administrators have to follow these policies too?

Some policies, like environment creation restrictions, don't apply to administrators. Others, like resource limits, apply to everyone.

### How can I make a temporary exception to a policy?

The policy system doesn't include built-in exceptions. To make a temporary exception, adjust the policy temporarily and then change it back when no longer needed.

### What happens if I downgrade from Pro/Enterprise to Free tier?

If you downgrade to the Free tier, your policy settings will be preserved but will become inactive and non-editable until you upgrade again.

### Can policies be enforced retroactively?

Most policies only affect new actions or environments. Existing environments will continue to operate under the settings they were created with.

## Getting Help

If you have questions about organization policies:

* Contact [Gitpod support](https://www.gitpod.io/contact-support)
* Enterprise customers: Reach out to your account representative
