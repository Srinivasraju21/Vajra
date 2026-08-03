"""
Vajra Decision Planner

Connects autonomous decisions
with the planning layer.
"""


from vajra.decision.decision_engine import (
    DecisionEngine
)





class DecisionPlanner:
    """
    Planner extension that uses
    autonomous decision making.
    """



    def __init__(
        self,
        planner
    ):
        """
        Initialize decision planner.

        Args:

            planner:
                Existing Vajra planner
        """


        self.planner = planner


        self.decision_engine = (

            DecisionEngine()

        )





    def create_plan(
        self,
        goal,
        options,
        risk_level
    ):
        """
        Make decision and create plan.
        """


        # Step 1:
        # Decide best action


        decision_result = (

            self.decision_engine
            .decide(

                goal,

                options,

                risk_level

            )

        )



        selected_action = (

            decision_result
            ["decision"]
            ["selected_option"]

        )



        # Step 2:
        # Send selected action
        # to existing planner


        plan = (

            self.planner
            .create_plan(

                selected_action

            )

        )



        return {


            "decision":

                decision_result,


            "plan":

                plan

        }