"""
Base Capability

Every capability in Project Vajra inherits from this class.
"""


class Capability:
    """
    Base class for all Vajra capabilities.
    """

    def __init__(
        self,
        name,
        description
    ):
        """
        Initialise capability.

        Parameters:
            name (str):
                Capability identifier

            description (str):
                What this capability does
        """

        self.name = name
        self.description = description


    def execute(self, task):
        """
        Execute a task.

        Every capability must implement this.
        """

        raise NotImplementedError(
            "Capability must implement execute(task)."
        )