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
    print("VAJRA AUTONOMOUS LEARNING TEST")
    print("=" * 60)

    runtime = RuntimeEngine()

    loop = AutonomousExecutionLoop(
        runtime
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
                "vajra_learning_demo"

            }

        )

    ]

    print("\nExecuting...\n")

    results = loop.execute(tasks)

    print("=" * 60)
    print("EXECUTION RESULTS")
    print("=" * 60)

    for result in results:

        print(result)

    print()

    print("=" * 60)
    print("KNOWLEDGE")
    print("=" * 60)

    for knowledge in loop.get_knowledge():

        print(knowledge)

    print()

    print("=" * 60)
    print("RELIABILITY")
    print("=" * 60)

    report = loop.get_reliability_report()

    for capability, stats in report.items():

        print(capability)

        print(stats)

        print()

    print("=" * 60)
    print("AUTONOMOUS LOOP COMPLETE")
    print("=" * 60)


if __name__ == "__main__":

    main()
    