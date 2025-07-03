# Port sharing

Port sharing allows you to expose HTTP ports from your running Gitpod environment to the internet, enabling easy sharing and collaboration. This feature is available for cloud-hosted Gitpod environments not Gitpod Desktop environments.

## How it works

When you share a port, Gitpod creates a public URL with automatic TLS termination. This allows secure access to your application or service running inside the Gitpod environment.

### Limitations

* Only HTTP traffic is supported.
* Not available on Gitpod Desktop environments.
* Subject to Gitpod's fair use policies and bandwidth limits.

### Prerequisites

To ensure port sharing works correctly, services must:

* listen on `0.0.0.0` instead of `localhost` or `127.0.0.1`
* be exposed from the Dev Container on the virtual machine using [the host network stack](/flex/configuration/devcontainer/getting-started#host-network-stack).

For example, if you're running a Node.js server, make sure to bind it to `0.0.0.0` instead of `localhost`.

```javascript
const app = express();
app.listen(3000, '0.0.0.0', () => {
	console.log('Server is running on port 3000');
});
```

### Security considerations

While port sharing is convenient, it's important to be mindful of security:

* Only share ports when necessary and unshare them when you're done.
* Be cautious about sharing ports running sensitive services or containing confidential data.
* Remember that shared URLs are public and potentially accessible by anyone with the link.

## Sharing ports

There are two ways to share ports from your Gitpod environment:

### Using the UI

In the Gitpod UI, you'll see a section labeled "Public Ports" that allows you to manage port sharing for your environment.

To share a new port:

1. Click the "Open Port" button in the "Public Ports" section.
2. A dialog will appear titled "Open a public port".
3. Enter a name for the port (optional) and the port number you wish to share.
4. Click "Open Port" to confirm.

For ports that are already open:

They will be listed in the "Public Ports" section. Each open port will show its name (if given) and port number. A green indicator next to the port signifies it's currently active and accessible.

<Warning>
  {' '}

  **Security notice**: When you open a port, it will be available on the open internet.
  Be careful when sharing the URL.
</Warning>

This interface provides an easy way to manage which ports are exposed from your Gitpod environment, allowing you to quickly share access to services or applications you're running.

### Using the CLI

Gitpod provides a set of CLI commands to manage port sharing. These commands allow you to list, open, and close ports directly from your terminal.

#### Listing ports

To view all currently open ports:

```
gitpod environment port list
```

This command will display a list of all ports that are currently open and available for sharing.

#### Opening a Port

To open and share a new port:

```
gitpod environment port open 3000 --name my-app
```

#### Closing a Port

To close a previously opened port:

```
gitpod environment port close <port-number>
```

For example, to close port 3000:

```
gitpod environment port close 3000
```

#### Examples

1. Open a port for a web server:

   ```
   gitpod environment port open 8080 --name webserver
   ```

2. Open a port for an API server:

   ```
   gitpod environment port open 4000 --name api
   ```

3. List all open ports:

   ```
   gitpod environment port list
   ```

4. Close a port that's no longer needed:
   ```
   gitpod environment port close 4000
   ```

These CLI commands provide a quick and efficient way to manage port sharing directly from your terminal, especially useful for scripting or when you prefer command-line interactions.

## Use cases

Port sharing enables various scenarios that enhance development workflows and collaboration:

1. Demonstrating work-in-progress: Quickly share your application with teammates or clients without deploying to a staging environment.

2. API testing: Expose your local API server to test integrations with external services or mobile apps.

3. Collaborative debugging: Share a running application with a colleague to troubleshoot issues together in real-time.

4. Design reviews: Make your local development server accessible so designers can review and provide feedback on UI changes.

5. Webhooks development: Test webhook integrations by exposing your local server to receive real-time events from external services.
