"""
Vajra Capability Ranker

Ranks capabilities based on
execution performance.
"""



class CapabilityRanker:
    """
    Maintains capability performance scores.
    """



    def __init__(
        self
    ):

        # Stores capability statistics
        self.capabilities = {}



    def record_execution(
        self,
        capability_name,
        success
    ):
        """
        Record capability execution.
        """


        if capability_name not in self.capabilities:

            self.capabilities[capability_name] = {

                "success": 0,

                "failure": 0

            }



        if success:

            self.capabilities[capability_name][
                "success"
            ] += 1


        else:

            self.capabilities[capability_name][
                "failure"
            ] += 1



    def calculate_score(
        self,
        capability_name
    ):
        """
        Calculate capability score.
        """


        data = self.capabilities.get(

            capability_name,

            {

                "success": 0,

                "failure": 0

            }

        )


        total = (

            data["success"]

            +

            data["failure"]

        )


        if total == 0:

            return 0



        return (

            data["success"]

            /

            total

        ) * 100



    def get_ranking(
        self
    ):
        """
        Return ranked capabilities.
        """


        ranking = {}



        for capability in self.capabilities:


            ranking[capability] = (

                self.calculate_score(
                    capability
                )

            )


        return dict(

            sorted(

                ranking.items(),

                key=lambda item:
                item[1],

                reverse=True

            )

        )