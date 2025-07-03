# Overview

Runners are single-tenant, self-hosted, flexible orchestrators of remote development environments. They are self-hosted in order to compartmentalize any sensitive information related to your development environments. Runners are responsible for operational tasks like

* Scaling
* Backup
* Caching

To reduce operational overhead, runners offload all non-sensitive administration responsibilities to the management plane.

Gitpod offers two types of self-hosted runners:

1. **AWS Runner**: Deploy on AWS using a CloudFormation template, ideal for production use and larger teams. It provides:

   * Horizontal scaling capabilities
   * Full AWS infrastructure integration
   * Dev container image build caching for faster environment startup
   * Pay-per-use cost model
   * Deployment in any region or availability zone, in any AWS Account
   * Runners can be deployed into multiple different AWS Accounts

2. **Linux Runner**: Run directly on your Linux machine, perfect for evaluation and small teams. It offers:
   * Simple local setup
   * Fixed infrastructure costs
   * Direct local network access
   * Support for up to 10 concurrent environments

Organizations can have as many runners as needed, deploying them in different locations to support remote teams in different timezones, adhere to data sovereignty, and other compliance requirements.

To create or modify runners, you must have an admin role inside the Gitpod organization.

Once deployed, you don’t need to interact with the infrastructure directly. Through Gitpod Desktop you can configure:

* which repositories a runner can access
* what environment classes are supported
* share it with your organization to allow any member to use it when creating environments
