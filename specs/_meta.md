# Project Chimera – Meta Specification

## Vision
Project Chimera is an autonomous influencer infrastructure designed to
create, operate, and govern AI-driven digital personas with minimal
human intervention.

Unlike traditional automation tools, Chimera agents are:
- Persistent
- Goal-driven
- Capable of perception, reasoning, and action
- Governed through explicit architectural constraints

## Scope
This repository defines the agent factory, not a single influencer.
Its purpose is to provide specifications, governance, and infrastructure
that allow AI agents to safely build and operate autonomous influencers.

## Non-Goals
The following are explicitly out of scope:
- Prompt-only chatbot systems
- Manual content scheduling tools
- One-off influencer demos
- Direct API integrations without MCP

## Core Architectural Constraints
- All external interactions MUST occur via Model Context Protocol (MCP)
- Agent execution MUST follow the Planner–Worker–Judge pattern
- Human intervention occurs only by exception (HITL)
- Specifications are the source of truth, not implementation code

## Success Criteria
The system is considered successful if:
- Agents can be developed without modifying core infrastructure
- Failures are isolated and recoverable
- Unsafe or low-confidence outputs are escalated automatically
