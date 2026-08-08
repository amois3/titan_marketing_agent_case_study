from collections.abc import Iterable

from .models import ArmStats, Event


def aggregate(events: Iterable[Event]) -> dict[str, ArmStats]:
    """Apply each event once, so delivery retries cannot inflate outcomes."""
    result: dict[str, ArmStats] = {}
    seen: set[str] = set()
    increments = {"impression": "impressions", "click": "clicks", "conversion": "conversions"}
    for event in events:
        if event.event_id in seen:
            continue
        if event.kind not in increments:
            raise ValueError(f"unsupported event kind: {event.kind}")
        seen.add(event.event_id)
        stats = result.setdefault(event.arm, ArmStats())
        field = increments[event.kind]
        setattr(stats, field, getattr(stats, field) + 1)
    return result


def reward(stats: ArmStats) -> float:
    return round(stats.conversions * 100.0 + stats.clicks * 2.0 + stats.impressions * 0.01, 2)
