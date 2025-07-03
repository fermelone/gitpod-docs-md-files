# Browser Extension

The browser extension adds a Gitpod button to GitHub, GitLab, Bitbucket and Azure DevOps repository interfaces, whether managed or self-hosted to allow you to quickly create environments.

<Frame caption="The Gitpod button on a GitHub repository, created by the browser extension">
  <img src="https://www.gitpod.io/images/docs/browser-extension-repo.png" />
</Frame>

**Caption:** The Gitpod button shown on a GitHub repository, created by the browser
extension

<br />

The extension is available for the following browsers:

1. [Chrome](https://chromewebstore.google.com/detail/gitpod/dodmmooeoklaejobgleioelladacbeki) (including Edge, Brave and other Chromium-based browsers)
2. [Firefox](https://addons.mozilla.org/firefox/addon/gitpod/)

## Access the extension settings

You can access the extension settings by clicking on the Gitpod icon in the browser toolbar. In the resulting popup you can find a comprehensive view of all possible customization.

<img className="shadow-medium w-full rounded-xl max-w-3xl mt-x-small" alt="Gitpod browser extension configuration in Google Chrome" src="https://www.gitpod.io/images/docs/browser-extension-settings.webp" />

## Enabling the browser extension on self-hosted SCM providers (e.g. GitLab CE/EE and Bitbucket Datacenter)

By default, the browser extension automatically is automatically enabled for the domains of GitHub (`github.com`), GitLab (`gitlab.com`) and Bitbucket (`bitbucket.org`) and Azure DevOps (`dev.azure.com`). If the `run on all sites` option is disabled, all other domains must be configured manually.

To add a custom SCM domain, open the Gitpod extension's context menu. Opening the context menu can be achieved by either right clicking the extension icon in the browser toolbar or revealing it by clicking on a kebab menu \[Chrome] / cog wheel \[Firefox] in the extensions dropdown.

| Chrome                                                                                                              | Firefox                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| ![Screenshot of the context menu in Chrome](https://www.gitpod.io/images/docs/browser-extension/chrome-context.png) | ![Screenshot of the context menu in Firefox](https://www.gitpod.io/images/docs/browser-extension/firefox-context.png) |

## Use a custom Gitpod instance URL

If you are using a custom Gitpod instance (e.g., [Gitpod Enterprise](https://www.gitpod.io/contact/enterprise-self-serve)) you can still use the browser extension by configuring it with your instance URL.

After you've installed the extension, open its options (see chapter [Access the extension settings](#access-the-extension-settings)) and enter your custom Gitpod instance URL. Then, simply click "Save" and approve the browser's request for new permissions.

## Source Code

Gitpod's browser extension is open source, meaning that you can check out its [source code](https://github.com/gitpod-io/browser-extension).
