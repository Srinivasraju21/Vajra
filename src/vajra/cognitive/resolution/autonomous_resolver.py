"""
Vajra Autonomous Resolver

Connects goal understanding with
decision intelligence.

Flow:

Goal
 |
 v
Goal Resolver
 |
 v
Options
 |
 v
Decision Engine
 |
 v
Selected Action
"""


from vajra.cognitive.resolution.goal_resolver import (
    GoalResolver
)


from vajra.decision.decision_engine import (
    DecisionEngine
)


from vajra.planning.risk import (
    RiskLevel
)





class AutonomousResolver:
    """
    Complete autonomous reasoning layer.

    Responsibilities:

    1. Understand goal
    2. Generate possible actions
    3. Evaluate actions
    4. Select best action
    """



    def __init__(
        self
    ):
        """
        Initialize autonomous resolver.
        """


        # Goal understanding component

        self.goal_resolver = GoalResolver()



        # Decision making component

        self.decision_engine = DecisionEngine()





    def resolve(
        self,
        goal,
        risk_level=RiskLevel.READ_ONLY
    ):
        """
        Complete autonomous resolution.

        Args:

            goal:
                High level user objective


            risk_level:
                Risk category of operation


        Returns:

            Final decision
        """



        # ------------------------------------------------
        # STEP 1:
        # Convert goal into possible actions
        # ------------------------------------------------


        options = (

            self.goal_resolver
            .resolve(

                goal

            )

        )



        # ------------------------------------------------
        # STEP 2:
        # Ask Decision Engine to select
        # the best action
        # ------------------------------------------------


        decision = (

            self.decision_engine
            .decide(

                goal,

                options,

                risk_level

            )

        )



        # ------------------------------------------------
        # STEP 3:
        # Return complete reasoning result
        # ------------------------------------------------


        return decision