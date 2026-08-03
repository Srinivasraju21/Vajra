"""
Autonomous Execution Loop

Coordinates execution between the
Scheduler, Execution Bridge and
Runtime Engine.
"""

from vajra.core.runtime.execution_scheduler import (
    ExecutionScheduler
)

from vajra.core.runtime.execution_bridge import (
    ExecutionBridge
)


class AutonomousExecutionLoop:
    """
    Coordinates execution of a plan.
    """

    def __init__(
        self,
        runtime_engine
    ):

        self.runtime_engine = runtime_engine

        self.scheduler = (
            ExecutionScheduler()
        )

        self.bridge = (
            ExecutionBridge(
                runtime_engine
            )
        )

    def execute(
        self,
        planned_tasks
    ):
        """
        Execute a complete plan.

        Parameters
        ----------
        planned_tasks : list

        Returns
        -------
        list
            Execution results.
        """

        execution_results = []

        self.scheduler.schedule(
            planned_tasks
        )

        while self.scheduler.has_tasks():

            task = (
                self.scheduler.next_task()
            )

            result = (
                self.bridge.execute_task(
                    task
                )
            )

            execution_results.extend(
                result
            )

        return execution_results