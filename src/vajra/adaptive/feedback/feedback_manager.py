"""
Vajra Feedback Manager

Responsible for converting execution
results into learning feedback.

Flow:

Execution Result

        ↓

Feedback Analysis

        ↓

Reflection

        ↓

Adaptive Learning
"""





class FeedbackManager:
    """
    Manages execution feedback.

    This module does not execute tasks.

    Its responsibility:

    Observe
       |
       v
    Analyse
       |
       v
    Improve
    """



    def __init__(
        self,
        reflection_engine,
        adaptive_engine
    ):
        """
        Initialize feedback manager.

        Args:

            reflection_engine:
                Creates insights from results


            adaptive_engine:
                Updates learning state
        """


        # Stores reflection component

        self.reflection_engine = (
            reflection_engine
        )


        # Stores adaptive intelligence

        self.adaptive_engine = (
            adaptive_engine
        )





    def process_feedback(
        self,
        mission,
        result
    ):
        """
        Process execution feedback.


        Args:

            mission:
                Completed objective


            result:
                Execution output


        Returns:

            Learning feedback
        """



        # ------------------------------------
        # Step 1:
        # Create reflection
        # ------------------------------------


        reflection = (

            self.reflection_engine
            .reflect(

                mission,

                result

            )

        )



        # ------------------------------------
        # Step 2:
        # Update adaptive intelligence
        # ------------------------------------


        self.adaptive_engine.learn(

            reflection

        )



        # ------------------------------------
        # Step 3:
        # Return learning information
        # ------------------------------------


        return {


            "reflection":

                reflection,


            "learning_updated":

                True

        }