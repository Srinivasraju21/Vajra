"""
System Capability

Handles Vajra internal system operations.
"""
from vajra.capabilities.capability import Capability
from vajra.capabilities.result import CapabilityResult
from vajra.capabilities.risk import RiskLevel


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

        return CapabilityResult(
            success=False,
            message=f"Unsupported system action: {task.action}"
        )

    def prepare_environment(self):
        """
        Prepare Vajra before execution begins.
        """

        return CapabilityResult(
            success=True,
            message="Environment prepared successfully.",
            data={
                "risk": RiskLevel.READ_ONLY.value,
                "operation": "prepare_environment"
            }
        )

    def validate_execution(self):
        """
        Validate execution after tasks complete.
        """

        return CapabilityResult(
            success=True,
            message="Execution validated successfully.",
            data={
                "risk": RiskLevel.READ_ONLY.value,
                "operation": "validate_execution"
            }
        )