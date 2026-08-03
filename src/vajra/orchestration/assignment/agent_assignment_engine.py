"""
Vajra Agent Assignment Engine

Automatically selects the correct
agent for a mission.

Flow:

Mission

    ↓

Agent Registry

    ↓

Capability Matching

    ↓

Agent Assignment
"""





class AgentAssignmentEngine:
    """
    Assigns missions to agents based
    on their capabilities.
    """



    def __init__(
        self,
        agent_registry
    ):
        """
        Initialize assignment engine.
        """

        # Store registry

        self.agent_registry = (
            agent_registry
        )





    def _get_agents(
        self
    ):
        """
        Extract actual Agent objects
        from registry.

        Different phases of Vajra
        may expose registry data
        differently.
        """



        # Case 1:
        # Registry has get_agents()

        if hasattr(
            self.agent_registry,
            "get_agents"
        ):


            agents = (

                self.agent_registry
                .get_agents()

            )



        # Case 2:
        # Registry has get_all_agents()

        elif hasattr(
            self.agent_registry,
            "get_all_agents"
        ):


            agents = (

                self.agent_registry
                .get_all_agents()

            )



        # Case 3:
        # Direct dictionary/list storage

        elif hasattr(
            self.agent_registry,
            "agents"
        ):


            agents = (

                self.agent_registry
                .agents

            )


        else:

            agents = []





        # --------------------------------
        # Convert dictionary registry
        # into Agent objects
        # --------------------------------


        if isinstance(
            agents,
            dict
        ):


            agents = list(

                agents.values()

            )



        return agents





    def assign(
        self,
        mission
    ):
        """
        Assign best agent to mission.
        """



        # Get available agents

        agents = self._get_agents()



        # Mission requirement

        requirement = (

            mission.name
            .lower()

        )





        # Capability matching

        for agent in agents:



            # Ignore invalid entries

            if not hasattr(
                agent,
                "capabilities"
            ):

                continue



            for capability in agent.capabilities:



                if capability.lower() in requirement:



                    mission.add_agent(

                        agent

                    )


                    return agent





        # --------------------------------
        # Fallback
        # --------------------------------


        if agents:


            agent = agents[0]


            mission.add_agent(

                agent

            )


            return agent





        return None