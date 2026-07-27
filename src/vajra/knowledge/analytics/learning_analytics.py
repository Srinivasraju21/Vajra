"""
Learning Analytics

Analyses Vajra's accumulated knowledge
and provides learning insights.
"""


class LearningAnalytics:
    """
    Provides statistics and insights
    from stored knowledge.
    """

    def __init__(self, knowledge_manager):
        """
        Initialise analytics.

        Parameters:
            knowledge_manager:
                Shared KnowledgeManager instance.
        """

        self.knowledge_manager = knowledge_manager


    def total_knowledge(self):
        """
        Return total number of knowledge items.
        """

        return len(
            self.knowledge_manager.get_all_knowledge()
        )


    def count_by_type(self):
        """
        Count knowledge grouped by type.
        """

        statistics = {}

        for knowledge in self.knowledge_manager.get_all_knowledge():

            knowledge_type = knowledge.knowledge_type

            if knowledge_type not in statistics:

                statistics[knowledge_type] = 0

            statistics[knowledge_type] += 1

        return statistics


    def average_confidence(self):
        """
        Calculate average confidence score.
        """

        knowledge_items = (
            self.knowledge_manager.get_all_knowledge()
        )

        if not knowledge_items:
            return 0


        total = sum(
            item.confidence
            for item in knowledge_items
        )

        return total / len(knowledge_items)


    def generate_report(self):
        """
        Generate learning report.
        """

        return {
            "total_knowledge": self.total_knowledge(),

            "knowledge_types": self.count_by_type(),

            "average_confidence": (
                round(
                    self.average_confidence(),
                    2
                )
            ),
        }