from enum import Enum


class AutonomyMode(str, Enum):
    FULL = "full"
    APPROVAL = "approval"
    SUGGEST_ONLY = "suggest_only"


def may_publish(mode: AutonomyMode, approved: bool) -> bool:
    return mode is AutonomyMode.FULL or (mode is AutonomyMode.APPROVAL and approved)
