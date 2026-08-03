"""
Vajra Reflection Engine

Analyzes completed executions and
creates insights for adaptive learning.

Flow:

Execution Result

        ↓

Reflection Engine

        ↓

Insight

        ↓

Adaptive Engine
"""


class ReflectionEngine:
    """
    Creates reflections from completed missions.

    Reflection answers:

    - Did the task succeed?
    - What happened?
    - What should Vajra learn?
    """



    def __init__(
        self
    ):
        """
        Initialize reflection storage.
        """


        # Stores all generated reflections.

        self.reflections = []





    def reflect(
        self,
        mission,
        result
    ):
        """
        Analyze execution result.


        Args:

            mission:
                Completed objective


            result:
                Execution output


        Returns:

            Reflection object
        """



        # Determine success.

        success = (

            result.get(
                "success",
                False
            )

        )



        # Create learning insight.

        if success:

            insight = (

                "Mission completed successfully. "
                "Current strategy is effective."

            )

        else:

            insight = (

                "Mission failed. "
                "Strategy requires improvement."

            )



        # Create reflection object.

        reflection = {


            "mission":

                mission,



            "success":

                success,



            "result":

                result,



            "insight":

                insight

        }



        # Store reflection history.

        self.reflections.append(

            reflection

        )



        return reflection





    def get_reflections(
        self
    ):
        """
        Return previous reflections.
        """


        return self.reflections