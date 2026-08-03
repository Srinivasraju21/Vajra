"""
Vajra Adaptive Intelligence Engine

Coordinates reflection,
ranking and strategy learning.
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
    Central intelligence layer
    responsible for learning.
    """



    def __init__(
        self
    ):

        self.reflection = (
            ReflectionEngine()
        )


        self.ranker = (
            CapabilityRanker()
        )


        self.strategy = (
            StrategyManager()
        )



    def learn_from_mission(
        self,
        mission
    ):
        """
        Learn from completed mission.
        """


        # Generate reflection

        reflection = (

            self.reflection.reflect(
                mission
            )

        )



        # Update agent performance

        for agent in mission.agents:


            self.ranker.record_execution(

                capability_name=
                agent.name,


                success=
                reflection["success"]

            )



        # Update strategy

        self.strategy.record_result(

            strategy_name=
            "default_strategy",


            success=
            reflection["success"]

        )



        return reflection



    def get_recommendation(
        self
    ):
        """
        Provide future strategy.
        """


        return {

            "best_strategy":
                self.strategy
                .recommend_strategy(),


            "capability_ranking":
                self.ranker
                .get_ranking()

        }