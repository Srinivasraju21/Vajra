"""
Vajra Reflection Engine

Analyzes mission outcomes
and generates learning feedback.
"""



class ReflectionEngine:
    """
    Evaluates completed missions.

    Converts execution results
    into learning insights.
    """



    def __init__(self):

        # Store reflection history
        self.reflections = []



    def reflect(
        self,
        mission
    ):
        """
        Analyze mission outcome.
        """


        success = (

            mission.state.value
            ==
            "completed"

        )


        reflection = {

            "mission":
                mission.name,


            "objective":
                mission.objective,


            "success":
                success,


            "agents":

                [
                    agent.name
                    for agent
                    in mission.agents
                ],


            "results":
                mission.results,


            "insight":

                self.generate_insight(
                    success
                )

        }


        self.reflections.append(
            reflection
        )


        return reflection



    def generate_insight(
        self,
        success
    ):
        """
        Generate learning message.
        """


        if success:

            return (
                "Mission completed successfully. "
                "Current strategy is effective."
            )


        return (

            "Mission failed. "
            "Strategy improvement required."

        )



    def get_reflections(
        self
    ):
        """
        Return previous reflections.
        """

        return self.reflections