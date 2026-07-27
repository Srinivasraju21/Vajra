"""
Experience Extractor

Converts Vajra experiences from memory
into reusable knowledge.
"""

from vajra.knowledge.base.knowledge import Knowledge


class ExperienceExtractor:
    """
    Extracts knowledge from execution experiences.
    """

    def __init__(self):
        """
        Initialise extractor.
        """
        pass


    def extract(self, memory):
        """
        Convert a memory object into knowledge.

        Parameters:
            memory:
                Memory object.

        Returns:
            Knowledge object.
        """

        knowledge_content = (
            f"Experience learned from "
            f"{memory.source}: "
            f"{memory.content}"
        )

        return Knowledge(
            knowledge_type="experience",
            source="ExperienceExtractor",
            content=knowledge_content,
            confidence=0.90,
            metadata={
                "memory_type": memory.memory_type,
                "status": memory.status,
            },
        )
