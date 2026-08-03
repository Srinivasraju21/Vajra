"""
Capability Selector

Chooses the most reliable capability
from a list of available capabilities.
"""


class CapabilitySelector:

    """
    Selects capabilities using
    reliability scores.
    """

    def __init__(
        self,
        reliability_manager
    ):

        self.reliability_manager = (
            reliability_manager
        )

    def select_best(
        self,
        capabilities
    ):

        if not capabilities:

            return None

        best = None

        best_score = -1

        for capability in capabilities:

            stats = (
                self.reliability_manager
                .get_statistics(
                    capability
                )
            )

            score = stats[
                "reliability"
            ]

            if score > best_score:

                best_score = score

                best = capability

        return best