from vajra.core.learning.capability_reliability_manager import (
    CapabilityReliabilityManager
)

from vajra.planning.capability_selector import (
    CapabilitySelector
)


def main():

    print("=" * 60)
    print("VAJRA CAPABILITY SELECTOR TEST")
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

    selector = (
        CapabilitySelector(
            manager
        )
    )

    capabilities = [

        "filesystem",

        "system"

    ]

    best = (
        selector.select_best(
            capabilities
        )
    )

    print("\nAvailable Capabilities")
    print("------------------------------")
    print(capabilities)

    print("\nSelected Capability")
    print("------------------------------")
    print(best)

    print("\nTEST PASSED")
    print("=" * 60)


if __name__ == "__main__":
    main()