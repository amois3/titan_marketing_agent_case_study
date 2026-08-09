# Agent design

TITAN Marketing Agent is not a generic content generator. Its working unit is a falsifiable hypothesis: a claim about an audience, channel, message or timing paired with an outcome that can be observed.

The agent can propose and prepare work; product policy decides whether it may execute it. A measured result feeds the next allocation decision through a deterministic reward, not through self-assessment by the same model that produced the work.

Lifecycle transitions — approve, reject, mark-posted, retry — are business rules, not interface code. Centralizing them guarantees that the CLI, the dashboard, and any future entry point apply the same guardrails and produce the same audit record.

The private product has richer planning, content and channel adapters. The public core keeps the contract small enough to audit: facts arrive as events, a decision is attributable to inputs, and irreversible action is gated.
