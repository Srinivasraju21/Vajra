"""
Capability Execution Result
"""


class CapabilityResult:

    def __init__(
        self,
        success,
        message,
        data=None
    ):
        self.success = success
        self.message = message
        self.data = data or {}


    def __repr__(self):

        return (
            f"CapabilityResult("
            f"success={self.success}, "
            f"message='{self.message}')"
        )
    