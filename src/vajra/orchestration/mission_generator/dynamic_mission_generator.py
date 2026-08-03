"""
Vajra Dynamic Mission Generator

Creates Mission objects automatically
from decomposed objectives.

Flow:

Objective

    ↓

Decomposition

    ↓

Mission Generation

    ↓

Mission Lifecycle
"""



from vajra.orchestration.mission import (
    Mission
)





class DynamicMissionGenerator:
    """
    Generates Vajra missions dynamically.

    Responsibilities:

    1. Receive sub objectives
    2. Create Mission objects
    3. Prepare missions for agents
    """



    def __init__(
        self
    ):
        """
        Initialize mission generator.
        """



        # Stores generated missions.

        # This allows future tracking,
        # monitoring and recovery.

        self.missions = []





    def generate(
        self,
        objectives
    ):
        """
        Convert objectives into missions.


        Args:

            objectives:
                List of sub objectives


        Returns:

            List of Mission objects
        """



        generated = []



        # Create one mission
        # for every objective.

        for objective in objectives:



            mission = Mission(

                name=objective,

                objective=objective

            )



            # Store internally

            self.missions.append(

                mission

            )



            # Add to current batch

            generated.append(

                mission

            )



        return generated





    def get_missions(
        self
    ):
        """
        Return generated missions.
        """

        return self.missions