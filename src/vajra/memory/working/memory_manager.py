"""
Working Memory Manager

Stores and retrieves memories created during execution.
"""

from vajra.memory.working.memory_object import Memory


class MemoryManager:
    """
    Manages Vajra's Working Memory.
    """

    def __init__(self):
        """
        Initialise the Working Memory.
        """

        # Store all memory objects here.
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

        Parameters:
            memory_type (str): Memory category.
            source (str): Component creating the memory.
            content (str): Memory description.
            metadata (dict): Optional extra information.
            status (str): Success, failure, warning, etc.

        Returns:
            Memory: Newly created Memory object.
        """

        memory = Memory(
            memory_type=memory_type,
            source=source,
            content=content,
            metadata=metadata,
            status=status,
        )

        # Save memory into Working Memory.
        self.memories.append(memory)

        return memory

    def get_all_memories(self):
        """
        Return every stored memory.

        Returns:
            list: List of Memory objects.
        """

        return self.memories

    def clear(self):
        """
        Remove every memory from Working Memory.
        """

        self.memories.clear()