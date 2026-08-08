# Design decisions

## Reward business evidence, not model self-assessment

Model-generated assessments are useful as hypotheses, not as a reward signal. The core scores measurable events with a small, inspectable formula. Product teams may change the formula, but that change should be versioned and reviewed like any other business rule.

## Make retries idempotent

Event delivery is not exactly-once in the real world. Deduplication is performed before counters change, making a replay visible and harmless rather than quietly inflating performance.

## Treat low-sample filtering as a disclosure requirement

A conversion threshold can be useful for decision quality, but it changes the reported population. The command therefore keeps the default at zero and emits the number of filtered arms every time.

## Preserve an investigation path

Thompson sampling is stochastic. The random generator is injected rather than hidden so a decision can be reproduced with the recorded seed and inputs.
