## Security Specifications

### Authentication & Authorization
- Multi-tenancy: JWT-based auth via MCP (e.g., mcp-server-auth). Operators get roles (admin, reviewer).
- API: All endpoints require bearer tokens; rate limiting via MCP layer.

### Data Protection
- Wallets: Non-custodial keys stored in encrypted secrets (e.g., AWS Secrets Manager or .env with Vault). Never log/expose.
- Memories: Weaviate/PostgreSQL with row-level security; encrypt PII (e.g., user interactions).

### Compliance & Safety
- EU AI Act: Agents self-disclose as AI in posts (SRS NFR 2.0).
- Anomaly Detection: CFO Judge for transactions (SRS FR 5.2); escalate suspicious patterns.
- Vulnerabilities: CI scans with Trivy or Dependabot; .coderabbit.yaml already checks.

### Risks & Mitigations
- Runaway costs: Resource Governor with budget thresholds.
- Race conditions: OCC in Judge (SRS FR 6.1).