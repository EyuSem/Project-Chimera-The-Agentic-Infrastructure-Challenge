# Architecture Strategy – Project Chimera

## 1. Agent Pattern Selection

Chosen Pattern: Hierarchical Swarm (Planner–Worker–Judge)

Reasoning:
This pattern allows the system to scale horizontally while keeping
decision-making and safety centralized.

- Planners handle intent and coordination
- Workers execute isolated tasks in parallel
- Judges enforce quality, safety, and governance

This prevents cascading failures and allows safe autonomy.

---

## 2. Human-in-the-Loop (HITL) Placement

Human review is introduced only when required:

- Low confidence outputs
- Sensitive content domains
- Financial transactions exceeding limits

This follows a “management by exception” model, allowing autonomy
without sacrificing safety.

---

## 3. Data Storage Strategy

Different data types require different storage models:

- PostgreSQL:
  - Campaign state
  - Task metadata
  - Audit logs

- Weaviate (Vector Database):
  - Long-term semantic memory
  - Persona knowledge
  - Past interactions

- Redis:
  - Task queues
  - Short-term memory
  - Rate limiting and counters

---

## 4. MCP as a System Boundary

All external systems are accessed through MCP servers.

Benefits:
- API changes do not affect agent logic
- Security and rate limits are centralized
- Agent behavior remains predictable

Agents are never aware of platform-specific APIs.

---

## 5. Failure & Safety Model

Failure is expected and designed for:

- Worker failures do not affect other workers
- Judges prevent invalid or unsafe state commits
- Stale state is rejected using optimistic concurrency control

This ensures the system can recover without manual intervention.
