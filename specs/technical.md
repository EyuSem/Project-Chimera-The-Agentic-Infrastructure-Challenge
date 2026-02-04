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
