"""
Vajra Full Adaptive Intelligence Test

Validates complete learning loop.
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


from vajra.adaptive.adaptive_engine import (
    AdaptiveEngine
)



def main():


    print("=" * 70)

    print(
        "VAJRA FULL ADAPTIVE INTELLIGENCE TEST"
    )

    print("=" * 70)



    # -----------------------------
    # Create Agents
    # -----------------------------

    agent_manager = AgentManager()



    research_agent = (

        agent_manager.create_agent(

            name="Research Agent",

            purpose=
            "Analyze information",

            capabilities=[

                "research"

            ]

        )

    )



    execution_agent = (

        agent_manager.create_agent(

            name="Execution Agent",

            purpose=
            "Execute tasks",

            capabilities=[

                "execution"

            ]

        )

    )



    # -----------------------------
    # Create Mission System
    # -----------------------------

    orchestrator = AgentOrchestrator(

        agent_manager

    )



    mission_controller = MissionController(

        orchestrator

    )



    mission = (

        mission_controller
        .create_mission(

            name=
            "Build AI Knowledge System",

            objective=
            "Create autonomous workflow"

        )

    )



    mission_controller.assign_agents(

        mission,

        [

            research_agent,

            execution_agent

        ]

    )



    # -----------------------------
    # Execute Mission
    # -----------------------------

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



    # -----------------------------
    # Adaptive Learning
    # -----------------------------

    adaptive_engine = AdaptiveEngine()



    reflection = (

        adaptive_engine
        .learn_from_mission(

            completed_mission

        )

    )



    print("\nREFLECTION")

    print(

        reflection

    )



    print("\nLEARNING STATE")

    print(

        adaptive_engine
        .get_learning_state()

    )



    print("=" * 70)

    print(
        "FULL ADAPTIVE LOOP COMPLETE"
    )

    print("=" * 70)



if __name__ == "__main__":

    main()
    