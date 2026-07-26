"""
Capability Base Class

Every capability in Project Vajra inherits from this class.

A capability represents a real-world skill that Vajra
can perform, such as:
- File management
- Web browsing
- Email handling
- Calendar operations
- Database access
"""


class Capability:
    """
    Base class for all Vajra capabilities.
    """

    def __init__(self, name):
        # Human-readable capability name
        self.name = name

    def execute(self, task):
        """
        Execute a task.

        Every child capability must override
        this method with its own implementation.
        """

        raise NotImplementedError(
            "Child capability must implement execute()."
        )