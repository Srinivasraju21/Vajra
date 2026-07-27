"""
Reasoning Engine

Coordinates thinking, knowledge retrieval,
and decision making.
"""

from vajra.cognitive.thinking.thinking_engine import ThinkingEngine
from vajra.cognitive.decision.decision_engine import DecisionEngine


class ReasoningEngine:
    """
    Coordinates Vajra's cognitive pipeline.
    """

    def __init__(self, knowledge_manager):
        """
        Initialise the Reasoning Engine.

        Parameters:
            knowledge_manager:
                Shared KnowledgeManager instance
                provided by RuntimeEngine.
        """

        # Generates thoughts from tasks.
        self.thinking_engine = ThinkingEngine()

        # Makes decisions based on thoughts.
        self.decision_engine = DecisionEngine()

        # Uses shared learned knowledge.
        self.knowledge_manager = knowledge_manager


    def reason(self, task):
        """
        Think about a task using available knowledge
        and make a decision.

        Parameters:
            task:
                Task object.

        Returns:
            tuple:
                Thought,
                Decision
        """

        # Retrieve relevant knowledge.
        knowledge = self.knowledge_manager.search(
            task.capability
        )


        # Generate initial thought.
        thought = self.thinking_engine.think(
            task
        )


        # Add knowledge context if available.
        if knowledge:

            thought.content += (
                " Previous knowledge indicates: "
                f"{knowledge[0].content}"
            )


        # Make final decision.
        decision = self.decision_engine.decide(
            thought,
            knowledge
        )


        return thought, decision