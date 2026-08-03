"""
Planned Task Model

Represents individual tasks generated
during Vajra planning.
"""

from dataclasses import dataclass

from vajra.planning.risk import RiskLevel


@dataclass
class PlannedTask:
    """
    Represents a single executable task.
    """

    name: str

    risk: RiskLevel

    status: str = "pending"