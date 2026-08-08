# TITAN Marketing Agent

## Autonomous growth experimentation engine

> Public case study. The original product remains private. This repository documents the architecture, operational boundaries, and verification model without publishing implementation code, credentials, channel accounts, or proprietary data.

TITAN Marketing Agent is not a content generator with a scheduler attached. It is a controlled experimentation loop:

hypothesis -> experiment -> measured outcome -> deterministic reward -> durable insight -> better next experiment

The system is designed for the part that makes autonomous marketing difficult in practice: selecting what to test, measuring what happened, learning without inventing metrics, protecting a product voice, and keeping external actions under explicit control.

## What it does

- Generates structured growth hypotheses and candidate content.
- Selects channel/category arms with Thompson sampling rather than a fixed posting calendar.
- Tracks clicks, conversions, and platform engagement.
- Computes rewards deterministically from measured events - never from a language model's interpretation.
- Stores insights and experiment evidence for the next planning cycle.
- Supports explicit autonomy modes per channel: full automation, approval-required, or suggest-only.
- Keeps the orchestration restart-safe with durable state transitions.

## The operating model

### 1. Hypotheses are testable objects

A candidate starts as a falsifiable proposition: audience, channel, message angle, expected signal, and a defined observation window. The system does not treat a post as success merely because it exists.

### 2. Planning is exploration with accountability

A Thompson-sampling planner selects among experiment arms using observed outcomes and uncertainty. This balances exploitation of proven directions with exploration of under-sampled ones.

### 3. Attribution produces the reward

Reward inputs come from tracked clicks, conversion events, and supported platform signals. The reward function is deterministic and inspectable, which prevents a model from declaring an experiment successful because the copy sounds persuasive.

The reporting CLI supports a minimum-conversion threshold for arms. It explicitly reports how many arms were filtered rather than quietly changing the comparison set.

### 4. Voice is a quality boundary

Voice is not delegated to a single prompt. The system works from approved examples, generates multiple candidates where useful, runs a critic pass, applies deterministic banned-phrase checks, and carries learned taste notes forward. Content can still be held for review before publication.

### 5. External actions remain governed

Each channel can be configured independently:

| Mode | Behaviour |
|---|---|
| Full automation | The system may publish within its configured policy. |
| Approval required | It produces a ready candidate and waits for a human decision. |
| Suggest only | It produces recommendations but never publishes. |

A capability being implemented is not treated as live automation. In the current product configuration, X is the live automated channel; other channel integrations remain intentionally disabled until explicitly enabled.

## Reliability and safety decisions

- Database-backed experiment state prevents a restart from losing the lifecycle of an active test.
- Transactions and idempotent transitions protect state from partial completion.
- Pydantic schemas constrain structured tool inputs and outputs.
- Metrics are calculated from events, not free-form model prose.
- Publishing authority is separate from generation capability.
- Approval state is explicit and auditable.
- The system reports missing or insufficient data instead of fabricating a conclusion.

## Verification

The private source includes CLI and helper tests for reporting, planning, rewards, and state handling. A recent delivery added:

- `ga report --min-conversions-per-arm`, defaulting to `0`;
- explicit reporting of arms filtered by that threshold;
- tests for the CLI option and filtering helper;
- README documentation;
- published laptop commit `4e6e934`.

This case study intentionally does not publish source code. The evidence to evaluate is the system design, its deterministic boundaries, its documented operating model, and the reproducible claims above.

## Why this architecture matters

Marketing automation gets risky when it behaves confidently but cannot say what it measured, why it selected an action, or whether a person approved it. TITAN Marketing Agent makes those questions first-class product constraints.

The goal is not more output. It is a marketing system that can test, learn, and operate without becoming unaccountable.

## Scope and disclosure

- This is an independent product in the TITAN family, not a component of TITAN Agent or TITAN Code.
- The public repository is documentation only; the original source remains private.
- No client data, channel credentials, private prompts, or implementation code are included.

---

Built by [Aleksejs Moisejevs](https://github.com/amois3) · AI Systems Architect & Agentic Product Builder
