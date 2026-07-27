"""
Learning Pipeline

Connects Memory with Knowledge extraction.
"""

from vajra.knowledge.learning.experience_extractor import ExperienceExtractor
from vajra.knowledge.manager.knowledge_manager import KnowledgeManager


class LearningPipeline:
    """
    Converts experiences into stored knowledge.
    """

    def __init__(self):
        """
        Initialise learning pipeline.
        """

        self.extractor = ExperienceExtractor()

        self.knowledge_manager = KnowledgeManager()


    def learn(self, memories):
        """
        Learn from a collection of memories.

        Parameters:
            memories:
                List of Memory objects.

        Returns:
            List of Knowledge objects.
        """

        learned = []

        for memory in memories:

            knowledge = self.extractor.extract(memory)

            self.knowledge_manager.add_knowledge(
                knowledge
            )

            learned.append(knowledge)

        return learned


    def get_knowledge(self):
        """
        Return stored knowledge.
        """

        return self.knowledge_manager.get_all_knowledge()
    