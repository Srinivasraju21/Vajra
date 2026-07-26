"""
Base Capability

Every capability in Project Vajra inherits from this class.
"""


class Capability:
    """
    Base class for all Vajra capabilities.
    """

    def __init__(self, name):
        """
        Initialise the capability.

        Parameters:
            name (str): Human-readable capability name.
        """
        self.name = name

    def execute(self, task):
        """
        Execute a Task.

        Every capability must implement this method.

        Parameters:
            task: Task object received from the Runtime Engine.

        Returns:
            Execution result.
        """
        raise NotImplementedError(
            "Capability must implement execute(task)."
        )