"""
Vajra Failure Recovery Test
"""



from vajra.orchestration.recovery.failure_recovery_manager import (
    FailureRecoveryManager
)





def main():


    print("=" * 60)

    print(
        "VAJRA FAILURE RECOVERY TEST"
    )

    print("=" * 60)



    recovery = FailureRecoveryManager()



    # Simulated failure

    result = recovery.handle_failure(

        task="Deploy application",

        error="Execution timeout"

    )



    print()

    print(
        "RECOVERY RESULT"
    )


    print(result)



    print()

    print(
        "FAILURE HISTORY"
    )


    print(

        recovery.get_failure_history()

    )



    print()

    print("=" * 60)

    print(
        "FAILURE RECOVERY COMPLETE"
    )

    print("=" * 60)





if __name__ == "__main__":

    main()