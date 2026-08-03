"""
Vajra Agent Assignment Test

Tests:

Mission

    ↓

Agent Matching

    ↓

Assignment
"""



from vajra.agents.agent import Agent


from vajra.agents.agent_registry import (
    AgentRegistry
)


from vajra.orchestration.mission import (
    Mission
)


from vajra.orchestration.assignment.agent_assignment_engine import (
    AgentAssignmentEngine
)





def main():


    print("=" * 60)

    print(
        "VAJRA AGENT ASSIGNMENT TEST"
    )

    print("=" * 60)



    # Create registry

    registry = AgentRegistry()



    # Create agents


    research_agent = Agent(

        name="Research Agent",

        purpose="Analyze information",

        capabilities=[
            "research"
        ]

    )



    execution_agent = Agent(

        name="Execution Agent",

        purpose="Execute tasks",

        capabilities=[
            "execution"
        ]

    )



    # Register agents


    registry.register(

        research_agent

    )


    registry.register(

        execution_agent

    )



    # Create mission


    mission = Mission(

        name="research architecture",

        objective=
        "Analyze Vajra architecture"

    )



    # Create assignment engine


    assignment = AgentAssignmentEngine(

        registry

    )



    # Assign agent


    selected = assignment.assign(

        mission

    )



    print()

    print(
        "ASSIGNED AGENT"
    )


    print(

        selected.get_info()

    )



    print()

    print(
        "MISSION"
    )


    print(

        mission.get_info()

    )



    print()

    print("=" * 60)

    print(
        "AGENT ASSIGNMENT COMPLETE"
    )

    print("=" * 60)





if __name__ == "__main__":

    main()