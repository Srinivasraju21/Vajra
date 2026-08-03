from vajra.core.runtime.runtime_engine import RuntimeEngine
from vajra.core.task.task import Task


def main():

    print("=" * 60)
    print("CAPABILITY RESULT CONTRACT TEST")
    print("=" * 60)

    runtime = RuntimeEngine()

    tasks = [

        Task(
            capability="system",
            action="prepare_environment"
        ),

        Task(
            capability="filesystem",
            action="create_directory",
            parameters={
                "directory_name":
                "contract_test"
            }
        )

    ]

    results = runtime.execute(tasks)

    for result in results:

        print(result)

        print(type(result).__name__)

        assert hasattr(result, "success")
        assert hasattr(result, "message")

    print()

    print("ALL CAPABILITIES RETURN CapabilityResult")

    print("=" * 60)


if __name__ == "__main__":
    main()