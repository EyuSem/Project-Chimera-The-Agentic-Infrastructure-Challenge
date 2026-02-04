# Chimera Skills

A Skill is a reusable runtime capability used by Chimera agents.

Skills are:
- Called by Worker agents
- Independent of MCP servers
- Designed to be testable and replaceable

## Skill Structure

Each skill MUST define:
- Input schema
- Output schema
- Expected failure modes

## Initial Skills

### trend_fetcher
Fetches trend data from MCP Resources and normalizes it.

### content_generator
Transforms structured intent into publishable content.

### engagement_responder
Generates safe, context-aware replies to user engagement.
