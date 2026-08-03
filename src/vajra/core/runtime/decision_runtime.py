"""
Vajra Decision Runtime

Connects autonomous decisions
with runtime execution.
"""


from vajra.decision.decision_engine import (
    DecisionEngine
)


from vajra.planning.risk import (
    RiskLevel
)





class DecisionRuntime:
    """
    Runtime layer that makes decisions
    before executing tasks.
    """



    def __init__(
        self,
        runtime_engine,
        planner
    ):
        """
        Initialize decision runtime.
        """


        self.runtime = runtime_engine


        self.planner = planner


        self.decision_engine = (

            DecisionEngine()

        )





    def execute_goal(
        self,
        goal,
        options,
        risk_level=RiskLevel.READ_ONLY
    ):
        """
        Decide and execute goal.
        """


        # Step 1:
        # Decision making


        decision = (

            self.decision_engine
            .decide(

                goal,

                options,

                risk_level

            )

        )



        selected_action = (

            decision["decision"]
            ["selected_option"]

        )



        # Step 2:
        # Create plan


        plan = (

            self.planner
            .create_plan(

                selected_action

            )

        )



        # Step 3:
        # Execute through runtime


        results = (

            self.runtime
            .execute(

                plan

            )

        )



        return {


            "decision":

                decision,


            "plan":

                plan,


            "results":

                results

        }