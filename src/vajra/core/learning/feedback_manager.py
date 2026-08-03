"""
Feedback Manager

Connects execution feedback
with Vajra knowledge system.
"""


from vajra.core.learning.execution_analyzer import (
    ExecutionAnalyzer
)



class FeedbackManager:
    """
    Manages execution feedback
    and learning updates.
    """


    def __init__(
        self,
        knowledge_manager
    ):
        """
        Initialize feedback manager.
        """

        self.knowledge_manager = (
            knowledge_manager
        )

        self.analyzer = (
            ExecutionAnalyzer()
        )



    def process_feedback(
        self,
        result,
        source="runtime"
    ):
        """
        Process execution result
        and store learning experience.
        """


        learning_event = (
            self.analyzer
            .analyze(result)
        )


        self.knowledge_manager.add_knowledge(

            learning_event,

            source

        )


        return learning_event