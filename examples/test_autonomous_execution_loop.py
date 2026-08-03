from vajra.core.runtime.runtime_engine import (
    RuntimeEngine
)

from vajra.core.runtime.autonomous_execution_loop import (
    AutonomousExecutionLoop
)

from vajra.planning.planned_task import (
    PlannedTask
)

from vajra.planning.risk import (
    RiskLevel
)


def main():

    print("=" * 60)
    print("VAJRA AUTONOMOUS EXECUTION LOOP TEST")
    print("=" * 60)

    runtime = RuntimeEngine()

    loop = (
        AutonomousExecutionLoop(
            runtime
        )
    )

    tasks = [

        PlannedTask(
            name="system",
            action="prepare_environment",
            risk=RiskLevel.READ_ONLY
        ),

        PlannedTask(
            name="filesystem",
            action="create_directory",
            risk=RiskLevel.REVERSIBLE,
            parameters={
                "directory_name":
                "vajra_autonomous_demo"
            }
        )

    ]

    print("\nExecuting Plan...")
    print("-" * 40)

    results = (
        loop.execute(
            tasks
        )
    )

    print("\nExecution Results")
    print("-" * 40)

    for result in results:

        print(result)

    print("\nTEST PASSED")
    print("=" * 60)


if __name__ == "__main__":
    main()
    