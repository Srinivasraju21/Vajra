"""
Goal Object

This module defines the fundamental computational unit
of Project Vajra.

A Goal represents:
- What the user wants to achieve
- The context of the request
- Current execution status
"""


class Goal:
    """
    Represents a user objective inside Vajra.

    Future versions will expand this object to include:
    - Constraints
    - Required capabilities
    - Execution plans
    - Memory references
    """

    def __init__(self, objective):
        # The main outcome the user wants to achieve.
        self.objective = objective

        # Current lifecycle state of the goal.
        # Initial state when a goal is created.
        self.status = "created"

    def update_status(self, new_status):
        """
        Updates the current state of the goal.

        Example states:
        created
        planning
        executing
        completed
        failed
        """

        self.status = new_status

    def get_details(self):
        """
        Returns the goal information
        in a structured format.
        """

        return {
            "objective": self.objective,
            "status": self.status
        }