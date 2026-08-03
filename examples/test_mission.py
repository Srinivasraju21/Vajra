"""
Vajra Mission Object Test
"""


from vajra.orchestration.mission import (
    Mission
)


def main():


    print("=" * 60)

    print(
        "VAJRA MISSION TEST"
    )

    print("=" * 60)



    mission = Mission(

        name="Build AI System",

        objective=
        "Create an autonomous AI workflow"

    )


    print(
        "\nInitial Mission"
    )


    print(
        mission.get_info()
    )



    mission.start_planning()

    mission.assign_agents()

    mission.start_execution()



    print(
        "\nExecuting Mission"
    )


    print(
        mission.get_info()
    )



    mission.complete(

        results=[

            "Planning complete",

            "Execution complete"

        ]

    )



    print(
        "\nCompleted Mission"
    )


    print(
        mission.get_info()
    )



    print("=" * 60)

    print(
        "MISSION TEST COMPLETE"
    )

    print("=" * 60)



if __name__ == "__main__":

    main()