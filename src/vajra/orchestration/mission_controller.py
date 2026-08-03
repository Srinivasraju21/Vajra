"""
Vajra Mission Controller

Controls missions and coordinates
agent execution.
"""


from vajra.orchestration.mission import (
    Mission
)


class MissionController:
    """
    Controls mission lifecycle
    and agent coordination.
    """


    def __init__(
        self,
        agent_orchestrator=None
    ):
        """
        Initialize controller.
        """


        self.missions = []


        self.agent_orchestrator = (
            agent_orchestrator
        )



    def create_mission(
        self,
        name,
        objective
    ):
        """
        Create mission.
        """


        mission = Mission(

            name=name,

            objective=objective

        )


        self.missions.append(
            mission
        )


        return mission



    def assign_agents(
        self,
        mission,
        agents
    ):
        """
        Attach agents to mission.
        """


        for agent in agents:

            mission.add_agent(
                agent
            )


        mission.assign_agents()


        return mission



    def execute_mission(
        self,
        mission
    ):
        """
        Execute mission using
        agent orchestrator.
        """


        mission.start_execution()



        if self.agent_orchestrator:


            agent_ids = [

                agent.id

                for agent
                in mission.agents

            ]


            results = (

                self.agent_orchestrator
                .execute_mission(
                    agent_ids
                )

            )


            mission.complete(
                results
            )


        return mission



    def get_all_missions(
        self
    ):
        """
        Return missions.
        """

        return self.missions