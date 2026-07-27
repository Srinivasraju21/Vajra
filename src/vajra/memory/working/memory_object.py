"""
Memory Object

Represents a single memory inside Vajra's
working memory.
"""

from datetime import datetime
import uuid


class Memory:
    """
    Represents a single memory record.
    """

    def __init__(
        self,
        memory_type,
        source,
        content,
        metadata=None,
        status="success",
    ):
        """
        Create a new memory.

        Parameters:
            memory_type (str): Type of memory.
            source (str): Component that created the memory.
            content (str): Main memory content.
            metadata (dict): Optional additional information.
            status (str): Result status.
        """

        # Unique identifier for this memory.
        self.id = str(uuid.uuid4())

        # UTC timestamp when the memory was created.
        self.timestamp = datetime.utcnow()

        # Classification of memory.
        self.memory_type = memory_type

        # Component that produced the memory.
        self.source = source

        # Human-readable description.
        self.content = content

        # Extra structured data.
        self.metadata = metadata or {}

        # Success, failed, warning, etc.
        self.status = status

    def __str__(self):
        """
        Human-readable representation.
        """

        return (
            f"[{self.timestamp}] "
            f"{self.memory_type} | "
            f"{self.source} | "
            f"{self.content}"
        )