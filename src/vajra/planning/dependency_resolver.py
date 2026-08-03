"""
Dependency Resolver

Analyzes Task Graph dependencies
and determines executable tasks.
"""


from vajra.planning.task_graph import TaskGraph



class DependencyResolver:
    """
    Resolves task execution order
    from a Task Graph.
    """


    def __init__(
        self,
        task_graph: TaskGraph
    ):
        """
        Initialize resolver.

        Parameters:
            task_graph:
                Vajra TaskGraph instance
        """

        self.task_graph = task_graph



    def get_executable_tasks(self):
        """
        Return tasks that are ready
        for execution.
        """

        return (
            self.task_graph
            .get_ready_tasks()
        )



    def get_blocked_tasks(self):
        """
        Return tasks waiting
        for dependencies.
        """

        blocked = []


        for node in self.task_graph.nodes:

            if (
                not node.completed
                and not node.is_ready()
            ):
                blocked.append(node)


        return blocked



    def has_pending_tasks(self):
        """
        Check whether unfinished
        tasks remain.
        """

        return any(
            not node.completed
            for node in self.task_graph.nodes
        )
    