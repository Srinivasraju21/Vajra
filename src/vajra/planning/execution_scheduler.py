"""
Execution Scheduler

Controls the order and availability
of task execution inside Vajra.

The scheduler prepares tasks
for the Runtime Engine.
"""


from vajra.planning.dependency_resolver import (
    DependencyResolver
)



class ExecutionScheduler:
    """
    Selects tasks that are ready
    for execution.
    """


    def __init__(
        self,
        resolver: DependencyResolver
    ):
        """
        Initialize scheduler.

        Parameters:
            resolver:
                DependencyResolver instance.
        """

        # Scheduler depends on the resolver
        # to understand task dependencies
        # and execution readiness.
        self.resolver = resolver



    def get_next_tasks(self):
        """
        Returns tasks that are ready
        to execute.
        """

        return (
            self.resolver
            .get_executable_tasks()
        )



    def has_pending_tasks(self):
        """
        Checks whether unfinished
        tasks exist.
        """

        return (
            self.resolver
            .has_pending_tasks()
        )