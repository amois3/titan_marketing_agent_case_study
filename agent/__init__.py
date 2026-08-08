"""Runnable reference core for deterministic growth experimentation."""

from .allocation import choose_arm
from .metrics import aggregate, reward
from .models import ArmStats, Event
from .policy import AutonomyMode, may_publish
from .reporting import filter_min_conversions, report

__all__ = ["ArmStats", "AutonomyMode", "Event", "aggregate", "choose_arm", "filter_min_conversions", "may_publish", "report", "reward"]
