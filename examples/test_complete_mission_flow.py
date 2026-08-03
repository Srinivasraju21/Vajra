"""
Vajra Complete Mission Flow Test

Validates complete autonomous
mission execution pipeline.
"""


from vajra.agents.agent_manager import (
    AgentManager
)

from vajra.orchestration.agent_orchestrator import (
    AgentOrchestrator
)

from vajra.orchestration.mission_controller import (
    MissionController
)



def main():


    print("=" * 70)

    print(
        "VAJRA COMPLETE MISSION FLOW TEST"
    )

    print("=" * 70)



    # Create agent management layer

    agent_manager = AgentManager()



    # Create agents

    planner_agent = (

        agent_manager.create_agent(

            name="Planning Agent",

            purpose=
            "Break mission into steps",

            capabilities=[

                "planning"

            ]

        )

    )



    execution_agent = (

        agent_manager.create_agent(

            name="Execution Agent",

            purpose=
            "Execute mission tasks",

            capabilities=[

                "execution"

            ]

        )

    )



    # Create orchestrator

    orchestrator = AgentOrchestrator(

        agent_manager

    )



    # Create mission controller

    mission_controller = MissionController(

        orchestrator

    )



    # Create mission

    mission = (

        mission_controller.create_mission(

            name=
            "Build AI Assistant",

            objective=
            "Create an autonomous AI workflow"

        )

    )



    print("\nMISSION CREATED")

    print(
        mission.get_info()
    )



    # Assign agents

    mission_controller.assign_agents(

        mission,

        [

            planner_agent,

            execution_agent

        ]

    )



    print("\nAGENTS ASSIGNED")

    print(
        mission.get_info()
    )



    # Execute mission

    completed_mission = (

        mission_controller
        .execute_mission(
            mission
        )

    )



    print("\nMISSION RESULT")

    print(
        completed_mission.get_info()
    )



    print("\n")

    print("=" * 70)

    print(
        "PHASE 7.2 MISSION LAYER COMPLETE"
    )

    print("=" * 70)



if __name__ == "__main__":

    main()