"""
Vajra Agent Orchestrator Test

Tests multiple agents working
under orchestration.
"""


from vajra.agents.agent_manager import (
    AgentManager
)

from vajra.orchestration.agent_orchestrator import (
    AgentOrchestrator
)



def main():


    print("=" * 60)

    print(
        "VAJRA AGENT ORCHESTRATOR TEST"
    )

    print("=" * 60)



    manager = AgentManager()



    research_agent = (
        manager.create_agent(

            name="Research Agent",

            purpose=
            "Collect information",

            capabilities=[

                "search"

            ]

        )
    )



    coding_agent = (
        manager.create_agent(

            name="Coding Agent",

            purpose=
            "Develop software",

            capabilities=[

                "coding"

            ]

        )
    )



    orchestrator = (
        AgentOrchestrator(
            manager
        )
    )



    print(
        "\nExecuting Mission...\n"
    )



    results = (
        orchestrator
        .execute_mission(

            [

                research_agent.id,

                coding_agent.id

            ]

        )
    )



    print(
        "=" * 60
    )

    print(
        "MISSION RESULTS"
    )

    print(
        "=" * 60
    )



    for result in results:

        print(result)



    print(
        "\n"
        + "=" * 60
    )

    print(
        "AGENT ORCHESTRATOR TEST COMPLETE"
    )

    print(
        "=" * 60
    )



if __name__ == "__main__":

    main()

    