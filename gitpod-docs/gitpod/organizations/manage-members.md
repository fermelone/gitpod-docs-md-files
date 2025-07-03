# Manage members

As an admin of your organization, you can manage the organization's members. This includes:

* Changing a member's role.
* Removing members from the organization.
* Inviting teammates by generating invite links.

You can also view any user's environments by selecting 'View Environments' from the drop-down menu.

<Frame caption="Manager org members">
  <img src="https://www.gitpod.io/images/docs/flex/organizations/members-list-options.png" />
</Frame>

## User roles

Members of an organization can have of the following roles:

* Admin - an admin is a privilidged member who can manage other members, create remote Runners, view all resources and administer the organization.
* Member - a regular user who can only a use a Local Runner, or a Runner that's been shared with them by an Admin.

## Permissions table

The following table outlines the specific permissions for each role in Gitpod:

| Permission                              | Admin | Member               |
| --------------------------------------- | ----- | -------------------- |
| **Organization Management**             |       |                      |
| Create and manage organization          | ✅     | ❌                    |
| Invite members                          | ✅     | ❌                    |
| Manage member roles                     | ✅     | ❌                    |
| View all organization members           | ✅     | ✅                    |
| Configure organization policies         | ✅     | ❌                    |
| View organization audit logs            | ✅     | ❌                    |
| Configure SSO                           | ✅     | ❌                    |
| **User**                                |       |                      |
| Create Personal Access Token            | ✅     | ✅                    |
| **Projects**                            |       |                      |
| Create projects                         | ✅     | Depends on policy    |
| Share projects within organization      | ✅     | ❌                    |
| View and use existing projects          | ✅     | ✅                    |
| **Runners**                             |       |                      |
| Create remote runners                   | ✅     | ❌                    |
| Use remote runners                      | ✅     | When shared by admin |
| Use Gitpod Desktop (if enabled)         | ✅     | ✅                    |
| **Environments**                        |       |                      |
| Create environments from any repository | ✅     | Depends on policy    |
| View all organization environments      | ✅     | ❌                    |
| **Secrets**                             |       |                      |
| Manage project secrets                  | ✅     | ❌                    |
| Manage personal secrets                 | ✅     | ✅                    |

To change a user's role, select 'Change Role' from the drop-down menu. This will open a modal where you can update their role.

<Frame caption="Change role">
  <img src="https://www.gitpod.io/images/docs/flex/organizations/change-role.png" />
</Frame>

<Frame caption="Change member role">
  <img src="https://www.gitpod.io/images/docs/flex/organizations/change-member-role.png" />
</Frame>

## Create an invite link

Select the 'Invite Members' button at the top of the list to open the 'Invite Members' page, where you can copy the invite link to share with your team. If you need to deactivate a link, click 'Reset Invite Link' to invalidate any previously created links.

<Frame caption="Invite members">
  <img src="https://www.gitpod.io/images/docs/flex/organizations/invite-members.png" />
</Frame>
