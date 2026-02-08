# Frontend Specifications

## Overview
The frontend is a React-based dashboard for Network Operators and HITL Reviewers, ensuring multi-tenancy and real-time monitoring. It consumes backend APIs via MCP (e.g., for fleet status).

## Components
- **Fleet Status View**: Real-time table showing agent states, wallet balances, queue depths (SRS UI 1.0). Use WebSockets for updates.
- **Campaign Composer**: Form for natural language goals (SRS UI 1.1). Decomposes via Planner API.
- **HITL Review Queue**: Cards for escalated tasks (SRS NFR 1.1-1.2). Includes Approve/Reject buttons with API calls.

## Tech Stack
- Framework: React with Tailwind CSS.
- State: Redux or Context API.
- API Integration: MCP Client for resources/tools (e.g., fetch global state).

## Wireframes (Mermaid Flow)
```mermaid
graph TD
    A[Login] --> B[Dashboard]
    B --> C[Fleet View]
    B --> D[Campaign Composer]
    B --> E[Review Queue]
    E --> F[Approve/Reject Action]