"""
Vajra Decision Engine

Central intelligence layer responsible
for autonomous decision making.
"""


from vajra.decision.decision_state import (
    DecisionState
)


from vajra.decision.risk_analyzer import (
    RiskAnalyzer
)


from vajra.decision.option_selector import (
    OptionSelector
)





class DecisionEngine:
    """
    Coordinates autonomous decisions.
    """



    def __init__(
        self
    ):
        """
        Initialize decision engine.
        """


        self.risk_analyzer = (

            RiskAnalyzer()

        )


        self.option_selector = (

            OptionSelector()

        )





    def create_decision(
        self,
        goal,
        options
    ):
        """
        Create new decision.
        """


        decision = DecisionState(

            goal,

            options

        )


        return decision





    def evaluate_risk(
        self,
        decision,
        risk_level
    ):
        """
        Analyze decision risk.
        """


        analysis = (

            self.risk_analyzer
            .analyze(
                risk_level
            )

        )


        decision.set_risk(

            analysis

        )


        return analysis





    def select_action(
        self,
        decision,
        risk_scores=None,
        reliability_scores=None,
        strategy_scores=None
    ):
        """
        Select best option.
        """


        result = (

            self.option_selector
            .select(

                decision.options,

                risk_scores,

                reliability_scores,

                strategy_scores

            )

        )


        decision.select_option(

            result["selected_option"],

            confidence=

            result["score"]

        )


        return result





    def decide(
        self,
        goal,
        options,
        risk_level,
        risk_scores=None,
        reliability_scores=None,
        strategy_scores=None
    ):
        """
        Complete autonomous decision flow.
        """


        decision = (

            self.create_decision(

                goal,

                options

            )

        )



        self.evaluate_risk(

            decision,

            risk_level

        )



        selection = (

            self.select_action(

                decision,

                risk_scores,

                reliability_scores,

                strategy_scores

            )

        )



        return {


            "decision":

                decision.get_info(),


            "selection":

                selection

        }