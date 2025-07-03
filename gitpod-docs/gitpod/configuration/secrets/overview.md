# Overview

> Learn how to configure secrets in Gitpod

Secrets allow you to securely store and inject sensitive data into your environments. These include API keys, access tokens, credentials, and certificates that your applications need but shouldn't be exposed in your source code.

Secrets are configured for a project, or a user, and automatically made available to any environment launched from that project. This ensures consistent and secure access to sensitive data across your development workflow. Learn more about managing [project secrets](/flex/projects/project-secrets) or [user secrets](/flex/configuration/secrets/user-secrets).

## Encryption of Secrets

All secrets you create are protected with industry-standard encryption. Secrets can only be retrieved by environments created from your projects (for Project secrets) or your user (for User secrets).

We use `AES256-GCM` to encrypt all secrets at rest in the database, with an additional layer of protection through AWS RDS encryption. This dual-layer approach ensures your sensitive data remains secure both at the application level and infrastructure level. In transit, all secrets are encrypted using TLS.

**Gitpod employees do not have access to the encryption keys and cannot decrypt your secrets.**

## Types of Secrets

Gitpod supports multiple types of secrets to accommodate different needs:

* [Files](/flex/configuration/secrets/files): Securely store and inject entire files into your environment
* [Environment Variables](/flex/configuration/secrets/environment-variables): Key-value pairs injected into your environment's process space
* [Container Registry Secrets](/flex/configuration/secrets/container-registry-secret): Authentication credentials for private container registries

Each type of secret serves a specific purpose in your development workflow. Click the links above to learn more about how to use each type effectively.
