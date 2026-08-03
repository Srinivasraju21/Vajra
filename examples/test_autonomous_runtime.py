"""
Vajra Autonomous Runtime Test

Tests complete:

Goal → Decision → Plan → Execution
"""



from vajra.core.runtime.runtime_engine import (
    RuntimeEngine
)



from vajra.core.runtime.autonomous_runtime import (
    AutonomousRuntime
)





def main():


    print("=" * 60)

    print(
        "VAJRA AUTONOMOUS RUNTIME TEST"
    )

    print("=" * 60)



    # Existing execution engine

    runtime_engine = RuntimeEngine()



    # Autonomous layer

    vajra = AutonomousRuntime(

        runtime_engine

    )



    # User gives only goal

    result = vajra.execute(

        "Prepare workspace for Vajra project"

    )



    print()

    print(
        "GOAL"
    )

    print(

        result["goal"]

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
        "PLAN"
    )

    print(

        result["plan"]

    )



    print()

    print(
        "EXECUTION"
    )

    print(

        result["execution"]

    )



    print()

    print("=" * 60)

    print(
        "AUTONOMOUS RUNTIME COMPLETE"
    )

    print("=" * 60)





if __name__ == "__main__":

    main()