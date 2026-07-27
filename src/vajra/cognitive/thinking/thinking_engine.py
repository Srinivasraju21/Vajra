"""
Thinking Engine

Generates structured thoughts from goals and tasks.
"""

from vajra.cognitive.thought.thought import Thought


class ThinkingEngine:
    """
    Generates cognitive thoughts.
    """

    def __init__(self):
        """
        Initialise the Thinking Engine.
        """
        pass

    def think(self, task):
        """
        Generate a thought from a task.

        Parameters:
            task: Task object.

        Returns:
            Thought
        """

        content = (
            f"Task '{task.action}' is ready "
            f"for execution using "
            f"'{task.capability}' capability."
        )

        return Thought(
            thought_type="analysis",
            source="ThinkingEngine",
            content=content,
            confidence=0.95,
            metadata={
                "task_action": task.action,
                "capability": task.capability,
            },
        )