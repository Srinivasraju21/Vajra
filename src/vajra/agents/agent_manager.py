"""
Vajra Agent Manager

Responsible for managing
autonomous agents.
"""


from vajra.agents.agent import (
    Agent
)

from vajra.agents.agent_registry import (
    AgentRegistry
)


class AgentManager:
    """
    Controls lifecycle and
    availability of agents.
    """


    def __init__(self):

        # Storage for available agents
        self.registry = AgentRegistry()



    def create_agent(
        self,
        name,
        purpose,
        capabilities=None
    ):
        """
        Create a new Vajra agent.
        """


        agent = Agent(

            name=name,

            purpose=purpose,

            capabilities=capabilities

        )


        self.registry.register(
            agent
        )


        return agent



    def activate_agent(
        self,
        agent_id
    ):
        """
        Activate an agent.
        """


        agent = (
            self.registry
            .get(agent_id)
        )


        if agent:

            agent.activate()

            return True


        return False



    def start_agent(
        self,
        agent_id
    ):
        """
        Start agent execution.
        """


        agent = (
            self.registry
            .get(agent_id)
        )


        if agent:

            agent.start()

            return True


        return False



    def complete_agent(
        self,
        agent_id
    ):
        """
        Complete agent execution.
        """


        agent = (
            self.registry
            .get(agent_id)
        )


        if agent:

            agent.complete()

            return True


        return False



    def get_agent(
        self,
        agent_id
    ):
        """
        Retrieve agent.
        """

        return (
            self.registry
            .get(agent_id)
        )



    def list_agents(self):
        """
        Return all registered agents.
        """

        return (
            self.registry
            .get_all()
        )