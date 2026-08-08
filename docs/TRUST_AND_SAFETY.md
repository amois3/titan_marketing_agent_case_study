# Trust and safety

The automation boundary is intentionally narrower than the reasoning boundary. An experiment may recommend an action; it does not thereby acquire permission to publish, spend money, or alter a connected account.

## What is enforced here

`AutonomyMode` is executable policy. `approval` requires an explicit approval signal. `suggest_only` always denies publication. This is not dependent on an instruction interpreted by a model.

## What production adds

The private product also has connected-account credentials, channel-specific configuration, durable transaction state, idempotency records, review flows and operational monitoring. Those components are not reproduced here and this repository cannot grant external authority.

## Investigating an incident

Record the event IDs, arm counters, reward formula version, selection seed, selected arm and approval decision. Those are the minimum inputs required to reproduce the decision rather than merely explain it after the fact.
