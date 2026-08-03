"""
Vajra Mission Object

Defines mission structure and
mission lifecycle management.
"""


from enum import Enum
import uuid



class MissionState(Enum):
    """
    Mission lifecycle states.
    """

    CREATED = "created"

    PLANNING = "planning"

    ASSIGNED = "assigned"

    EXECUTING = "executing"

    COMPLETED = "completed"

    FAILED = "failed"





class Mission:
    """
    Represents a Vajra mission.

    A mission is a higher-level
    objective involving autonomous agents.
    """



    def __init__(
        self,
        name,
        objective
    ):

        self.id = str(
            uuid.uuid4()
        )


        self.name = name

        self.objective = objective


        self.agents = []


        self.results = []


        self.state = (

            MissionState.CREATED

        )





    def add_agent(
        self,
        agent
    ):
        """
        Assign agent.
        """

        self.agents.append(
            agent
        )





    def start_planning(
        self
    ):

        self.state = (

            MissionState.PLANNING

        )





    def assign_agents(
        self
    ):

        self.state = (

            MissionState.ASSIGNED

        )





    def start_execution(
        self
    ):

        self.state = (

            MissionState.EXECUTING

        )





    def complete(
        self,
        results=None
    ):
        """
        Complete mission.

        Finalizes agent states
        and stores final results.
        """


        # Complete all agents

        for agent in self.agents:


            if hasattr(
                agent,
                "complete"
            ):

                agent.complete()



        # Store ONLY final agent states

        self.results = [

            agent.get_info()

            for agent in self.agents

        ]



        self.state = (

            MissionState.COMPLETED

        )





    def fail(
        self
    ):

        self.state = (

            MissionState.FAILED

        )





    def get_info(
        self
    ):

        return {


            "id":

                self.id,


            "name":

                self.name,


            "objective":

                self.objective,


            "state":

                self.state.value,


            "agents":

                [

                    agent.name

                    for agent
                    in self.agents

                ],


            "results":

                self.results

        }