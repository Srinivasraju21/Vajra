"""
Working Memory Manager

Stores and retrieves memories created during execution.
"""

from collections import Counter

from vajra.memory.working.memory_object import Memory


class MemoryManager:
    """
    Manages Vajra's Working Memory.
    """

    def __init__(self):
        """
        Initialise the Working Memory.
        """

        self.memories = []

    def add_memory(
        self,
        memory_type,
        source,
        content,
        metadata=None,
        status="success",
    ):
        """
        Create a new memory and store it.
        """

        memory = Memory(
            memory_type=memory_type,
            source=source,
            content=content,
            metadata=metadata,
            status=status,
        )

        self.memories.append(memory)

        return memory

    def get_all_memories(self):
        """
        Return every stored memory.
        """

        return self.memories

    def get_latest_memory(self):
        """
        Return the latest memory.
        """

        if not self.memories:
            return None

        return self.memories[-1]

    def get_memories_by_type(self, memory_type):
        """
        Return memories matching a type.
        """

        return [
            memory
            for memory in self.memories
            if memory.memory_type == memory_type
        ]

    def get_memories_by_source(self, source):
        """
        Return memories matching a source.
        """

        return [
            memory
            for memory in self.memories
            if memory.source == source
        ]

    def get_memories_by_status(self, status):
        """
        Return memories matching a status.
        """

        return [
            memory
            for memory in self.memories
            if memory.status == status
        ]

    def count_memories(self):
        """
        Return total number of memories.
        """

        return len(self.memories)

    def count_by_status(self):
        """
        Return memory counts grouped by status.
        """

        counter = Counter()

        for memory in self.memories:
            counter[memory.status] += 1

        return dict(counter)

    def count_by_source(self):
        """
        Return memory counts grouped by source.
        """

        counter = Counter()

        for memory in self.memories:
            counter[memory.source] += 1

        return dict(counter)

    def generate_report(self):
        """
        Generate a Working Memory analytics report.

        Returns:
            dict: Complete memory summary.
        """

        return {
            "total_memories": self.count_memories(),
            "status_summary": self.count_by_status(),
            "source_summary": self.count_by_source(),
        }

    def clear(self):
        """
        Remove every memory.
        """

        self.memories.clear()