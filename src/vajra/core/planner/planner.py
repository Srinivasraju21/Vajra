"""
Planner Module

The Planner converts a Goal into an execution plan.

Future responsibilities:
- Task decomposition
- Reasoning
- Prioritization
- Dependency management
"""


class Planner:
    """
    Responsible for creating execution plans
    from Vajra Goals.
    """

    def create_plan(self, goal):
        """
        Converts a Goal object into a list of tasks.

        Example:

        Goal:
        "Create a project report"

        Output:
        [
            "Understand requirements",
            "Collect information",
            "Generate report"
        ]
        """

        # Store the goal objective
        objective = goal.objective

        # Create initial task plan.
        # In future versions this will be generated
        # dynamically using AI reasoning models.
        plan = [
            f"Understand goal: {objective}",
            "Identify required resources",
            "Execute required actions",
            "Validate final result"
        ]

        # Return the generated execution plan
        return plan