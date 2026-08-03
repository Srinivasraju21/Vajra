"""
Vajra Mission Agent Integration Test
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


    print("=" * 60)

    print(
        "VAJRA MISSION EXECUTION TEST"
    )

    print("=" * 60)



    manager = AgentManager()



    research_agent = (

        manager.create_agent(

            name="Research Agent",

            purpose=
            "Research information",

            capabilities=[

                "search"

            ]

        )

    )



    coding_agent = (

        manager.create_agent(

            name="Coding Agent",

            purpose=
            "Write code",

            capabilities=[

                "coding"

            ]

        )

    )



    orchestrator = AgentOrchestrator(

        manager

    )



    controller = MissionController(

        orchestrator

    )



    mission = controller.create_mission(

        name="Build AI Application",

        objective=
        "Create application using agents"

    )



    controller.assign_agents(

        mission,

        [

            research_agent,

            coding_agent

        ]

    )



    result = (

        controller.execute_mission(
            mission
        )

    )



    print()

    print(
        result.get_info()
    )



    print("=" * 60)

    print(
        "MISSION EXECUTION COMPLETE"
    )

    print("=" * 60)



if __name__ == "__main__":

    main()