"""
Vajra Task Dependency Graph Test
"""



from vajra.orchestration.dependency.task_dependency_graph import (
    TaskDependencyGraph
)





def main():


    print("=" * 60)

    print(
        "VAJRA TASK DEPENDENCY GRAPH TEST"
    )

    print("=" * 60)



    graph = TaskDependencyGraph()



    # Add dependencies


    graph.add_dependency(

        "Implementation",

        "Architecture Design"

    )


    graph.add_dependency(

        "Testing",

        "Implementation"

    )


    graph.add_dependency(

        "Deployment",

        "Testing"

    )



    print()


    print(
        "EXECUTION ORDER"
    )



    order = graph.execution_order()



    for index, task in enumerate(

        order,

        start=1

    ):


        print(

            index,

            "->",

            task

        )



    print()

    print("=" * 60)

    print(
        "TASK DEPENDENCY GRAPH COMPLETE"
    )

    print("=" * 60)





if __name__ == "__main__":

    main()