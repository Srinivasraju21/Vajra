"""
Task Node

Represents an individual node
inside Vajra's Task Graph.
"""


from dataclasses import dataclass, field

from vajra.planning.planned_task import PlannedTask



@dataclass
class TaskNode:
    """
    Node representation of a planned task.
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
        Add a dependency.

        The current task will wait
        until this dependency completes.
        """

        self.dependencies.append(
            task_node
        )



    def is_ready(self):
        """
        Check whether this task
        can execute.
        """

        return all(
            dependency.completed
            for dependency in self.dependencies
        )