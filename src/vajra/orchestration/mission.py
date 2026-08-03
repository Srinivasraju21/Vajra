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
    objective that can involve
    multiple autonomous agents.
    """


    def __init__(
        self,
        name,
        objective
    ):
        """
        Initialize mission.
        """


        # Unique mission identifier
        self.id = str(
            uuid.uuid4()
        )


        # Mission details
        self.name = name

        self.objective = objective


        # Agents assigned
        self.agents = []


        # Execution results
        self.results = []


        # Initial state
        self.state = (
            MissionState.CREATED
        )



    def add_agent(
        self,
        agent
    ):
        """
        Assign agent to mission.
        """

        self.agents.append(
            agent
        )



    def start_planning(self):
        """
        Move mission to planning.
        """

        self.state = (
            MissionState.PLANNING
        )



    def assign_agents(self):
        """
        Mark agents assigned.
        """

        self.state = (
            MissionState.ASSIGNED
        )



    def start_execution(self):
        """
        Start execution.
        """

        self.state = (
            MissionState.EXECUTING
        )



    def complete(
        self,
        results=None
    ):
        """
        Complete mission.
        """

        self.results = (
            results
            if results
            else []
        )


        self.state = (
            MissionState.COMPLETED
        )



    def fail(self):
        """
        Mark mission failed.
        """

        self.state = (
            MissionState.FAILED
        )



    def get_info(self):
        """
        Return mission information.
        """

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
                    for agent in self.agents
                ],

            "results":
                self.results
        }