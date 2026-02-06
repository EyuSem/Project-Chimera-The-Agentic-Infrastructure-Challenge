# Project Chimera – Agentic Infrastructure Challenge
```markdown
[![CI](https://github.com/EyuSem/Project-Chimera-The-Agentic-Infrastructure-Challenge/actions/workflows/main.yml/badge.svg)](https://github.com/EyuSem/Project-Chimera-The-Agentic-Infrastructure-Challenge/actions/workflows/main.yml)

## Overview
This repository is a **spec-driven foundation** for Project Chimera,
an autonomous influencer infrastructure built using agentic design,
Model Context Protocol (MCP), and swarm orchestration.

The goal of this project is **not** to deliver a finished influencer,
but to build a **governed factory** where AI agents can safely and
reliably build autonomous influencers in the future.

---

## Core Principles
- Spec-Driven Development (Specs before code)
- Planner–Worker–Judge agent pattern
- Human-in-the-Loop by exception
- MCP for all external interactions
- Test-first governance

---

## Repository Structure

specs/ # Source of truth (what the system must do)
research/ # Architectural reasoning and decisions
skills/ # Agent capabilities (interfaces only)
tests/ # Failing tests defining expected behavior
.github/ # CI/CD pipelines
Dockerfile # Reproducible environment
Makefile # Standardized commands


---

## Architecture Summary
Project Chimera follows a **Hierarchical Swarm Architecture**:

- **Planner**: Interprets goals and creates tasks
- **Worker**: Executes atomic tasks using MCP tools
- **Judge**: Validates outputs, assigns confidence, escalates if needed

Safety, scalability, and cost control are enforced through:
- Confidence scoring
- Human-in-the-Loop review
- Optimistic Concurrency Control
- Budget governance for agentic commerce

---

## Development Workflow

### Run tests locally
```bash
pytest
