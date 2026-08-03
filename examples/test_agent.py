"""
Vajra Agent Core Test

Creates and manages
a simple autonomous agent.
"""


from vajra.agents.agent import (
    Agent
)



def main():

    print("=" * 60)

    print(
        "VAJRA AGENT CORE TEST"
    )

    print("=" * 60)



    agent = Agent(

        name="Research Agent",

        purpose=
        "Collect and analyze information",

        capabilities=[

            "search",

            "summarization",

            "analysis"

        ]

    )


    print("\nCreated Agent")

    print(
        agent.get_info()
    )



    print("\nActivating agent...")

    agent.activate()

    print(
        agent.get_info()
    )



    print("\nStarting execution...")

    agent.start()

    print(
        agent.get_info()
    )



    print("\nCompleting execution...")

    agent.complete()

    print(
        agent.get_info()
    )



    print("\n" + "=" * 60)

    print(
        "AGENT CORE TEST COMPLETE"
    )

    print("=" * 60)



if __name__ == "__main__":

    main()