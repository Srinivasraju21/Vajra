"""
Vajra Adaptive Intelligence Engine

Coordinates reflection,
capability ranking,
and strategy learning.
"""


from vajra.adaptive.reflection.reflection_engine import (
    ReflectionEngine
)


from vajra.adaptive.ranking.capability_ranker import (
    CapabilityRanker
)


from vajra.adaptive.strategy.strategy_manager import (
    StrategyManager
)



class AdaptiveEngine:
    """
    Central adaptive intelligence layer.

    Learns from mission execution
    and improves future decisions.
    """



    def __init__(
        self
    ):
        """
        Initialize adaptive components.
        """


        # Analyzes mission outcomes
        self.reflection_engine = (

            ReflectionEngine()

        )


        # Tracks agent/capability performance
        self.capability_ranker = (

            CapabilityRanker()

        )


        # Stores and evaluates strategies
        self.strategy_manager = (

            StrategyManager()

        )



    def learn_from_mission(
        self,
        mission
    ):
        """
        Learn from completed mission.

        Flow:

        Mission Result
              |
              ↓
        Reflection
              |
              ↓
        Ranking Update
              |
              ↓
        Strategy Update
        """


        # Generate reflection

        reflection = (

            self.reflection_engine
            .reflect(
                mission
            )

        )


        success = (

            reflection["success"]

        )



        # Update capability performance

        for agent in mission.agents:


            self.capability_ranker.record_execution(

                capability_name=

                agent.name,


                success=

                success

            )



        # Update strategy performance

        self.strategy_manager.record_result(

            strategy_name=

            "default_strategy",


            success=

            success

        )


        return reflection



    def get_learning_state(
        self
    ):
        """
        Return current adaptive intelligence state.

        Includes:

        - Reflection history
        - Capability rankings
        - Strategy performance
        """


        return {

            "reflections":

                self.reflection_engine
                .get_reflections(),


            "capability_ranking":

                self.capability_ranker
                .get_ranking(),


            "strategies":

                self.strategy_manager
                .get_all_strategies()

        }