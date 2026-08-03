"""
Execution Plan Model

Represents a complete plan generated
by Vajra Planner.
"""

from dataclasses import dataclass
from typing import List

from vajra.planning.planned_task import PlannedTask


@dataclass
class ExecutionPlan:
    """
    Collection of tasks required
    to achieve a goal.
    """

    goal_id: str

    tasks: List[PlannedTask]

    status: str = "created"