# Migrate from Gitpod Classic to Gitpod

Gitpod uses [Dev Containers](/flex/configuration/devcontainer) and [Automations](/flex/configuration/automations) as its core configuration elements. Migration involves converting your `.gitpod.yml` into a `devcontainer.json` and `automations.yml` setup.

## Migrate the configuration

Create a new Gitpod environment for your existing repository and run the migration command:

```sh
gitpod env migrate
```

This command generates two key files:

* `.devcontainer/devcontainer.json`: Defines your development environment by setting the workspace folder, image, user, and other settings, aligned with Gitpod Classic experience.
* `.gitpod/automations.yml`: Contains tasks extracted from `.gitpod.yml`, maintaining their dependency order.

## Test the configuration

1. Deploy the `automations.yml` file using the following command:

   ```sh
   gitpod automations update .gitpod/automations.yml
   ```

2. Use the following command to rebuild your workspace with the new devcontainer.json:

   ```sh
   gitpod environment devcontainer rebuild
   ```

3. The default workspace folder in Dev Container differs from Gitpod Classic (`/workspaces` vs `/workspace`). VS Code may not open the correct folder automatically after rebuilding. To fix this:

   * Use the "Open File" option in VS Code to select the `/workspace/<project>` folder.

## Customize the configuration

While `gitpod env migrate` creates these baseline files, you need to make manual adjustments to match your requirements.
Note, for instance, that the default Dev Container image differs from the Gitpod Classic workspace image. You'll need to create a custom image for a more optimized environment.

Refer to the following resources to learn more about the configuration options:

* [Dev Containers](/flex/configuration/devcontainer)
* [Automations](/flex/configuration/automations)
