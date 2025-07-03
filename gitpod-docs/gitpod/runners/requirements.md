# Requirements

# Gitpod Requirements

This page outlines the essential requirements for using Gitpod, with special attention to network configurations that ensure optimal performance.

Here's what you need to get started with Gitpod, including important network settings for the best experience.

## Network Requirements

When accessing Gitpod (`app.gitpod.io`) using a browser, certain network configurations are essential, particularly in enterprise environments:

* **HTTP/2 Support**: The Gitpod Dashboard requires HTTP/2 protocol support throughout your network infrastructure.
  * **Important**: If your corporate network includes proxy servers that don't support HTTP/2 traffic, the Gitpod Dashboard will not function correctly.
  * Ensure all proxy servers in your network path are configured to pass through HTTP/2 traffic without downgrading it.
