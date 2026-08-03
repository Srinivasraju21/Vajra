"""
Vajra Decision Engine Test
"""


from vajra.decision.decision_engine import (
    DecisionEngine
)


from vajra.planning.risk import (
    RiskLevel
)





def main():


    print("=" * 60)

    print(
        "VAJRA DECISION ENGINE TEST"
    )

    print("=" * 60)



    engine = DecisionEngine()



    result = engine.decide(

        goal=
        "Clean computer system",


        options=[

            "delete temporary files",

            "remove applications",

            "format system"

        ],


        risk_level=

        RiskLevel.REVERSIBLE,


        risk_scores={

            "delete temporary files":1,

            "remove applications":3,

            "format system":5

        },


        reliability_scores={

            "delete temporary files":5,

            "remove applications":2,

            "format system":1

        },


        strategy_scores={

            "delete temporary files":4,

            "remove applications":2,

            "format system":0

        }

    )



    print()

    print(
        "FINAL DECISION"
    )

    print()



    print(result)



    print()

    print("=" * 60)

    print(
        "DECISION ENGINE COMPLETE"
    )

    print("=" * 60)





if __name__ == "__main__":

    main()