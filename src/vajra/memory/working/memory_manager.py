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
        Return the most recently stored memory.
        """

        if not self.memories:
            return None

        return self.memories[-1]

    def get_memories_by_type(self, memory_type):
        """
        Return all memories of the specified type.
        """

        return [
            memory
            for memory in self.memories
            if memory.memory_type == memory_type
        ]

    def get_memories_by_source(self, source):
        """
        Return all memories created by the specified source.
        """

        return [
            memory
            for memory in self.memories
            if memory.source == source
        ]

    def get_memories_by_status(self, status):
        """
        Return all memories with the specified status.
        """

        return [
            memory
            for memory in self.memories
            if memory.status == status
        ]

    def count_memories(self):
        """
        Return the total number of memories.
        """

        return len(self.memories)

    def count_by_status(self):
        """
        Count memories grouped by status.

        Returns:
            dict: Status counts.
        """

        return dict(
            Counter(
                memory.status
                for memory in self.memories
            )
        )

    def clear(self):
        """
        Remove every memory.
        """

        self.memories.clear()