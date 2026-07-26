"""
Goal Engine

Responsible for creating and managing
Goal objects inside Project Vajra.

Future responsibilities:
- Goal understanding
- Goal decomposition
- Goal prioritization
- Goal tracking
"""

# Import the Goal data structure
from vajra.core.goal.goal_object import Goal


class GoalEngine:
    """
    Core engine responsible for handling
    user objectives.
    """

    def create_goal(self, user_input):
        """
        Converts raw user input into
        a structured Vajra Goal.

        Example:

        Input:
        "Create a project report"

        Output:
        Goal object
        """

        # Create a new Goal instance
        goal = Goal(user_input)

        # Return the structured goal
        return goal