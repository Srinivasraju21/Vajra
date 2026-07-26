"""
Capability Registry

The Capability Registry is responsible for storing and
providing access to all capabilities available in Vajra.

Instead of Runtime Engine directly creating capabilities,
it requests them from this registry.

This makes the system modular and easy to extend.
"""

# Import the File System capability.
from vajra.capabilities.filesystem.file_manager import FileManager
from vajra.capabilities.system.system_manager import SystemManager

class CapabilityRegistry:
    """
    Stores and manages all registered capabilities.
    """

    def __init__(self):
        """
        Register all available capabilities.
        """

        # Dictionary containing capability name → capability object.
        self.capabilities = {
            "filesystem": FileManager(),
            "system": SystemManager(),
        }

    def get_capability(self, capability_name):
        """
        Return the requested capability.

        Parameters:
            capability_name (str): Name of the capability.

        Returns:
            Capability object if found, otherwise None.
        """

        return self.capabilities.get(capability_name)