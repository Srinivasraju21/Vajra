"""
Vajra Agent Performance Evaluator

Tracks and evaluates autonomous
agent performance.

Responsibilities:

1. Record agent execution results
2. Track success/failure history
3. Calculate reliability score
4. Provide evaluation data
"""





class AgentEvaluator:
    """
    Evaluates performance of Vajra agents.
    """



    def __init__(
        self
    ):
        """
        Initialize evaluator storage.
        """


        # Stores performance data
        # for every agent.

        self.performance = {}





    def record(
        self,
        agent,
        success
    ):
        """
        Record execution outcome
        of an agent.


        Args:

            agent:
                Agent object


            success:
                True if execution succeeded
                False if execution failed
        """



        # Create tracking entry
        # for new agents.

        if agent.name not in self.performance:


            self.performance[agent.name] = {


                "success":

                    0,


                "failure":

                    0


            }





        # Update counters.

        if success:


            self.performance[agent.name][
                "success"
            ] += 1


        else:


            self.performance[agent.name][
                "failure"
            ] += 1





    def evaluate(
        self,
        agent
    ):
        """
        Calculate agent reliability.


        Returns:

            Agent performance statistics
        """



        # Retrieve agent history.

        data = self.performance.get(

            agent.name,

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





        # Calculate success percentage.

        success_rate = (

            data["success"]

            /

            total

            if total

            else 0

        )





        return {


            "agent":

                agent.name,


            "successful_tasks":

                data["success"],


            "failed_tasks":

                data["failure"],


            "success_rate":

                success_rate


        }





    def get_all_scores(
        self
    ):
        """
        Return all agent performance data.
        """

        return self.performance