"""
Knowledge Object

Represents learned information extracted
from Vajra experiences.
"""

from datetime import datetime


class Knowledge:
    """
    Represents a piece of learned knowledge.
    """

    def __init__(
        self,
        knowledge_type,
        source,
        content,
        confidence=1.0,
        metadata=None,
    ):
        """
        Initialise Knowledge.

        Parameters:
            knowledge_type (str):
                Category of knowledge.

            source (str):
                Component that created knowledge.

            content (str):
                Learned information.

            confidence (float):
                Confidence level.

            metadata (dict):
                Additional information.
        """

        self.timestamp = datetime.now()

        self.knowledge_type = knowledge_type

        self.source = source

        self.content = content

        self.confidence = confidence

        self.metadata = metadata or {}


    def __str__(self):
        """
        Human-readable representation.
        """

        return (
            f"[{self.timestamp}] "
            f"{self.knowledge_type} | "
            f"{self.source} | "
            f"{self.content} "
            f"(confidence={self.confidence:.2f})"
        )