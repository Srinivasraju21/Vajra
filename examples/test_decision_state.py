"""
Vajra Decision State Test
"""


from vajra.decision.decision_state import (
    DecisionState
)



def main():


    print("=" * 60)

    print(
        "VAJRA DECISION STATE TEST"
    )

    print("=" * 60)



    decision = DecisionState(

        goal=
        "Clean system files",

        options=[

            "Delete temporary files",

            "Remove applications",

            "Clear cache"

        ]

    )



    decision.set_risk(

        {

            "level":
            "LOW",

            "reason":
            "Temporary files are reversible"

        }

    )



    decision.select_option(

        "Delete temporary files",

        confidence=0.92

    )



    print(

        decision.get_info()

    )



    print("=" * 60)

    print(
        "DECISION STATE COMPLETE"
    )

    print("=" * 60)



if __name__ == "__main__":

    main()