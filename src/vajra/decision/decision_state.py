"""
Vajra Decision State

Represents the state of an autonomous
decision made by Vajra.
"""


from enum import Enum
import uuid



class DecisionStatus(Enum):
    """
    Decision lifecycle states.
    """

    CREATED = "created"

    ANALYZING = "analyzing"

    SELECTED = "selected"

    EXECUTED = "executed"

    FAILED = "failed"





class DecisionState:
    """
    Represents an autonomous decision.

    Stores decision context,
    options, risks and selection.
    """



    def __init__(
        self,
        goal,
        options=None
    ):
        """
        Initialize decision state.

        Args:

            goal:
                Objective requiring decision

            options:
                Possible actions
        """


        # Unique decision identifier

        self.id = str(
            uuid.uuid4()
        )


        # Decision objective

        self.goal = goal


        # Available choices

        self.options = (

            options

            if options

            else []

        )


        # Selected action

        self.selected_option = None


        # Risk information

        self.risk = None


        # Confidence score

        self.confidence = 0.0


        # Initial status

        self.status = (

            DecisionStatus.CREATED

        )





    def add_option(
        self,
        option
    ):
        """
        Add possible decision option.
        """

        self.options.append(
            option
        )





    def select_option(
        self,
        option,
        confidence=0.0
    ):
        """
        Select final decision.
        """


        self.selected_option = option


        self.confidence = confidence


        self.status = (

            DecisionStatus.SELECTED

        )





    def set_risk(
        self,
        risk
    ):
        """
        Attach risk analysis.
        """

        self.risk = risk





    def mark_executed(
        self
    ):
        """
        Mark decision completed.
        """

        self.status = (

            DecisionStatus.EXECUTED

        )





    def fail(
        self
    ):
        """
        Mark decision failed.
        """

        self.status = (

            DecisionStatus.FAILED

        )





    def get_info(
        self
    ):
        """
        Return decision information.
        """

        return {


            "id":

                self.id,


            "goal":

                self.goal,


            "options":

                self.options,


            "selected_option":

                self.selected_option,


            "risk":

                self.risk,


            "confidence":

                self.confidence,


            "status":

                self.status.value

        }