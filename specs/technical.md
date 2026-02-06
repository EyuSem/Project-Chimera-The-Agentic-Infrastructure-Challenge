# Technical Specification – Project Chimera

## Agent Task Contract

```json
{
  "task_id": "uuid",
  "task_type": "perceive | generate | engage | transact",
  "priority": "high | medium | low",
  "context": {
    "goal": "string",
    "persona_constraints": ["string"],
    "resources": ["mcp://resource/path"]
  },
  "state_version": "string",
  "status": "pending | in_progress | review | complete"
}

### Agent Task Schema
```json
{
  "task_id": "uuid-v4-string",
  "task_type": "generate_content | reply_comment | execute_transaction",
  "priority": "high | medium | low",
  "context": {
    "goal_description": "string",
    "persona_constraints": ["string"]
  },
  "status": "pending | in_progress | review | complete"
}

{
  "name": "post_content",
  "description": "Publishes text and media to a connected social platform.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "platform": {
        "type": "string",
        "enum": ["twitter", "instagram", "threads"]
      },
      "text_content": {
        "type": "string",
        "description": "The body of the post/tweet."
      },
      "media_urls": {
        "type": "array",
        "items": {"type": "string"}
      },
      "disclosure_level": {
        "type": "string",
        "enum": ["automated", "assisted", "none"]
      }
    },
    "required": ["platform", "text_content"]
  }
}