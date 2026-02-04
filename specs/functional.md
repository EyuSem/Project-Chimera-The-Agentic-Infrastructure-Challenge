# Functional Specification – Project Chimera

## Agent Roles

### Planner Agent
Responsible for:
- Interpreting high-level campaign goals
- Decomposing goals into executable tasks
- Re-planning when context or state changes

### Worker Agent
Responsible for:
- Executing a single atomic task
- Using MCP Tools to interact with external systems
- Producing artifacts for review

### Judge Agent
Responsible for:
- Validating outputs against persona, safety, and quality constraints
- Assigning confidence scores
- Escalating to Human-in-the-Loop when required

---

## Core Functional Requirements

### Trend Perception
As an Agent,
I need to ingest trend and event data through MCP Resources
So that content generation is contextually relevant and timely.

---

### Content Generation
As an Agent,
I need to generate text, image, or video assets
So that I can publish content autonomously.

---

### Social Engagement
As an Agent,
I need to respond to mentions and comments
So that engagement remains active.

---

### Financial Actions
As an Agent,
I need to execute on-chain transactions
So that I can operate as an economic actor.
