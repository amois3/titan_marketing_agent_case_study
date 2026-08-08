# TITAN Marketing Agent — the deterministic experimentation core, isolated

[![CI](https://github.com/amois3/titan_marketing_agent_case_study/actions/workflows/ci.yml/badge.svg)](https://github.com/amois3/titan_marketing_agent_case_study/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)
![Runtime dependencies](https://img.shields.io/badge/runtime%20dependencies-0-2ea44f)
[![License](https://img.shields.io/badge/license-review--only-6f42c1)](LICENSE)

TITAN Marketing Agent is an autonomous growth-experimentation product: a hypothesis becomes an experiment, measured outcomes become a deterministic reward, and the result informs the next decision. The private product contains channel integrations, persistence, content workflows, and operational controls. This public repository is a runnable reference core that isolates the decision boundary rather than exposing that private system.

The important premise is deliberately modest: language models may help formulate work, but they do not grade their own commercial success. Rewards come from attributable events; retries do not double-count them; and a policy decides whether an action may leave the system.

```bash
python -m venv .venv && . .venv/bin/activate  # .venv\\Scripts\\activate on Windows
pip install -r requirements-dev.txt
python -m pytest -q                            # 8 tests, no account, network or API key
python -m agent.cli report --min-conversions-per-arm 1
```

## What is here

| Component | Responsibility | Test focus |
| --- | --- | --- |
| `agent/` | Event aggregation, deterministic rewards, Thompson sampling, reporting and autonomy policy | duplicate delivery, filtering, repeatability, approval gates |
| `tests/` | Executable product invariants | failures that would otherwise distort decisions quietly |
| `docs/` | Architecture, decisions and autonomy boundary | why the boundary exists |

## The failures this core refuses to hide

**An event can be delivered twice.** A network retry must not turn one conversion into two. `aggregate()` deduplicates by event ID before it mutates an arm.

**A reporting threshold can silently change the picture.** `ga report --min-conversions-per-arm` defaults to `0`, filters only when explicitly asked, and always reports how many arms were removed by the threshold.

**An agent can be given more autonomy than the channel deserves.** `full`, `approval`, and `suggest_only` are product policy, not a prompt. An approval-mode action cannot publish without an approval signal; suggest-only never publishes.

## How the decision loop works

1. Capture attributable impressions, clicks and conversions as events.
2. Deduplicate events, calculate transparent statistics, and derive a deterministic reward.
3. Use a Beta posterior to sample a candidate arm. The caller owns the random seed, so a decision can be reproduced during investigation.
4. Report the evidence and pass the action through the autonomy policy before any external side effect.

The production system adds durable database transactions and idempotency records around this boundary. This compact core makes the contract readable without publishing credentials, private prompts, channel accounts, content, or the original product source.

## System context

The larger private product supports hypothesis-led experiments, Thompson-sampling allocation, deterministic rewards, attribution reporting, an approval matrix, structured tool boundaries, and restart-safe execution. Its documented `ga report` delivery includes `--min-conversions-per-arm`, tests for the CLI option and filtering helper, and an explicit count of filtered arms.

## Documentation

- [Architecture](docs/ARCHITECTURE.md)
- [Design decisions](docs/DECISIONS.md)
- [Trust and safety](docs/TRUST_AND_SAFETY.md)
- [Agent design](docs/AGENT_DESIGN.md)

## Scope and license

This is a public technical case study and reference core, not a distribution of the private TITAN Marketing Agent product. It is published for review and discussion only; see [LICENSE](LICENSE).

