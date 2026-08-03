"""
Execution Bridge

Connects Planner tasks
with Runtime execution.
"""


from vajra.core.task.task import Task



class ExecutionBridge:
    """
    Converts planned tasks
    into runtime tasks.
    """


    def __init__(
        self,
        runtime_engine
    ):

        self.runtime_engine = runtime_engine



    def execute_task(
        self,
        planned_task
    ):

        runtime_task = Task(

            capability=
                planned_task.name,

            action=
                planned_task.action,

            parameters=
                planned_task.parameters

        )


        return (
            self.runtime_engine
            .execute(
                [runtime_task]
            )
        )