"""
Vajra Agent Core

Defines the fundamental autonomous
agent object used by Vajra.
"""


import uuid

from vajra.agents.agent_state import (
    AgentState
)


class Agent:
    """
    Represents an autonomous
    Vajra agent.
    """


    def __init__(
        self,
        name,
        purpose,
        capabilities=None
    ):
        """
        Initialize an agent.

        Args:
            name:
                Agent identity name

            purpose:
                Reason why agent exists

            capabilities:
                Skills available to agent
        """


        # Unique identity for every agent
        self.id = str(uuid.uuid4())


        # Human-readable name
        self.name = name


        # Agent responsibility
        self.purpose = purpose


        # Skills/tools agent can use
        self.capabilities = (
            capabilities
            if capabilities
            else []
        )


        # Initial lifecycle state
        self.state = AgentState.CREATED



    def activate(self):
        """
        Make agent available
        for execution.
        """

        self.state = AgentState.READY



    def start(self):
        """
        Start agent execution.
        """

        self.state = AgentState.WORKING



    def complete(self):
        """
        Mark successful completion.
        """

        self.state = AgentState.COMPLETED



    def fail(self):
        """
        Mark execution failure.
        """

        self.state = AgentState.FAILED



    def get_info(self):
        """
        Return agent information.
        """

        return {

            "id": self.id,

            "name": self.name,

            "purpose": self.purpose,

            "state": self.state.value,

            "capabilities":
                self.capabilities
        }