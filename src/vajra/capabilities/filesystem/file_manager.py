"""
File Manager Capability

Handles filesystem operations
inside Vajra.
"""


from vajra.capabilities.capability import Capability
from vajra.capabilities.result import CapabilityResult
from vajra.capabilities.risk import RiskLevel



class FileManager(Capability):
    """
    Provides filesystem related capabilities.
    """


    def __init__(self):

        super().__init__(
            "filesystem",
            "Handles filesystem operations"
        )



    def execute(self, task):
        """
        Execute filesystem tasks.
        """


        if task.action == "create_directory":

            directory_name = (
                task.parameters
                .get("directory_name")
            )


            return self.create_directory(
                directory_name
            )


        return CapabilityResult(
            success=False,
            message=(
                f"Unsupported filesystem action: "
                f"{task.action}"
            )
        )



    def create_directory(
        self,
        directory_name
    ):
        """
        Create a directory.
        """


        import os


        try:

            os.makedirs(
                directory_name,
                exist_ok=True
            )


            return CapabilityResult(
                success=True,

                message=(
                    f"Directory "
                    f"{directory_name} "
                    f"created successfully."
                ),

                data={
                    "risk":
                        RiskLevel.REVERSIBLE.value,

                    "operation":
                        "create_directory",

                    "directory":
                        directory_name
                }
            )


        except Exception as error:

            return CapabilityResult(
                success=False,
                message=str(error)
            )