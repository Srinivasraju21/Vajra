"""
Decision Engine

Makes execution decisions based on generated thoughts.
"""


class DecisionEngine:
    """
    Decides whether a task should proceed.
    """

    def __init__(self):
        """
        Initialise the Decision Engine.
        """
        self.minimum_confidence = 0.80

    def decide(self, thought):
        """
        Decide whether to execute a task.

        Parameters:
            thought: Thought object.

        Returns:
            dict: Decision result.
        """

        if thought.confidence >= self.minimum_confidence:

            return {
                "decision": "execute",
                "approved": True,
                "reason": (
                    "Confidence meets execution threshold."
                ),
            }

        return {
            "decision": "reject",
            "approved": False,
            "reason": (
                "Confidence below execution threshold."
            ),
        }