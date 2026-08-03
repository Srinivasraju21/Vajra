"""
Vajra Autonomous Mission Controller Test
"""



from vajra.agents.agent import Agent

from vajra.agents.agent_registry import (
    AgentRegistry
)


from vajra.orchestration.mission_generator.dynamic_mission_generator import (
    DynamicMissionGenerator
)


from vajra.orchestration.assignment.agent_assignment_engine import (
    AgentAssignmentEngine
)


from vajra.orchestration.collaboration.collaboration_protocol import (
    AgentCollaborationProtocol
)


from vajra.orchestration.recovery.failure_recovery_manager import (
    FailureRecoveryManager
)


from vajra.orchestration.controller.autonomous_mission_controller import (
    AutonomousMissionController
)





def main():



    print("=" * 60)

    print(
        "VAJRA AUTONOMOUS MISSION CONTROLLER TEST"
    )

    print("=" * 60)



    registry = AgentRegistry()



    research = Agent(

        name="Research Agent",

        purpose="Analyze information",

        capabilities=[
            "research"
        ]

    )



    execution = Agent(

        name="Execution Agent",

        purpose="Execute tasks",

        capabilities=[
            "execution"
        ]

    )



    registry.register(
        research
    )


    registry.register(
        execution
    )





    controller = AutonomousMissionController(


        mission_generator=

            DynamicMissionGenerator(),



        assignment_engine=

            AgentAssignmentEngine(
                registry
            ),



        collaboration_protocol=

            AgentCollaborationProtocol(),



        recovery_manager=

            FailureRecoveryManager()

    )





    result = controller.execute(

        "research architecture"

    )





    print()

    print(
        "MISSION RESULT"
    )


    print(result)



    print()

    print("=" * 60)

    print(
        "AUTONOMOUS MISSION CONTROLLER COMPLETE"
    )

    print("=" * 60)





if __name__ == "__main__":

    main()