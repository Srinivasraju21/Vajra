"""
File System Capability

This module provides Vajra with the ability to interact
with the local file system.

Current features:
- Create directories

Future features:
- Create files
- Read files
- Write files
- Copy files
- Move files
- Delete files
"""

# Import Python's built-in operating system library.
# It provides functions for interacting with files and directories.
import os

# Import the base Capability class.
from vajra.capabilities.capability import Capability


class FileManager(Capability):
    """
    File System Capability.

    Handles file and directory operations for Vajra.
    """

    def __init__(self):
        # Initialise the parent Capability class.
        super().__init__("File System")

    def create_directory(self, directory_name):
        """
        Creates a directory if it does not already exist.

        Parameters:
            directory_name (str): Name or path of the directory.

        Returns:
            str: Status message.
        """

        # Check whether the directory already exists.
        if os.path.exists(directory_name):
            return f"Directory already exists: {directory_name}"

        # Create the directory.
        os.makedirs(directory_name)

        return f"Directory created successfully: {directory_name}"