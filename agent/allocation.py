import random

from .models import ArmStats


def choose_arm(arms: dict[str, ArmStats], rng: random.Random) -> str:
    """Thompson-sample a conversion rate with a caller-owned random source."""
    if not arms:
        raise ValueError("at least one arm is required")

    def draw(stats: ArmStats) -> float:
        failures = max(0, stats.impressions - stats.conversions)
        return rng.betavariate(1 + stats.conversions, 1 + failures)

    return max(arms, key=lambda name: (draw(arms[name]), name))
