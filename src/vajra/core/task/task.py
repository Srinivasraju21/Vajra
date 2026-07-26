"""
Task Object

A Task represents one executable unit of work.

The Planner creates Task objects.

The Runtime Engine executes them.
"""


class Task:
    """
    Represents a single executable task.
    """

    def __init__(
        self,
        action,
        capability,
        parameters=None
    ):
        """
        Initialise a Task.

        Parameters:
            action (str): The operation to perform.
            capability (str): The capability responsible for execution.
            parameters (dict): Input data required by the capability.
        """

        # Action to perform
        self.action = action

        # Capability required
        self.capability = capability

        # Additional task parameters
        self.parameters = parameters or {}

    def __repr__(self):
        """
        String representation of the Task.
        Useful while debugging.
        """

        return (
            f"Task("
            f"action='{self.action}', "
            f"capability='{self.capability}', "
            f"parameters={self.parameters}"
            f")"
        )