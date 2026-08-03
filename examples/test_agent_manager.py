"""
Vajra Agent Manager Test

Validates creation,
registration and lifecycle
management of agents.
"""


from vajra.agents.agent_manager import (
    AgentManager
)



def main():

    print("=" * 60)

    print(
        "VAJRA AGENT MANAGER TEST"
    )

    print("=" * 60)



    manager = AgentManager()



    print("\nCreating Research Agent...\n")


    agent = manager.create_agent(

        name="Research Agent",

        purpose=
        "Collect and analyze information",

        capabilities=[

            "search",

            "analysis"

        ]

    )


    print(
        agent.get_info()
    )



    print("\nActivating agent...\n")


    manager.activate_agent(
        agent.id
    )


    print(
        manager
        .get_agent(agent.id)
        .get_info()
    )



    print("\nStarting agent...\n")


    manager.start_agent(
        agent.id
    )


    print(
        manager
        .get_agent(agent.id)
        .get_info()
    )



    print("\nCompleting agent...\n")


    manager.complete_agent(
        agent.id
    )


    print(
        manager
        .get_agent(agent.id)
        .get_info()
    )



    print("\nRegistered Agents:")


    for agent in manager.list_agents():

        print(
            agent.get_info()
        )


    print("\n" + "=" * 60)

    print(
        "AGENT MANAGER TEST COMPLETE"
    )

    print("=" * 60)



if __name__ == "__main__":

    main()