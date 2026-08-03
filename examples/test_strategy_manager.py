"""
Vajra Strategy Manager Test
"""


from vajra.adaptive.strategy.strategy_manager import (
    StrategyManager
)



def main():


    print("=" * 60)

    print(
        "VAJRA STRATEGY MANAGER TEST"
    )

    print("=" * 60)



    manager = StrategyManager()



    # Strategy 1

    manager.record_result(

        "parallel_execution",

        True

    )


    manager.record_result(

        "parallel_execution",

        True

    )


    manager.record_result(

        "parallel_execution",

        False

    )



    # Strategy 2

    manager.record_result(

        "sequential_execution",

        True

    )


    manager.record_result(

        "sequential_execution",

        True

    )


    manager.record_result(

        "sequential_execution",

        True

    )



    print("\nStrategies:")


    print(

        manager.get_all_strategies()

    )



    print("\nRecommended Strategy:")


    print(

        manager.recommend_strategy()

    )



    print("=" * 60)

    print(
        "STRATEGY MANAGER COMPLETE"
    )

    print("=" * 60)



if __name__ == "__main__":

    main()