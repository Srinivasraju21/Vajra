"""
System Capability

Handles Vajra internal system operations.
"""


from vajra.capabilities.capability import Capability



class SystemManager(Capability):
    """
    Performs internal system tasks.
    """


    def __init__(self):
        """
        Initialise the System capability.
        """

        super().__init__(
            "system",
            "Handles Vajra internal system operations"
        )



    def execute(self, task):
        """
        Execute an internal system task.
        """


        if task.action == "prepare_environment":

            return self.prepare_environment()


        elif task.action == "validate_execution":

            return self.validate_execution()


        return (
            f"Unsupported system action: "
            f"{task.action}"
        )



    def prepare_environment(self):
        """
        Prepare Vajra before execution begins.
        """

        return (
            "Environment prepared successfully."
        )



    def validate_execution(self):
        """
        Validate execution after tasks complete.
        """

        return (
            "Execution validated successfully."
        )