"""
Vajra Orchestration Memory

Stores mission execution history.

This connects:

Orchestration Layer

        ↓

Adaptive Learning Layer
"""





class OrchestrationMemory:
    """
    Maintains historical mission
    execution information.
    """



    def __init__(self):
        """
        Initialize memory storage.
        """


        # Stores completed missions.

        self.missions = []





    def store(
        self,
        mission_result
    ):
        """
        Store completed mission.
        """

        self.missions.append(

            mission_result

        )





    def get_history(
        self
    ):
        """
        Return mission history.
        """

        return self.missions





    def get_statistics(
        self
    ):
        """
        Basic execution statistics.
        """



        total = len(

            self.missions

        )



        completed = len(

            [

                mission

                for mission in self.missions

                if mission.get(
                    "status"
                )
                ==
                "completed"

            ]

        )



        return {



            "total_missions":

                total,



            "completed":

                completed,



            "success_rate":

                (

                    completed / total

                    if total

                    else 0

                )

        }