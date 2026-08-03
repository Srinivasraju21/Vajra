"""
Vajra Strategy Manager

Maintains and selects execution strategies
based on historical performance.
"""



class StrategyManager:
    """
    Manages adaptive execution strategies.
    """



    def __init__(
        self
    ):

        # Strategy performance storage
        self.strategies = {}



    def register_strategy(
        self,
        strategy_name
    ):
        """
        Register a new strategy.
        """


        if strategy_name not in self.strategies:


            self.strategies[strategy_name] = {

                "success": 0,

                "failure": 0

            }



    def record_result(
        self,
        strategy_name,
        success
    ):
        """
        Record strategy outcome.
        """


        self.register_strategy(
            strategy_name
        )


        if success:

            self.strategies[strategy_name][
                "success"
            ] += 1


        else:

            self.strategies[strategy_name][
                "failure"
            ] += 1



    def get_strategy_score(
        self,
        strategy_name
    ):
        """
        Calculate strategy score.
        """


        data = self.strategies.get(

            strategy_name,

            {

                "success": 0,

                "failure": 0

            }

        )


        total = (

            data["success"]

            +

            data["failure"]

        )


        if total == 0:

            return 0



        return (

            data["success"]

            /

            total

        ) * 100



    def recommend_strategy(
        self
    ):
        """
        Return best performing strategy.
        """


        if not self.strategies:

            return None



        scores = {}


        for strategy in self.strategies:


            scores[strategy] = (

                self.get_strategy_score(
                    strategy
                )

            )


        return max(

            scores,

            key=scores.get

        )



    def get_all_strategies(
        self
    ):
        """
        Return strategy statistics.
        """

        return self.strategies
    