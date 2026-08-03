"""
Autonomous Execution Loop

Coordinates scheduling,
execution,
learning,
and reliability tracking.
"""

from vajra.core.runtime.execution_scheduler import (
    ExecutionScheduler
)

from vajra.core.runtime.execution_bridge import (
    ExecutionBridge
)

from vajra.core.learning.feedback_manager import (
    FeedbackManager
)

from vajra.core.learning.capability_reliability_manager import (
    CapabilityReliabilityManager
)


class AutonomousExecutionLoop:
    """
    Executes complete plans and
    continuously improves Vajra.
    """

    def __init__(
        self,
        runtime_engine
    ):

        self.runtime = runtime_engine

        self.scheduler = (
            ExecutionScheduler()
        )

        self.bridge = (
            ExecutionBridge(
                runtime_engine
            )
        )

        self.feedback = (
            FeedbackManager(
                runtime_engine.knowledge
            )
        )

        self.reliability = (
            CapabilityReliabilityManager()
        )

    def execute(
        self,
        planned_tasks
    ):
        """
        Execute a complete plan.
        """

        results = []

        self.scheduler.schedule(
            planned_tasks
        )

        while self.scheduler.has_tasks():

            task = (
                self.scheduler.next_task()
            )

            execution_results = (
                self.bridge.execute_task(
                    task
                )
            )

            for result in execution_results:

                results.append(
                    result
                )

                # Learn
                self.feedback.process_feedback(
                    result,
                    source=task.name
                )

                # Update reliability
                self.reliability.record_execution(
                    capability_name=task.name,
                    success=result.success
                )

        return results

    def get_knowledge(self):

        return (
            self.runtime
            .knowledge
            .get_all_knowledge()
        )

    def get_reliability_report(self):

        return (
            self.reliability
            .get_all_statistics()
        )