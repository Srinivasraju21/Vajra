"""
Vajra Decision Planner Test
"""


from vajra.core.planner.planner import (
    Planner
)


from vajra.core.planner.decision_planner import (
    DecisionPlanner
)


from vajra.planning.risk import (
    RiskLevel
)





def main():


    print("=" * 60)

    print(
        "VAJRA DECISION PLANNER TEST"
    )

    print("=" * 60)



    planner = Planner()



    decision_planner = DecisionPlanner(

        planner

    )



    result = decision_planner.create_plan(

        goal=

        "Prepare system cleanup",


        options=[

            "clear temporary files",

            "delete applications",

            "format system"

        ],


        risk_level=

        RiskLevel.REVERSIBLE

    )



    print()

    print(
        "DECISION RESULT"
    )

    print()



    print(

        result["decision"]

    )



    print()

    print(
        "PLAN RESULT"
    )

    print()



    print(

        result["plan"]

    )



    print()

    print("=" * 60)

    print(
        "DECISION PLANNER COMPLETE"
    )

    print("=" * 60)





if __name__ == "__main__":

    main()