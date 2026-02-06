# Project Chimera IDE Agent Rules

**Project Context**:  
This is Project Chimera: an autonomous AI influencer system built on MCP (Model Context Protocol), FastRender Swarm (Planner-Worker-Judge), and Agentic Commerce. The goal is a robust factory for AI agents to extend reliably.

**Prime Directive**:  
- NEVER generate or suggest implementation code without first reading and referencing all relevant files in specs/.  
- Always explain your reasoning and plan step-by-step, citing specific spec sections (e.g., "Per specs/technical.md API contract...").  
- Prioritize spec alignment, traceability, and failing tests.  
- If asked to code, respond: "First, confirm the relevant spec is ratified."  
- Maintain Git hygiene: suggest clear commit messages referencing specs/tests.

**Additional Guidelines**:  
- Distinguish dev tools (MCP for coding) vs. runtime skills (in skills/).  
- Favor TDD: reference failing tests in tests/.  
- Enforce governance: remind about Docker/CI/Make.