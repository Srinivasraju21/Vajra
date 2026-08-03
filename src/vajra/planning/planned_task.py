"""
Planned Task

Represents a task generated
by Vajra Planner.
"""


from vajra.planning.risk import RiskLevel



class PlannedTask:
    """
    Represents an executable planned task.
    """


    def __init__(
        self,
        name,
        risk,
        action=None,
        parameters=None
    ):
        """
        Initialize planned task.
        """

        self.name = name

        self.risk = risk

        self.action = action

        self.parameters = (
            parameters
            if parameters
            else {}
        )

        self.status = "pending"



    def __repr__(self):

        return (
            f"PlannedTask("
            f"name='{self.name}', "
            f"action='{self.action}', "
            f"risk={self.risk}, "
            f"status='{self.status}'"
            f")"
        )