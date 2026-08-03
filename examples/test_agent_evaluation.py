"""
Vajra Phase 7.5.10

Agent Performance Evaluation Test

Tests:

1. Agent creation
2. Recording success/failure
3. Reliability calculation
"""



from vajra.agents.agent import Agent


from vajra.orchestration.evaluation.agent_evaluator import (
    AgentEvaluator
)





def main():


    print("=" * 60)

    print(
        "VAJRA AGENT PERFORMANCE EVALUATION TEST"
    )

    print("=" * 60)





    #
    # Create agents
    #

    research_agent = Agent(

        name="Research Agent",

        purpose="Research information",

        capabilities=[

            "research"

        ]

    )



    execution_agent = Agent(

        name="Execution Agent",

        purpose="Execute tasks",

        capabilities=[

            "execution"

        ]

    )





    #
    # Create evaluator
    #

    evaluator = AgentEvaluator()





    #
    # Record executions
    #

    evaluator.record(

        research_agent,

        True

    )


    evaluator.record(

        research_agent,

        True

    )


    evaluator.record(

        research_agent,

        False

    )





    evaluator.record(

        execution_agent,

        True

    )


    evaluator.record(

        execution_agent,

        True

    )


    evaluator.record(

        execution_agent,

        True

    )





    #
    # Evaluate agents
    #

    print()

    print(
        "RESEARCH AGENT SCORE"
    )


    print(

        evaluator.evaluate(

            research_agent

        )

    )





    print()

    print(
        "EXECUTION AGENT SCORE"
    )


    print(

        evaluator.evaluate(

            execution_agent

        )

    )





    print()

    print(
        "ALL PERFORMANCE DATA"
    )


    print(

        evaluator.get_all_scores()

    )





    print()

    print("=" * 60)

    print(
        "PHASE 7.5.10 PERFORMANCE TEST COMPLETE"
    )

    print("=" * 60)





if __name__ == "__main__":

    main()