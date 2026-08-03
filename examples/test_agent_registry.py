"""
Vajra Agent Registry Test

Validates agent registration
and retrieval.
"""


from vajra.agents.agent import Agent

from vajra.agents.agent_registry import (
    AgentRegistry
)



def main():

    print("=" * 60)

    print(
        "VAJRA AGENT REGISTRY TEST"
    )

    print("=" * 60)



    registry = AgentRegistry()



    agent = Agent(

        name="Research Agent",

        purpose=
        "Collect information",

        capabilities=[

            "search"

        ]

    )


    print(
        "\nRegistering agent...\n"
    )


    registry.register(
        agent
    )


    print(
        "Total Agents:",
        registry.count()
    )


    retrieved = registry.get(
        agent.id
    )


    print(
        "\nRetrieved Agent:"
    )


    print(
        retrieved.get_info()
    )


    print(
        "\nAll Agents:"
    )


    for item in registry.get_all():

        print(
            item.get_info()
        )


    print("\n" + "=" * 60)

    print(
        "AGENT REGISTRY TEST COMPLETE"
    )

    print("=" * 60)



if __name__ == "__main__":

    main()