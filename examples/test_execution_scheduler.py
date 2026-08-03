from vajra.core.runtime.execution_scheduler import (
    ExecutionScheduler
)

from vajra.planning.planned_task import (
    PlannedTask
)

from vajra.planning.risk import (
    RiskLevel
)


def main():

    print("=" * 60)
    print("VAJRA EXECUTION SCHEDULER TEST")
    print("=" * 60)

    scheduler = (
        ExecutionScheduler()
    )

    tasks = [

        PlannedTask(
            name="filesystem",
            action="create_directory",
            risk=RiskLevel.REVERSIBLE,
            parameters={
                "directory_name":
                "phase681_demo"
            }
        ),

        PlannedTask(
            name="system",
            action="prepare_environment",
            risk=RiskLevel.READ_ONLY
        )

    ]

    scheduler.schedule(
        tasks
    )

    print("\nExecution Order")
    print("-" * 30)

    while scheduler.has_tasks():

        task = (
            scheduler.next_task()
        )

        print(task)

    print("\nTEST PASSED")
    print("=" * 60)


if __name__ == "__main__":
    main()
