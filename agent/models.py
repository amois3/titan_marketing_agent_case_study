from dataclasses import dataclass


@dataclass(frozen=True)
class Event:
    event_id: str
    arm: str
    kind: str


@dataclass
class ArmStats:
    impressions: int = 0
    clicks: int = 0
    conversions: int = 0
