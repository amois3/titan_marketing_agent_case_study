from .metrics import reward
from .models import ArmStats


def filter_min_conversions(arms: dict[str, ArmStats], minimum: int) -> tuple[dict[str, ArmStats], int]:
    if minimum < 0:
        raise ValueError("minimum conversions cannot be negative")
    kept = {name: stats for name, stats in arms.items() if stats.conversions >= minimum}
    return kept, len(arms) - len(kept)


def report(arms: dict[str, ArmStats], minimum: int = 0) -> str:
    kept, filtered = filter_min_conversions(arms, minimum)
    lines = [f"{filtered} arm(s) filtered by minimum conversions: {minimum}"]
    lines.extend(
        f"{name}: conversions={stats.conversions} clicks={stats.clicks} reward={reward(stats):.2f}"
        for name, stats in sorted(kept.items())
    )
    return "\n".join(lines)
