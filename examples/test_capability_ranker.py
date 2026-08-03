"""
Vajra Capability Ranker Test
"""


from vajra.adaptive.ranking.capability_ranker import (
    CapabilityRanker
)



def main():


    print("=" * 60)

    print(
        "VAJRA CAPABILITY RANKER TEST"
    )

    print("=" * 60)



    ranker = CapabilityRanker()



    # Filesystem capability

    ranker.record_execution(

        "filesystem",

        True

    )


    ranker.record_execution(

        "filesystem",

        True

    )


    ranker.record_execution(

        "filesystem",

        False

    )



    # Coding capability

    ranker.record_execution(

        "coding",

        True

    )


    ranker.record_execution(

        "coding",

        True

    )


    ranker.record_execution(

        "coding",

        True

    )



    print("\nRanking:")



    print(

        ranker.get_ranking()

    )



    print("=" * 60)

    print(
        "CAPABILITY RANKER COMPLETE"
    )

    print("=" * 60)



if __name__ == "__main__":

    main()