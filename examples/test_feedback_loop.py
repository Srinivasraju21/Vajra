"""
Vajra Feedback Loop Test

Tests:

Execution Result

        ↓

Reflection

        ↓

Learning Update
"""



from vajra.adaptive.feedback.feedback_manager import (
    FeedbackManager
)


from vajra.adaptive.reflection.reflection_engine import (
    ReflectionEngine
)


from vajra.adaptive.adaptive_engine import (
    AdaptiveEngine
)





def main():


    print("=" * 60)

    print(
        "VAJRA FEEDBACK LOOP TEST"
    )

    print("=" * 60)



    reflection_engine = ReflectionEngine()


    adaptive_engine = AdaptiveEngine()



    feedback = FeedbackManager(

        reflection_engine,

        adaptive_engine

    )



    result = feedback.process_feedback(

        mission=
        "Prepare workspace",


        result=
        {
            "success": True,

            "message":
            "Workspace created successfully"

        }

    )



    print()

    print(
        "FEEDBACK RESULT"
    )

    print(result)



    print()

    print(
        "LEARNING STATE"
    )

    print(

        adaptive_engine
        .get_learning_state()

    )



    print()

    print("=" * 60)

    print(
        "FEEDBACK LOOP COMPLETE"
    )

    print("=" * 60)





if __name__ == "__main__":

    main()
    