"""
Execution Analyzer

Analyzes capability execution results
and converts them into learning events.
"""


class ExecutionAnalyzer:
    """
    Analyzes execution outcomes.
    """


    def analyze(self, result):
        """
        Analyze a CapabilityResult object.

        Returns structured learning data.
        """


        if result.success:

            return {

                "event": "execution",

                "status": "success",

                "message": result.message,

                "confidence_change": 0.05

            }


        else:

            return {

                "event": "execution",

                "status": "failed",

                "message": result.message,

                "confidence_change": -0.05

            }