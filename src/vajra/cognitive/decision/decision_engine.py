"""
Decision Engine

Makes execution decisions based on thoughts
and learned knowledge.
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


    def decide(self, thought, knowledge=None):
        """
        Decide whether to execute a task.

        Parameters:
            thought:
                Thought object.

            knowledge:
                List of Knowledge objects.

        Returns:
            dict:
                Decision result.
        """


        confidence = thought.confidence


        # Increase confidence when previous knowledge exists.
        if knowledge:

            confidence += 0.05


        if confidence >= self.minimum_confidence:

            return {
                "decision": "execute",
                "approved": True,
                "reason": (
                    "Confidence meets execution threshold "
                    "with knowledge support."
                    if knowledge
                    else
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