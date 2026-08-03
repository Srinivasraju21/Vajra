"""
Test Objective Decomposition
"""


from vajra.orchestration.decomposition.objective_decomposer import (
    ObjectiveDecomposer
)





def main():


    print("=" * 60)

    print(
        "VAJRA OBJECTIVE DECOMPOSER TEST"
    )

    print("=" * 60)



    decomposer = ObjectiveDecomposer()



    objective = (

        "Build AI knowledge system"

    )



    missions = (

        decomposer.decompose(

            objective

        )

    )



    print()

    print(
        "OBJECTIVE:"
    )

    print(objective)



    print()

    print(
        "GENERATED MISSIONS:"
    )



    for mission in missions:

        print(

            "-",

            mission

        )



    print()

    print("=" * 60)

    print(
        "OBJECTIVE DECOMPOSER COMPLETE"
    )

    print("=" * 60)





if __name__ == "__main__":

    main()