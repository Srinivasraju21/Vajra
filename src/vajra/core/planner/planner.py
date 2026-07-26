"""
Planner

The Planner converts a Goal into a sequence of executable
Task objects.
"""

# Import the Task class.
from vajra.core.task.task import Task


class Planner:
    """
    Generates execution plans from Goals.
    """

    def create_plan(self, goal):
        """
        Create an execution plan for a goal.

        Parameters:
            goal: Goal object.

        Returns:
            list[Task]: Ordered list of executable tasks.
        """

        plan = [

            # Step 1: Prepare the environment.
            Task(
                action="prepare_environment",
                capability="system",
            ),

            # Step 2: Create the project workspace.
            Task(
                action="create_directory",
                capability="filesystem",
                parameters={
                    "directory_name": "vajra_workspace"
                }
            ),

            # Step 3: Validate execution.
            Task(
                action="validate_execution",
                capability="system",
            )
        ]

        return plan