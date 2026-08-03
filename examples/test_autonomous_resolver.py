"""
Vajra Autonomous Resolver Test

Tests complete goal-to-decision flow.
"""


from vajra.cognitive.resolution.autonomous_resolver import (
    AutonomousResolver
)


from vajra.planning.risk import (
    RiskLevel
)





def main():


    print("=" * 60)

    print(
        "VAJRA AUTONOMOUS RESOLVER TEST"
    )

    print("=" * 60)



    # Create autonomous reasoning system

    resolver = AutonomousResolver()



    # High level user goal

    goal = (

        "Prepare workspace for Vajra"

    )



    # Resolve automatically

    result = (

        resolver.resolve(

            goal,

            RiskLevel.REVERSIBLE

        )

    )



    print()

    print(
        "AUTONOMOUS DECISION"
    )

    print()



    print(result)



    print()

    print("=" * 60)

    print(
        "AUTONOMOUS RESOLVER COMPLETE"
    )

    print("=" * 60)





if __name__ == "__main__":

    main()