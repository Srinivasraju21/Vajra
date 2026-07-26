"""
File System Capability

Provides Vajra with the ability to interact
with the local file system.
"""

import os

from vajra.capabilities.capability import Capability


class FileManager(Capability):
    """
    Handles all file system operations.
    """

    def __init__(self):
        """
        Initialise the File System capability.
        """
        super().__init__("filesystem")

    def execute(self, task):
        """
        Execute a filesystem task.

        Parameters:
            task: Task object.

        Returns:
            Result of the executed operation.
        """

        if task.action == "create_directory":

            return self.create_directory(
                task.parameters["directory_name"]
            )

        return f"Unsupported filesystem action: {task.action}"

    def create_directory(self, directory_name):
        """
        Create a directory if it does not exist.
        """

        if os.path.exists(directory_name):
            return f"Directory already exists: {directory_name}"

        os.makedirs(directory_name)

        return f"Directory created successfully: {directory_name}"