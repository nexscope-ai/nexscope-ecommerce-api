# Installing the Nexscope MCP server in Cline

Nexscope is a hosted (remote) MCP server. There is nothing to clone, build or run locally.

1. Open Cline > MCP Servers > Remote Servers (or edit `cline_mcp_settings.json`).
2. Add:

```json
{
  "mcpServers": {
    "nexscope": {
      "type": "streamableHttp",
      "url": "https://api.nexscope.ai/mcp"
    }
  }
}
```

3. On first use, complete the OAuth sign-in in the browser window that opens (a free trial account works).
   Alternatively, create an API key in your Nexscope account and add it as a header:

```json
{
  "mcpServers": {
    "nexscope": {
      "type": "streamableHttp",
      "url": "https://api.nexscope.ai/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
      }
    }
  }
}
```

4. Test: ask "Which Nexscope tools can you use?"

Full client configuration, tool discovery and request shapes: [Nexscope MCP documentation](https://www.nexscope.ai/mcp-docs?co-from=cline).
