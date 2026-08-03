from vajra.core.learning.capability_reliability_manager import (
    CapabilityReliabilityManager
)


def main():

    print("=" * 60)
    print("VAJRA CAPABILITY RELIABILITY TEST")
    print("=" * 60)

    manager = (
        CapabilityReliabilityManager()
    )

    manager.record_execution(
        "filesystem",
        True
    )

    manager.record_execution(
        "filesystem",
        True
    )

    manager.record_execution(
        "filesystem",
        False
    )

    manager.record_execution(
        "system",
        True
    )

    manager.record_execution(
        "system",
        True
    )

    manager.record_execution(
        "system",
        True
    )

    print("\nFilesystem Statistics")
    print("------------------------------")

    print(
        manager.get_statistics(
            "filesystem"
        )
    )

    print("\nSystem Statistics")
    print("------------------------------")

    print(
        manager.get_statistics(
            "system"
        )
    )

    print("\nAll Statistics")
    print("------------------------------")

    all_stats = (
        manager.get_all_statistics()
    )

    for capability, stats in all_stats.items():

        print(
            capability,
            "->",
            stats
        )

    print("\nTEST PASSED")
    print("=" * 60)


if __name__ == "__main__":
    main()