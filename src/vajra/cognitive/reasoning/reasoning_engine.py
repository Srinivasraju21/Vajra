"""
Reasoning Engine

Coordinates thinking and decision making.
"""

from vajra.cognitive.thinking.thinking_engine import ThinkingEngine
from vajra.cognitive.decision.decision_engine import DecisionEngine


class ReasoningEngine:
    """
    Coordinates Vajra's cognitive pipeline.
    """

    def __init__(self):
        """
        Initialise the Reasoning Engine.
        """
        self.thinking_engine = ThinkingEngine()
        self.decision_engine = DecisionEngine()

    def reason(self, task):
        """
        Think about a task and make a decision.

        Parameters:
            task: Task object.

        Returns:
            tuple:
                (Thought, Decision)
        """

        thought = self.thinking_engine.think(task)

        decision = self.decision_engine.decide(thought)

        return thought, decision