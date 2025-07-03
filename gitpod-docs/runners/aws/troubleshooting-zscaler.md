# Zscaler Compatibility Issues

> Troubleshoot common issues when using Gitpod with Zscaler security solutions

Organizations using Zscaler as their security gateway may encounter various compatibility issues with Gitpod services. This guide helps identify and resolve the most common problems.

## Common Issues

### HTTP/2 Protocol Downgrade

**Symptoms:**

* Gitpod CLI requests fail unexpectedly
* Connection timeouts or protocol errors
* Performance degradation in web requests

**Root Cause:**
Zscaler downgrades HTTP/2 connections to HTTP/1.1 by default for encrypted traffic that undergoes SSL inspection, which can cause compatibility issues with Gitpod services that rely on HTTP/2.

**Solutions:**

1. **Enable HTTP/2 for SSL-Inspected Traffic (Recommended)**
   * Contact your Zscaler administrator
   * Request enabling HTTP/2 support for encrypted traffic subject to SSL inspection
   * This setting is under `Administration > Advanced Settings`
   * Enable the toggle for HTTP/2 support for SSL-inspected requests
   * For more information see [Zscaler's documentation](https://www.zscaler.com/de/blogs/product-insights/http-2-better-faster-stronger)

### SSL Certificate Verification Failures

**Symptoms:**

* VS Code extension fails to connect to Gitpod environments
* Certificate verification errors in application logs
* TLS handshake failures with "certificate verify failed" messages
* Applications showing "untrusted certificate" warnings

**Root Cause:**
Zscaler performs SSL inspection by intercepting HTTPS traffic and presenting its own certificates instead of the original server certificates. Applications using custom certificate stores (like VS Code) may not trust these Zscaler-generated certificates.

**Important Note:** Gitpod does not implement certificate pinning, so SSL inspection should work once the Zscaler certificates are properly trusted by the system.

**Identifying SSL Inspection:**
Run this command to check if Zscaler is intercepting certificates:

```bash
curl -I -vv https://app.gitpod.io
```

**With Zscaler SSL Inspection:**

```
* Server certificate:
*  subject: CN=app.gitpod.io; O=Zscaler Inc.; OU=Zscaler Inc.
*  start date: Mar 17 13:23:09 2025 GMT
*  expire date: Mar 30 03:38:20 2025 GMT
*  issuer: C=US; ST=California; O=Zscaler Inc.; OU=Zscaler Inc.; CN=Zscaler Intermediate Root CA (zscalerthree.net) (t)
```

**Without SSL Inspection:**

```
* Server certificate:
*  subject: CN=app.gitpod.io
*  start date: Aug 7 00:00:00 2024 GMT
*  expire date: Sep 5 23:59:59 2025 GMT
*  issuer: C=US; O=Amazon; CN=Amazon RSA 2048 M03
```

**Solutions:**

1. **Disable SSL Inspection for Gitpod (Recommended)**
   * Contact your network security team
   * Request adding `app.gitpod.io` to the SSL inspection exemption list
   * This ensures applications receive authentic Gitpod certificates

2. **Configure VS Code to Use System Certificates**

   * **Requirements:** VS Code 1.97 or later
   * **Steps:**
     1. Open VS Code
     2. Go to `File > Preferences > Settings`
     3. Search for "System certificates" and ensure it's enabled (default)
     4. Search for "Fetch Additional Support" and ensure it's enabled (default)
     5. Restart VS Code and test connection

   **If issues persist, try these additional settings:**

   * Enable "Electron Fetch" setting
   * Enable "System Certificates V2" setting
   * Restart VS Code after each change

### Runner Connection Issues

**Symptoms:**

* Gitpod runners cannot connect to the gateway
* Runner status not properly reported in dashboard
* OAuth authentication failures with external services (GitLab, GitHub)
* "Connection refused" or timeout errors in runner logs

**Root Cause:**
Zscaler may block or interfere with specific IP ranges and protocols that Gitpod services need, particularly:

* Static IP addresses for Lighthouse connectivity
* OAuth callback URLs and authentication flows
* Runner-to-gateway communication protocols

**Solutions:**

1. **Whitelist Gitpod IP Ranges**
   * Contact your network team to whitelist Gitpod's static IP addresses
   * This is particularly important for Lighthouse connectivity
   * See [Network Connectivity Requirements](/flex/runners/aws/aws-infrastructure-prerequisites#network-connectivity-requirements) for the current IP ranges

2. **Temporary Workaround: Use Personal Access Tokens**
   * While IP whitelisting is being configured, use Personal Access Tokens (PATs) instead of OAuth
   * This bypasses some authentication flows that may be blocked

## Configuration Checklist

Work with your network and security teams to implement these Zscaler configurations:

#### Phase 1: SSL Inspection Exemptions

* [ ] Add `app.gitpod.io` to SSL inspection bypass list
* [ ] Test certificate verification with `curl -I -v https://app.gitpod.io`
* [ ] Verify certificate issuer shows Amazon RSA (not Zscaler)

### HTTP/2 Protocol Support

* [ ] Raise provisioning ticket with Zscaler support to enable HTTP/2 backend configuration
* [ ] Enable HTTP/2 in SSL inspection policy pages
* [ ] Enable HTTP/2 for encrypted traffic subject to SSL inspection in Advanced Settings

### Network Access

* [ ] Whitelist Gitpod static IP ranges for runner connectivity
* [ ] Ensure WebSocket connections are allowed
* [ ] Verify GRPC traffic is not blocked

## Testing Your Configuration

After implementing the above changes:

1. **Test Certificate Trust**
   ```bash
   curl -I -v https://app.gitpod.io
   ```
   Verify the certificate issuer shows Amazon RSA (authentic) rather than Zscaler

2. **Test Gateway Certificate (for AWS runners)**
   ```bash
   curl -I -v https://us01.gitpod.dev
   ```
   You can also verify the gateway certificate using [SSL Labs](https://www.ssllabs.com/ssltest/analyze.html?d=us01.gitpod.dev\&s=52.22.228.114\&hideResults=on)

3. **Test Protocol Support**
   ```bash
   curl --http2 -I https://app.gitpod.io
   ```
   Verify HTTP/2 protocol is maintained

4. **Test Gitpod Services**
   * Try connecting with VS Code extension
   * Test Gitpod CLI commands
   * Verify runner connectivity if applicable

## Getting Help

If issues persist after implementing these solutions:

1. Collect diagnostic information:
   * Output from `curl -I -vv https://app.gitpod.io`
   * VS Code and Gitpod extension logs
   * Network configuration details
