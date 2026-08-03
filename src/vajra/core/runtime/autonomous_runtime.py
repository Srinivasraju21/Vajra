"""
Vajra Autonomous Runtime

Complete autonomous execution pipeline.

This module connects:

Goal Understanding
        |
        v
Decision Intelligence
        |
        v
Planning
        |
        v
Runtime Execution


This is the bridge between
thinking and doing.
"""



from vajra.cognitive.resolution.autonomous_resolver import (
    AutonomousResolver
)



from vajra.core.planner.planner import (
    Planner
)





class AutonomousRuntime:
    """
    Complete autonomous execution system.

    Responsibilities:

    1. Receive user goal
    2. Resolve possible actions
    3. Select best action
    4. Create execution plan
    5. Execute through runtime
    """



    def __init__(
        self,
        runtime_engine
    ):
        """
        Initialize autonomous runtime.


        Args:

            runtime_engine:
                Existing Vajra runtime
        """



        # Intelligence layer

        self.resolver = AutonomousResolver()



        # Planning layer

        self.planner = Planner()



        # Execution layer

        self.runtime = runtime_engine





    def execute(
        self,
        goal
    ):
        """
        Execute a complete autonomous goal.


        Flow:

        Goal

        ↓

        Resolve

        ↓

        Plan

        ↓

        Execute

        """



        # -----------------------------------------
        # STEP 1:
        # Understand goal and make decision
        # -----------------------------------------


        decision = (

            self.resolver
            .resolve(

                goal

            )

        )



        # Selected action

        action = (

            decision["decision"]
            ["selected_option"]

        )



        # -----------------------------------------
        # STEP 2:
        # Convert decision into tasks
        # -----------------------------------------


        plan = (

            self.planner
            .create_plan(

                action

            )

        )



        # -----------------------------------------
        # STEP 3:
        # Execute generated plan
        # -----------------------------------------


        result = (

            self.runtime
            .execute(

                plan

            )

        )



        return {


            "goal":

                goal,


            "decision":

                decision,


            "plan":

                plan,


            "execution":

                result

        }