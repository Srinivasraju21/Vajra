"""
Vajra Reflection Engine Test
"""


from vajra.adaptive.reflection.reflection_engine import (
    ReflectionEngine
)


from vajra.orchestration.mission import (
    Mission
)



def main():


    print("=" * 60)

    print(
        "VAJRA REFLECTION ENGINE TEST"
    )

    print("=" * 60)



    mission = Mission(

        name="AI Research Mission",

        objective=
        "Generate research report"

    )


    mission.complete(

        results=[

            "Research completed",

            "Report generated"

        ]

    )



    reflection_engine = ReflectionEngine()



    reflection = (

        reflection_engine.reflect(
            mission
        )

    )



    print()

    print(
        reflection
    )



    print()

    print("=" * 60)

    print(
        "REFLECTION TEST COMPLETE"
    )

    print("=" * 60)



if __name__ == "__main__":

    main()