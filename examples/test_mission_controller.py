"""
Vajra Mission Controller Test
"""


from vajra.orchestration.mission_controller import (
    MissionController
)


def main():

    print("=" * 60)

    print(
        "VAJRA MISSION CONTROLLER TEST"
    )

    print("=" * 60)



    controller = MissionController()



    mission = controller.create_mission(

        name="AI Research Project",

        objective=
        "Build an AI research report"

    )


    print("\nCreated Mission")

    print(
        mission.get_info()
    )



    controller.start_mission(
        mission
    )


    print("\nMission Planning")

    print(
        mission.get_info()
    )



    controller.execute_mission(
        mission
    )


    print("\nMission Executing")

    print(
        mission.get_info()
    )



    controller.complete_mission(

        mission,

        [

            "Research complete",

            "Report generated"

        ]

    )


    print("\nMission Completed")

    print(
        mission.get_info()
    )



    print("=" * 60)

    print(
        "MISSION CONTROLLER TEST COMPLETE"
    )

    print("=" * 60)



if __name__ == "__main__":

    main()