"""
Vajra Agent Collaboration Test

Tests multiple agents
working together.
"""



from vajra.agents.agent import Agent


from vajra.orchestration.mission import (
    Mission
)


from vajra.orchestration.collaboration.collaboration_protocol import (
    AgentCollaborationProtocol
)





def main():


    print("=" * 60)

    print(
        "VAJRA AGENT COLLABORATION TEST"
    )

    print("=" * 60)



    # Create mission

    mission = Mission(

        name="Build AI Knowledge System",

        objective=
        "Create autonomous workflow"

    )



    # Create agents


    research_agent = Agent(

        name="Research Agent",

        purpose=
        "Analyze information",

        capabilities=[
            "research"
        ]

    )



    execution_agent = Agent(

        name="Execution Agent",

        purpose=
        "Execute implementation",

        capabilities=[
            "execution"
        ]

    )



    validation_agent = Agent(

        name="Validation Agent",

        purpose=
        "Validate results",

        capabilities=[
            "validation"
        ]

    )



    agents = [

        research_agent,

        execution_agent,

        validation_agent

    ]



    # Create protocol

    protocol = AgentCollaborationProtocol()



    result = protocol.collaborate(

        mission,

        agents

    )



    print()

    print(
        "COLLABORATION RESULT"
    )



    print(result)



    print()

    print("=" * 60)

    print(
        "AGENT COLLABORATION COMPLETE"
    )

    print("=" * 60)





if __name__ == "__main__":

    main()