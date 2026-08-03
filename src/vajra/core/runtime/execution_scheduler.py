"""
Execution Scheduler

Determines the order in which
planned tasks should be executed.
"""


class ExecutionScheduler:
    """
    Simple execution scheduler.

    Currently executes tasks in the
    order they are received.

    Future versions will support:

    - Priority scheduling
    - Parallel execution
    - Retry queues
    - Time-based scheduling
    """

    def __init__(self):
        """
        Initialise scheduler.
        """

        self.execution_queue = []

    def schedule(
        self,
        planned_tasks
    ):
        """
        Build an execution queue.

        Parameters
        ----------
        planned_tasks : list
            List of PlannedTask objects.

        Returns
        -------
        list
            Ordered execution queue.
        """

        self.execution_queue = []

        for task in planned_tasks:

            self.execution_queue.append(
                task
            )

        return self.execution_queue

    def next_task(self):
        """
        Return the next task.

        Returns
        -------
        PlannedTask | None
        """

        if not self.execution_queue:

            return None

        return self.execution_queue.pop(0)

    def has_tasks(self):
        """
        Returns True if tasks remain.
        """

        return len(
            self.execution_queue
        ) > 0

    def clear(self):
        """
        Clear scheduler queue.
        """

        self.execution_queue.clear()