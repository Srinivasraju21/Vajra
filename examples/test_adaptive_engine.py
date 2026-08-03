"""
Vajra Adaptive Intelligence Test
"""


from vajra.adaptive.adaptive_engine import (
    AdaptiveEngine
)


from vajra.orchestration.mission import (
    Mission
)



def main():


    print("=" * 70)

    print(
        "VAJRA ADAPTIVE INTELLIGENCE TEST"
    )

    print("=" * 70)



    mission = Mission(

        name=
        "Build AI Platform",

        objective=
        "Create autonomous system"

    )



    mission.complete(

        results=[

            "Planning complete",

            "Execution complete"

        ]

    )



    adaptive_engine = AdaptiveEngine()



    reflection = (

        adaptive_engine
        .learn_from_mission(
            mission
        )

    )



    print("\nReflection:")

    print(
        reflection
    )



    print("\nRecommendation:")

    print(

        adaptive_engine
        .get_recommendation()

    )



    print("=" * 70)

    print(
        "ADAPTIVE ENGINE COMPLETE"
    )

    print("=" * 70)



if __name__ == "__main__":

    main()