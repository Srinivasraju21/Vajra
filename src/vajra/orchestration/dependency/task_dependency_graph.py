"""
Vajra Task Dependency Graph

Maintains relationships between tasks.

A task can depend on another task.

Example:

Architecture

      ↓

Development

      ↓

Testing


The graph helps Vajra determine
execution order.
"""





class TaskDependencyGraph:
    """
    Directed dependency graph
    for Vajra tasks.
    """



    def __init__(
        self
    ):
        """
        Initialize graph.
        """


        # Stores task dependencies.

        # Format:

        # {
        #    task:
        #       [
        #          dependency tasks
        #       ]
        # }

        self.dependencies = {}





    def add_task(
        self,
        task
    ):
        """
        Add a new task node.
        """



        if task not in self.dependencies:


            self.dependencies[task] = []





    def add_dependency(
        self,
        task,
        depends_on
    ):
        """
        Create dependency relation.


        Example:


        Development

              depends on

        Architecture
        """



        # Ensure both tasks exist.

        self.add_task(

            task

        )


        self.add_task(

            depends_on

        )



        # Add relationship.

        self.dependencies[task].append(

            depends_on

        )





    def get_dependencies(
        self,
        task
    ):
        """
        Return prerequisites
        for a task.
        """



        return (

            self.dependencies
            .get(
                task,
                []
            )

        )





    def execution_order(
        self
    ):
        """
        Calculate execution order.

        Uses topological sorting.

        Tasks with no dependencies
        execute first.
        """



        graph = {

            task:list(deps)

            for task, deps

            in self.dependencies.items()

        }



        order = []



        while graph:



            ready = [

                task

                for task, deps

                in graph.items()

                if len(deps) == 0

            ]



            if not ready:


                raise Exception(

                    "Circular dependency detected"

                )



            for task in ready:


                order.append(

                    task

                )


                del graph[task]



            for deps in graph.values():


                for task in ready:


                    if task in deps:


                        deps.remove(task)



        return order