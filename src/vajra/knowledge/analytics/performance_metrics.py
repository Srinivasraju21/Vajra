"""
Knowledge Performance Metrics

Measures the quality and reliability
of Vajra's learned knowledge.
"""


class PerformanceMetrics:
    """
    Calculates knowledge performance metrics.
    """

    def __init__(self, knowledge_manager):
        """
        Initialise metrics.

        Parameters:
            knowledge_manager:
                Shared KnowledgeManager instance.
        """

        self.knowledge_manager = knowledge_manager


    def total_items(self):
        """
        Return total knowledge count.
        """

        return len(
            self.knowledge_manager.get_all_knowledge()
        )


    def successful_experiences(self):
        """
        Count successful experiences.
        """

        count = 0

        for knowledge in self.knowledge_manager.get_all_knowledge():

            if (
                knowledge.metadata.get("status")
                == "success"
            ):
                count += 1

        return count


    def failed_experiences(self):
        """
        Count failed experiences.
        """

        count = 0

        for knowledge in self.knowledge_manager.get_all_knowledge():

            if (
                knowledge.metadata.get("status")
                == "failed"
            ):
                count += 1

        return count


    def capability_usage(self):
        """
        Count knowledge by capability source.
        """

        usage = {}

        for knowledge in self.knowledge_manager.get_all_knowledge():

            source = knowledge.source

            if source not in usage:
                usage[source] = 0

            usage[source] += 1

        return usage


    def success_rate(self):
        """
        Calculate success percentage.
        """

        total = (
            self.successful_experiences()
            +
            self.failed_experiences()
        )

        if total == 0:
            return 0


        return (
            self.successful_experiences()
            /
            total
        ) * 100


    def report(self):
        """
        Generate performance report.
        """

        return {
            "total_knowledge": self.total_items(),

            "successful_experiences": (
                self.successful_experiences()
            ),

            "failed_experiences": (
                self.failed_experiences()
            ),

            "success_rate": (
                round(
                    self.success_rate(),
                    2
                )
            ),

            "capability_usage": (
                self.capability_usage()
            ),
        }