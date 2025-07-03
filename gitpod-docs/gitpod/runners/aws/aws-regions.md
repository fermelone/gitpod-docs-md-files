# Regions and Latency

For the best user experience, users need low network latency between their dev environment and their local machine.
Many operations in the IDE or terminal require network packets to be sent between the local machine and dev environment.
High network latency can make the IDE and terminal feel sluggish.

Follow these steps to optimize your setup:

1. Identify regions offering the best latency for your users
2. Verify these regions are among the supported regions
3. Contact Gitpod support if you need support for additional regions

# Predicting Network Latency

Before deploying Gitpod Runners, you can measure network latency using these tools:

## Latency Testing Tools

* Third-party websites (search for "aws latency test"):
  * [CloudPing](https://www.cloudping.cloud/aws)
  * [AWS Latency Test](https://aws-latency-test.com/)
  * [AWS Speed Test](https://awsspeedtest.com/latency)

* Command-line tools:
  * `ping` command (requires ICMP support)
  * [httping](https://www.vanheusden.com/httping/) (for HTTP/HTTPS-only networks)

## Important Considerations

* Test results reflect latency from *your* location to AWS regions. If users are in different locations, have them run the same tests.
* Gitpod is designed to work with multipe regions by installing a runner in each region.
* VPN usage affects test results. Configure your connection to match your planned Gitpod usage:
  * Use VPN if you plan to connect to Gitpod through VPN
  * Disable VPN if you plan to connect directly

# Measuring Network Latency

After deploying Gitpod Runners, you can monitor latency using:

* JetBrains IDE: Check the "backend status" view when connected to a remote dev environment

# Recommended Latency Thresholds

| Latency  | Experience | Recommendation                                            |
| -------- | ---------- | --------------------------------------------------------- |
| \< 70ms  | Excellent! | Ideal for all development tasks                           |
| \< 120ms | Good       | Suitable for most development work                        |
| \< 200ms | Ok         | Users may notice some latency in IDE and terminal         |
| > 200ms  | Poor       | Not recommended. Users will experience significant delays |

# Supported AWS Regions

Gitpod AWS Runners are available in select regions across North America, Europe, Asia Pacific, and South America.

### North America

* `us-east-1` (N. Virginia)
* `us-east-2` (Ohio)
* `us-west-1` (N. California)
* `us-west-2` (Oregon)
* `ca-central-1` (Canada Central)

### Europe

* `eu-west-1` (Ireland)
* `eu-central-1` (Frankfurt)
* `il-central-1` (Israel Central)

### Asia Pacific

* `ap-southeast-1` (Singapore)
* `ap-southeast-2` (Sydney)
* `ap-northeast-1` (Tokyo)

### South America

* `sa-east-1` (São Paulo)

Need support for additional regions? Please [contact Gitpod](https://www.gitpod.io/contact/sales) for assistance.
