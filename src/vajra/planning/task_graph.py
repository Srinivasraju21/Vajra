"""
Task Graph

Manages relationships between
Vajra execution tasks.
"""


from vajra.planning.task_node import TaskNode



class TaskGraph:
    """
    Directed Acyclic Graph
    for task execution.
    """



    def __init__(self):

        self.nodes = []



    def add_task(
        self,
        node: TaskNode
    ):
        """
        Add a task node.
        """

        self.nodes.append(
            node
        )



    def get_ready_tasks(self):
        """
        Return tasks that can execute.
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
        Mark task as completed.
        """

        node.completed = True