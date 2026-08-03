"""
Execution Scheduler

Controls the order and availability
of task execution inside Vajra.

The scheduler does not execute tasks.
It prepares tasks for the Runtime Engine.
"""


from vajra.planning.dependency_resolver import (
    DependencyResolver
)



class ExecutionScheduler:
    """
    Responsible for selecting
    executable tasks from the task graph.
    """


    def __init__(
        self,
        resolver: DependencyResolver
    ):
        """
        Initialize scheduler.

        Parameters:

            resolver:
                DependencyResolver instance
                responsible for understanding
                task dependencies.
        """

        # Store dependency resolver.
        # Scheduler uses this information
        # to know which tasks are ready.
        self.resolver = resolver


    def get_next_tasks(self):
        """
        Returns tasks that are ready
        for execution.
        """

        return (
            self.resolver
            .get_executable_tasks()
        )


    def has_pending_tasks(self):
        """
        Checks whether unfinished
        tasks remain.
        """

        return (
            self.resolver
            .has_pending_tasks()
        )