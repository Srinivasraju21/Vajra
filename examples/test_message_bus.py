"""
Vajra Phase 7.5.9

Agent Communication Bus Test
"""


from vajra.agents.agent import Agent

from vajra.orchestration.communication.message_bus import (
    MessageBus
)




def main():


    print("=" * 60)

    print(
        "VAJRA AGENT COMMUNICATION BUS TEST"
    )

    print("=" * 60)



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



    bus = MessageBus()



    result = bus.send(

        research_agent,

        execution_agent,

        "Research completed successfully"

    )



    print()

    print(
        "MESSAGE SENT"
    )

    print(result)



    print()

    print(
        "MESSAGE HISTORY"
    )

    print(

        bus.get_messages()

    )



    print()

    print("=" * 60)

    print(
        "PHASE 7.5.9 COMMUNICATION TEST COMPLETE"
    )

    print("=" * 60)




if __name__ == "__main__":

    main()