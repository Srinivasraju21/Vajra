"""
Vajra Real-Time Intelligence Demo

Demonstrates:
- Task execution
- Cognitive reasoning
- Working memory
- Knowledge integration
- Learning analytics
"""


from vajra.core.runtime.runtime_engine import RuntimeEngine
from vajra.core.task.task import Task

from vajra.knowledge.analytics.learning_analytics import (
    LearningAnalytics
)

from vajra.knowledge.analytics.performance_metrics import (
    PerformanceMetrics
)



def main():

    print("=" * 60)
    print(" VAJRA v0.5.0 REAL-TIME INTELLIGENCE DEMO ")
    print("=" * 60)



    # ---------------------------------
    # Initialize Vajra
    # ---------------------------------

    runtime = RuntimeEngine()

    print("\n[BOOT]")
    print("Runtime Engine initialized")
    print("Memory Manager loaded")
    print("Knowledge Manager loaded")
    print("Reasoning Engine loaded")



    # ---------------------------------
    # Create Task
    # ---------------------------------

    task = Task(
        capability="filesystem",
        action="create_directory",
        parameters={
            "directory_name":
            "vajra_realtime_demo"
        },
    )


    print("\n[TASK]")
    print(task)



    # ---------------------------------
    # Execute Task
    # ---------------------------------

    print("\n[EXECUTION]")

    result = runtime.execute(
        [task]
    )


    print(result)



    # ---------------------------------
    # Working Memory
    # ---------------------------------

    print("\n[WORKING MEMORY]")

    memories = (
        runtime.get_execution_history()
    )


    for memory in memories:

        print(memory)



    # ---------------------------------
    # Learning Analytics
    # ---------------------------------

    print("\n[LEARNING ANALYTICS]")


    analytics = LearningAnalytics(
        runtime.knowledge
    )


    print(
        analytics.generate_report()
    )



    # ---------------------------------
    # Performance Metrics
    # ---------------------------------

    print("\n[PERFORMANCE METRICS]")


    metrics = PerformanceMetrics(
        runtime.knowledge
    )


    print(
        metrics.report()
    )



    print("\n" + "=" * 60)
    print(" VAJRA DEMO COMPLETED ")
    print("=" * 60)



if __name__ == "__main__":

    main()