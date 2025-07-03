# Examples

Gitpod enables a wide range of use cases for automated and secure development environments. Here are some ways you can leverage Gitpod, with concrete examples and explanations of how Automations support each use case:

## Automate Environment Setup

Gitpod allows you to fully automate the setup and configuration of development environments.

### One-click onboarding

New developers can start coding immediately without manual setup.

Example: An automation task clones multiple repositories, installs project-specific dependencies, and configures environment variables.

```yaml
tasks:
    build:
        name: Build Code
        command: yarn && yarn build
    test:
        name: Run unit tests
        dependsOn: ['build']
        command: yarn test
    setup:
        name: Set up the environment
        dependsOn: ['build', 'test']
        command: echo "all set up and ready to go"
```

### Database provisioning

Automatically create and seed databases for development.

Example: A service spins up a PostgreSQL database and runs migration scripts.

```yaml
tasks:
    seedDatabase:
        name: (Re)seed the development database
        triggeredBy: ['manual']
        command: dev/seed-development-db.sh
services:
    postgresql:
        name: PostgreSQL
        description: A fully initialized development database
        triggeredBy: ['postDevcontainerStart']
        commands:
            start: docker run -d --name postgres -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 postgres:latest
            # Note: there is no support yet for task to service dependencies.
            ready: docker exec postgres pg_isready -U postgres && gitpod auto task start seedDatabase
```

### Cloud authentication

Securely authenticate to cloud services.

Example: A task uses Gitpod's built-in identity provider to authenticate with AWS.

```yaml
tasks:
    awsAuth:
        name: AWS Auth
        command: gitpod idp login aws
```

These Automations ensure consistent environments and dramatically reduce time spent on setup and configuration.

## Flexible Editing Interfaces

Launch the right editing interface for each project:

### Jupyter for data science

Example: Start a Jupyter Notebook server with required Python packages.

```yaml
services:
    jupyter:
        name: Jupyter Notebook
        command: |
            pip install jupyter pandas numpy matplotlib &&
            jupyter notebook --ip=0.0.0.0
```

### Storybook for UI development

Example: Automatically start Storybook server for component development.

```yaml
services:
    storybook:
        name: Storybook
        commands:
            start: yarn storybook
            ready: curl http://localhost:5173 -s -f -o /dev/null
```

## Self-Serve Testing Environments

Empower QA and testing with on-demand environments:

### Preview environments

Automatically create environments for pull requests.

Example: A service that builds and deploys the application to a preview URL.

```yaml
services:
    preview:
        triggeredBy: postDevcontainerStart
        commands:
            start: |
                npm install
                npm run build
                npx serve -p 3000 ./build
            ready: curl http://localhost:3000 -s -f -o /dev/null && gitpod ports open 3000 --name "Application Preview"
```

### Parallel testing

Run tests across multiple configurations simultaneously.

Example: Services that spin up different database versions for compatibility testing.

```yaml
services:
    pg12:
        name: Postgres 12
        commands:
            start: docker run -d --name pg12 -p 5432:5432 postgres:12
    pg13:
        name: Postgres 13
        commands:
            start: docker run -d --name pg13 -p 5433:5432 postgres:13
tasks:
    test:
        name: Run Tests
        command: |
            npm run test:pg12
            npm run test:pg13
```

These Automations allow testers to quickly access and verify changes in isolated environments.

## Operational Runbooks

Automate operational tasks and provide secure access:

### Troubleshooting environments

Pre-configured environments with necessary tools and access.

Example: A task that installs monitoring tools and sets up VPN access.

```yaml
tasks:
    troubleshoot:
        name: Setup Troubleshooting Env
        triggeredBy: ['manual']
        command: |
            sudo apt-get update && sudo apt-get install -y htop iftop
            ./setup_vpn.sh
```

### Verify log rates

Use a project which creates environments on a runner located so that AWS access is possible.

Example: A task that logs into AWS and verifies log error rates

```yaml
tasks:
    awsSetup:
        name: Setup AWS credentials
        commands: gitpod idp login aws --role arn::some:role
    troubleshoot:
        name: Setup Troubleshooting Env
        triggeredBy: ['postEnvironmentStart']
        dependsOn: ['awsSetup']
        command: |
            aws logs filter-log-events --log-group-name /aws/lambda/my-function --start-time $(date -u -d '1 hour ago' +%s000) --filter-pattern "ERROR"
```

These configurations ensure that operational tasks are performed consistently and securely.

These Automations enhance developer productivity and maintain security standards across all environments.

By centralizing and automating environment configuration, Gitpod enables you to standardize workflows, improve security, and unlock new possibilities across your development lifecycle. The combination of tasks and services allows for complex, multi-step Automations that can be easily shared and version-controlled alongside your codebase.
