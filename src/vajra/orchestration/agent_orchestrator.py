"""
Vajra Agent Orchestrator

Coordinates multiple autonomous
agents for mission execution.
"""


class AgentOrchestrator:
    """
    Responsible for coordinating
    available Vajra agents.
    """


    def __init__(
        self,
        agent_manager
    ):
        """
        Initialize orchestrator.

        Args:
            agent_manager:
                Controls available agents
        """

        self.agent_manager = agent_manager



    def assign_agent(
        self,
        agent_id
    ):
        """
        Activate an agent
        for execution.
        """


        activated = (
            self.agent_manager
            .activate_agent(agent_id)
        )


        return activated



    def start_agent(
        self,
        agent_id
    ):
        """
        Start selected agent.
        """


        started = (
            self.agent_manager
            .start_agent(agent_id)
        )


        return started



    def complete_agent(
        self,
        agent_id
    ):
        """
        Mark agent completion.
        """


        completed = (
            self.agent_manager
            .complete_agent(agent_id)
        )


        return completed



    def execute_mission(
        self,
        mission_agents
    ):
        """
        Execute a mission
        using multiple agents.

        mission_agents:
            List of agent IDs
        """


        results = []


        for agent_id in mission_agents:


            self.assign_agent(
                agent_id
            )


            self.start_agent(
                agent_id
            )


            agent = (
                self.agent_manager
                .get_agent(agent_id)
            )


            results.append(
                agent
                .get_info()
            )


            self.complete_agent(
                agent_id
            )


        return results