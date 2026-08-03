"""
Feedback Manager

Converts execution results into
Knowledge objects and stores them
inside the Knowledge Manager.
"""

from vajra.core.learning.execution_analyzer import (
    ExecutionAnalyzer
)

from vajra.knowledge.base.knowledge import (
    Knowledge
)


class FeedbackManager:
    """
    Processes execution feedback and
    stores learned experiences.
    """

    def __init__(
        self,
        knowledge_manager
    ):
        """
        Initialise Feedback Manager.
        """

        self.knowledge_manager = (
            knowledge_manager
        )

        self.execution_analyzer = (
            ExecutionAnalyzer()
        )

    def process_feedback(
        self,
        result,
        source="runtime"
    ):
        """
        Convert execution result into
        a Knowledge object.
        """

        learning_event = (
            self.execution_analyzer.analyze(
                result
            )
        )

        knowledge = Knowledge(

            knowledge_type="experience",

            source=source,

            content=learning_event["message"],

            confidence=1.0,

            metadata={

                "event":
                    learning_event["event"],

                "status":
                    learning_event["status"],

                "confidence_change":
                    learning_event[
                        "confidence_change"
                    ]
            }
        )

        self.knowledge_manager.add_knowledge(
            knowledge
        )

        return knowledge