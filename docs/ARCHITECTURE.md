# Architecture

The product boundary is a deterministic control plane around an otherwise flexible experimentation workflow.

```
hypothesis -> experiment -> lifecycle state machine -> arm -> attributable events
                                                      -> idempotent aggregation
                                                      -> deterministic reward -> allocation decision
                                                      -> autonomy policy -> external action
```

An *arm* is a selectable variant such as a channel, audience segment, creative strategy, or category. The public core uses impressions, clicks and conversions as explicit inputs. It does not infer success from model confidence or free-form text.

`aggregate()` is intentionally the first stateful boundary: it accepts an event only once per ID. `reward()` is then a transparent function of the resulting counters. `choose_arm()` represents Thompson sampling with a caller-provided random generator. In a real run, the seed and chosen arm belong in the audit trail.

The command-line report is part of the architecture, not just presentation. Operators need to see when an evidence threshold hides arms; otherwise an apparently clean report can be misleading.

In the full product, the lifecycle state machine is centralized: transitions such as approve, reject, mark-posted and retry are implemented once and invoked by every interface (CLI, dashboard, and any future channel). Keeping the rule in one place prevents the same defect from being fixed repeatedly across independent copies of the logic.
