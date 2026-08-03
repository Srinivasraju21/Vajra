"""
Vajra Goal Resolver Test

Tests whether Vajra can convert
a high-level objective into actions.
"""



from vajra.cognitive.resolution.goal_resolver import (
    GoalResolver
)





def main():


    print("=" * 60)

    print(
        "VAJRA GOAL RESOLVER TEST"
    )

    print("=" * 60)



    # Create resolver instance.

    resolver = GoalResolver()



    # User gives a high-level goal.

    goal = (

        "Prepare workspace for Vajra project"

    )



    # Resolve goal into actions.

    actions = (

        resolver.resolve(

            goal

        )

    )



    print()

    print(
        "GOAL:"
    )

    print(goal)



    print()

    print(
        "GENERATED ACTIONS:"
    )



    for action in actions:

        print(

            "-",

            action

        )



    print()

    print("=" * 60)

    print(
        "GOAL RESOLVER COMPLETE"
    )

    print("=" * 60)





if __name__ == "__main__":

    main()