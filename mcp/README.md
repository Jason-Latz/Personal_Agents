# Model Context Protocol (MCP) Guide

This document provides a detailed, step-by-step walkthrough for building a simple MCP server and connecting to it with the `mcp_client` module in this repository.

## Prerequisites

- **Python 3.10+** and **pip**
- **Git** for source control
- (Optional) **Node.js 18+** if you plan to write a JavaScript client
- A terminal with standard POSIX utilities

---

## 1. Create an MCP server project

1. **Create a working folder** for your server:
   ```bash
   mkdir my_mcp_server && cd my_mcp_server
   ```
2. **Create and activate a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. **Upgrade pip** to ensure the latest tooling:
   ```bash
   pip install --upgrade pip
   ```

## 2. Install the MCP reference implementation

1. **Install the library** from PyPI:
   ```bash
   pip install mcp
   ```
2. **Verify the installation**:
   ```bash
   python -c "import mcp; print(mcp.__version__)"
   ```

## 3. Implement a minimal server

1. **Create `server.py`** with the following content:
   ```python
   from mcp.server import Server, run

   server = Server("example")

   @server.tool
   def say_hello(name: str) -> str:
       """Return a friendly greeting."""
       return f"Hello {name}!"

   if __name__ == "__main__":
       run(server)
   ```
2. The `Server` object collects tools and resources. The `@server.tool` decorator marks a function as callable by clients.
3. `run(server)` starts a stdio-based service that waits for client connections.

## 4. Launch the server

1. **Make the script executable** (optional on Windows):
   ```bash
   chmod +x server.py
   ```
2. **Start the server**:
   ```bash
   python server.py
   ```
   The process will block and wait for a client connection via stdin/stdout.

## 5. Connect with the provided client

1. **Open another terminal** in the repository root of this project (`Personal_Agents`).
2. **Set an environment variable** so the client knows how to spawn the server:
   ```bash
   export MCP_SERVER_CMD="python /absolute/path/to/my_mcp_server/server.py"
   ```
3. **Run the client**:
   ```bash
   python mcp_client/client.py
   ```
   The client launches the server using the command from `MCP_SERVER_CMD` and establishes the MCP handshake.

## 6. Call tools and list resources

1. **Invoke the `say_hello` tool** programmatically:
   ```python
   from mcp_client.client import MCPClient

   client = MCPClient()
   result = client.call_tool("say_hello", {"name": "World"})
   print(result)  # -> "Hello World!"
   ```
2. **List resources** the server exposes:
   ```python
   resources = client.list_resources()
   print(resources)
   ```

## 7. Shut down

1. **Exit the client** normally or with `Ctrl+C`.
2. **Terminate the server** process with `Ctrl+C` in its terminal.
3. **Deactivate the virtual environment**:
   ```bash
   deactivate
   ```

## Additional tips

- Add more tools by decorating additional functions with `@server.tool`.
- Resources can be exposed via `server.add_resource()` for files or data streams.
- For deployment, package your server into a standalone script and distribute it with instructions for clients to connect via the MCP protocol.
- Consult the official MCP specification for advanced features such as structured messaging and authentication.

