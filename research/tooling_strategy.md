## MCP Configuration Depth

### Topology
- Hub-and-Spoke: Agent Runtime as MCP Host; connects to servers via Stdio/SSE.

### Key Servers (Dev & Runtime)
- Dev: git-mcp (for version control), filesystem-mcp (file editing).
- Runtime: mcp-server-twitter (post_tweet tool), mcp-server-weaviate (memory search), mcp-server-coinbase (wallet actions).

### Primitives
- Resources: Passive data (e.g., twitter://mentions/recent).
- Tools: Executable (e.g., generate_image() with JSON inputSchema).
- Prompts: Templates (e.g., analyze_sentiment).

### Example Config (JSON for .mcp.json)
```json
{
  "servers": {
    "github-mcp-server": {
      "type": "stdio",
      "command": "docker run -i --rm -e GITHUB_TOKEN=${env:token} ghcr.io/github/github-mcp-server:0.30.2"
    }
  }
}