"""
Planner Engine

Converts Goals into Execution Plans.

The Planner Engine is responsible for:
- Understanding the user goal
- Breaking the goal into tasks
- Assigning risk levels
- Creating an Execution Plan

The Planner thinks.
The Runtime executes.
"""

from typing import List

from vajra.core.goal.goal_object import Goal

from vajra.planning.execution_plan import ExecutionPlan
from vajra.planning.planned_task import PlannedTask
from vajra.planning.risk import RiskLevel


class PlannerEngine:
    """
    Creates execution plans from user goals.
    """

    def create_plan(
        self,
        goal: Goal
    ) -> ExecutionPlan:
        """
        Generate an execution plan
        from a Goal object.
        """

        tasks = self.generate_tasks(goal)

        return ExecutionPlan(
            goal_id=id(goal),
            tasks=tasks
        )


    def generate_tasks(
        self,
        goal: Goal
    ) -> List[PlannedTask]:
        """
        Convert a goal into individual tasks.

        Currently this uses simple rule-based
        planning logic.

        Future versions will use:
        - LLM reasoning
        - Knowledge memory
        - Previous experiences
        - Capability selection
        """

        description = goal.objective.lower()

        tasks: List[PlannedTask] = []


        # Report generation workflow
        if "report" in description:

            tasks.append(
                PlannedTask(
                    name="Collect Information",
                    risk=RiskLevel.READ_ONLY
                )
            )


            tasks.append(
                PlannedTask(
                    name="Generate Report",
                    risk=RiskLevel.REVERSIBLE
                )
            )


        # File deletion workflow
        elif "delete" in description:

            tasks.append(
                PlannedTask(
                    name="Delete Files",
                    risk=RiskLevel.IRREVERSIBLE
                )
            )


        # Default workflow
        else:

            tasks.append(
                PlannedTask(
                    name="Execute Goal",
                    risk=RiskLevel.REVERSIBLE
                )
            )


        return tasks