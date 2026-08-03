"""
Vajra Option Selector

Selects the best decision option
based on intelligence signals.
"""


class OptionSelector:
    """
    Chooses the best option from
    available decisions.
    """



    def __init__(
        self
    ):
        """
        Initialize selector.
        """

        self.history = {}





    def register_success(
        self,
        option
    ):
        """
        Record successful option usage.
        """

        if option not in self.history:

            self.history[option] = 0


        self.history[option] += 1





    def calculate_score(
        self,
        option,
        risk_score=0,
        reliability_score=0,
        strategy_score=0
    ):
        """
        Calculate option score.

        Higher score means better option.
        """


        success_score = (

            self.history
            .get(
                option,
                0
            )

        )



        total_score = (

            success_score
            +
            reliability_score
            +
            strategy_score
            -
            risk_score

        )


        return total_score





    def select(
        self,
        options,
        risk_scores=None,
        reliability_scores=None,
        strategy_scores=None
    ):
        """
        Select highest scoring option.
        """



        risk_scores = (

            risk_scores
            if risk_scores
            else {}

        )


        reliability_scores = (

            reliability_scores
            if reliability_scores
            else {}

        )


        strategy_scores = (

            strategy_scores
            if strategy_scores
            else {}

        )



        best_option = None

        best_score = float(
            "-inf"
        )



        for option in options:


            score = self.calculate_score(

                option,

                risk_scores.get(
                    option,
                    0
                ),

                reliability_scores.get(
                    option,
                    0
                ),

                strategy_scores.get(
                    option,
                    0
                )

            )



            if score > best_score:

                best_score = score

                best_option = option





        return {


            "selected_option":

                best_option,


            "score":

                best_score

        }
    