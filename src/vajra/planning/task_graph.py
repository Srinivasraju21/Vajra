"""
Task Graph

Maintains relationships between
Vajra execution tasks.
"""

from vajra.planning.task_node import TaskNode


class TaskGraph:
    """
    Directed Acyclic Graph (DAG)
    used for task execution planning.
    """


    def __init__(self):

        self.nodes = []


    def add_task(
        self,
        node: TaskNode
    ):
        """
        Add a task node into graph.
        """

        self.nodes.append(
            node
        )


    def get_ready_tasks(self):
        """
        Return tasks that are ready
        for execution.
        """

        return [
            node
            for node in self.nodes
            if not node.completed
            and node.is_ready()
        ]


    def mark_completed(
        self,
        node: TaskNode
    ):
        """
        Mark task execution completed.
        """

        node.completed = True