"""
Cognitive Logger

Records Vajra's cognitive process including
thoughts, decisions, and execution outcomes.
"""


from datetime import datetime


class CognitiveLogger:
    """
    Maintains cognitive execution traces.
    """

    def __init__(self):
        """
        Initialise cognitive storage.
        """

        self.logs = []


    def log(
        self,
        task,
        thought,
        decision,
        result=None,
    ):
        """
        Store a cognitive trace.

        Parameters:
            task: Task object.
            thought: Thought object.
            decision: Decision result.
            result: Execution result.
        """

        trace = {

            "timestamp": datetime.now(),

            "task": task.action,

            "capability": task.capability,

            "thought": thought.content,

            "confidence": thought.confidence,

            "decision": decision["decision"],

            "approved": decision["approved"],

            "result": result,
        }


        self.logs.append(trace)

        return trace


    def get_logs(self):
        """
        Return all cognitive logs.
        """

        return self.logs


    def clear(self):
        """
        Clear cognitive history.
        """

        self.logs.clear()