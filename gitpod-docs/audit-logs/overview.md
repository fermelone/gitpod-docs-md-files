# Audit Logs

Audit logs provide a record of all actions taken in a Gitpod organization. Using the audit logs, you can track who performed an operation, on which resource, and when. Gitpod produces audit logs for all operations within an organization.

## Accessing Audit Logs

Audit logs are accessible to users with the **Organization Owner** role. You can retrieve audit logs using the **Gitpod CLI** or the **Gitpod API**.

### Using the CLI

You can view audit logs using the `gitpod` CLI, which is pre-installed on all Gitpod environments.

```bash
gitpod audit-logs [--limit=number_of_entries]
```

For additional options, including filtering and output formatting (JSON or YAML), run:

```bash
gitpod audit-logs --help
```

#### Example Output

```bash
➜ gitpod audit-logs

SUBJECT ID                           SUBJECT TYPE            ACTOR ID                             ACTOR PRINCIPAL       ACTION                       CREATED AT
01951d94-d6ac-7edf-9021-a044cfd1908f RESOURCE_TYPE_ENVIRONMENT 0193e2f2-d0b5-7d52-87eb-235deadaf625 PRINCIPAL_RUNNER changed update_time, status, phase, last_running_session 2025-02-21T12:10:05Z
0194f5dd-01ca-75f4-a200-74381ed43f86 RESOURCE_TYPE_ENVIRONMENT 0193e2f2-d0b5-7d52-87eb-235deadaf625 PRINCIPAL_RUNNER changed update_time, status, phase, last_running_session 2025-02-21T12:10:03Z
...
```

### Using the API

You can retrieve audit logs programmatically via the Gitpod API. For detailed documentation, refer to the [API Reference](https://www.gitpod.io/docs/api-reference/resources/events/methods/list/).

#### Example Request

```bash
curl https://app.gitpod.io/api/gitpod.v1.EventService/ListAuditLogs \
     -H 'Content-Type: application/json' \
     -H "Authorization: Bearer $GITPOD_API_KEY" \
     -d '{}'
```
