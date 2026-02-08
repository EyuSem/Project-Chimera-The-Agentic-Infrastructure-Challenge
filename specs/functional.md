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

## User Stories with Acceptance Criteria

- As an Autonomous Agent, I need to fetch trends via MCP Resources so I can create relevant content.
  - AC1: Input: niche (str), location (str optional). Output: list of topics with sources (JSON array).
  - AC2: Handles API timeouts with retry (up to 3x).
  - AC3: Relevance score > 0.75 triggers Planner task (SRS FR 2.1).

- As an Agent, I need to generate images consistent with my persona so followers recognize me.
  - AC1: Input: prompt (str), character_reference_id (str). Output: image_url (str).
  - AC2: Judge validates consistency via Vision LLM (e.g., "YES/NO match" > 90% confidence).
  - AC3: Escalates low-confidence to HITL (SRS NFR 1.0).

- As a Planner, I need to decompose goals into tasks for Workers.
  - AC1: Input: goal (str). Output: DAG of tasks (JSON graph).
  - AC2: Reactive re-planning on state changes (SRS 3.1.1).
  - AC3: Integrates with TaskQueue (Redis).
