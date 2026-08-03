"""
Task Node

Represents an individual task
inside Vajra's execution graph.
"""

from dataclasses import dataclass, field

from vajra.planning.planned_task import PlannedTask


@dataclass
class TaskNode:
    """
    Represents a node in the Task Graph.
    """

    task: PlannedTask

    dependencies: list["TaskNode"] = field(
        default_factory=list
    )

    completed: bool = False


    def add_dependency(
        self,
        task_node: "TaskNode"
    ):
        """
        Add dependency relationship.

        The current task waits until
        the dependency completes.
        """

        self.dependencies.append(
            task_node
        )


    def is_ready(self):
        """
        Check if task can execute.

        A task is ready only when
        all dependencies are completed.
        """

        return all(
            dependency.completed
            for dependency in self.dependencies
        )