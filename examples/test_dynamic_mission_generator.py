"""
Vajra Dynamic Mission Generator Test

Tests:

Objectives

    ↓

Mission Objects
"""



from vajra.orchestration.mission_generator.dynamic_mission_generator import (
    DynamicMissionGenerator
)





def main():


    print("=" * 60)

    print(
        "VAJRA DYNAMIC MISSION GENERATOR TEST"
    )

    print("=" * 60)



    generator = DynamicMissionGenerator()



    objectives = [

        "Analyze Vajra architecture",

        "Implement autonomous modules",

        "Validate system execution"

    ]



    missions = generator.generate(

        objectives

    )



    print()

    print(
        "GENERATED MISSIONS"
    )



    for mission in missions:


        print()


        print(

            mission.get_info()

        )



    print()

    print("=" * 60)

    print(
        "MISSION GENERATOR COMPLETE"
    )

    print("=" * 60)





if __name__ == "__main__":

    main()