"""
Vajra Decision Runtime Test
"""


from vajra.core.runtime.runtime_engine import (
    RuntimeEngine
)


from vajra.core.runtime.decision_runtime import (
    DecisionRuntime
)


from vajra.core.planner.planner import (
    Planner
)


from vajra.planning.risk import (
    RiskLevel
)





def main():


    print("=" * 60)

    print(
        "VAJRA DECISION RUNTIME TEST"
    )

    print("=" * 60)



    runtime = RuntimeEngine()


    planner = Planner()



    decision_runtime = DecisionRuntime(

        runtime,

        planner

    )



    result = decision_runtime.execute_goal(

        goal=
        "Prepare workspace",


        options=[

            "create workspace",

            "delete workspace",

            "format system"

        ],


        risk_level=

        RiskLevel.REVERSIBLE

    )



    print()

    print(
        "DECISION"
    )

    print(

        result["decision"]

    )



    print()

    print(
        "EXECUTION"
    )

    print(

        result["results"]

    )



    print()

    print("=" * 60)

    print(
        "DECISION RUNTIME COMPLETE"
    )

    print("=" * 60)





if __name__ == "__main__":

    main()