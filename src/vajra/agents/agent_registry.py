"""
Vajra Agent Registry

Maintains all registered
autonomous agents.
"""


class AgentRegistry:
    """
    Stores and manages
    available Vajra agents.
    """


    def __init__(self):

        # Internal agent storage
        self.agents = {}



    def register(
        self,
        agent
    ):
        """
        Register a new agent.
        """

        self.agents[agent.id] = agent



    def get(
        self,
        agent_id
    ):
        """
        Retrieve an agent
        using its ID.
        """

        return (
            self.agents
            .get(agent_id)
        )



    def remove(
        self,
        agent_id
    ):
        """
        Remove an agent.
        """

        if agent_id in self.agents:

            del self.agents[agent_id]

            return True


        return False



    def get_all(self):
        """
        Return all registered agents.
        """

        return list(
            self.agents.values()
        )



    def count(self):
        """
        Return number of agents.
        """

        return len(
            self.agents
        )