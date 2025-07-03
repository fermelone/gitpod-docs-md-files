# Overview

AWS Runners allow you to deploy Gitpod's runner infrastructure directly within your own AWS VPC, giving you complete control over your development environments while maintaining security and compliance requirements.

When you deploy an AWS Runner, development environments are created as EC2 instances that are automatically sized based on your environment class requirements. The runner orchestrator itself runs as an ECS service within a dedicated ECS cluster in your AWS account. The entire deployment is automated through CloudFormation templates that we provide, making setup straightforward while ensuring best practices for security and scalability.

<Frame caption="Overview of Gitpod AWS runner architecture">
  <img src="https://www.gitpod.io/images/docs/flex/runners/flex-architecture.png" />
</Frame>

## Choose Your AWS Runner

Gitpod offers two AWS runner variants to meet different security and feature requirements. For information on runners generally, see [Self-Hosted Runners](/flex/runners).

<CardGroup cols={2}>
  <Card title="Standard Runner" icon="desktop" href="/gitpod/runners/aws/standard-runner/overview">
    **Quick & Easy**: 30-minute setup with CloudFormation template. Secure connectivity through Gitpod's central gateway eliminates complex networking configuration.
  </Card>

  <Card title="Enterprise Runner" icon="shield" href="/gitpod/runners/aws/enterprise-runner/overview">
    **Advanced Features**: AI agent integration, direct connectivity with your own domain/certificates, and enhanced security controls. Enterprise tier only.
  </Card>
</CardGroup>
