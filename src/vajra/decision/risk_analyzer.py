"""
Vajra Risk Analyzer

Evaluates decision risk before
autonomous execution.
"""


from vajra.planning.risk import (
    RiskLevel
)





class RiskAnalyzer:
    """
    Analyzes risk associated
    with possible decisions.
    """



    def __init__(
        self
    ):
        """
        Initialize analyzer.
        """


        # Risk priority order

        self.risk_priority = {


            RiskLevel.READ_ONLY:
                1,


            RiskLevel.REVERSIBLE:
                2,


            RiskLevel.IRREVERSIBLE:
                3,


            RiskLevel.FINANCIAL:
                4

        }





    def analyze(
        self,
        risk_level
    ):
        """
        Analyze a risk level.

        Returns risk assessment.
        """



        severity = (

            self.risk_priority
            .get(
                risk_level,
                0
            )

        )



        if severity == 1:


            recommendation = (
                "Safe to execute automatically."
            )


            approval = False



        elif severity == 2:


            recommendation = (
                "Execute with monitoring."
            )


            approval = False



        elif severity == 3:


            recommendation = (
                "Requires confirmation before execution."
            )


            approval = True



        elif severity == 4:


            recommendation = (
                "Requires explicit user approval."
            )


            approval = True



        else:


            recommendation = (
                "Unknown risk."
            )


            approval = True





        return {


            "risk":

                risk_level.value,


            "severity":

                severity,


            "requires_confirmation":

                approval,


            "recommendation":

                recommendation

        }





    def compare(
        self,
        risk_a,
        risk_b
    ):
        """
        Compare two risks.

        Returns higher risk.
        """



        value_a = (

            self.risk_priority
            .get(
                risk_a,
                0
            )

        )



        value_b = (

            self.risk_priority
            .get(
                risk_b,
                0
            )

        )



        if value_a >= value_b:

            return risk_a



        return risk_b
    