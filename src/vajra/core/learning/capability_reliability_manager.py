"""
Capability Reliability Manager

Tracks the reliability of each capability
based on execution history.
"""


class CapabilityReliabilityManager:
    """
    Maintains execution statistics for
    every registered capability.
    """

    def __init__(self):
        """
        Initialise reliability storage.
        """

        self.statistics = {}

    def record_execution(
        self,
        capability_name,
        success
    ):
        """
        Record one execution result.
        """

        if capability_name not in self.statistics:

            self.statistics[capability_name] = {

                "success": 0,

                "failure": 0

            }

        if success:

            self.statistics[
                capability_name
            ]["success"] += 1

        else:

            self.statistics[
                capability_name
            ]["failure"] += 1

    def get_statistics(
        self,
        capability_name
    ):
        """
        Return statistics for one capability.
        """

        if capability_name not in self.statistics:

            return {

                "success": 0,

                "failure": 0,

                "reliability": 0.0

            }

        stats = self.statistics[
            capability_name
        ]

        total = (
            stats["success"] +
            stats["failure"]
        )

        if total == 0:

            reliability = 0.0

        else:

            reliability = (
                stats["success"] /
                total
            ) * 100

        return {

            "success": stats["success"],

            "failure": stats["failure"],

            "reliability": round(
                reliability,
                2
            )

        }

    def get_all_statistics(self):
        """
        Return statistics for every capability.
        """

        report = {}

        for capability in self.statistics:

            report[
                capability
            ] = self.get_statistics(
                capability
            )

        return report