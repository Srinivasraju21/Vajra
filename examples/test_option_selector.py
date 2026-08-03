"""
Vajra Option Selector Test
"""


from vajra.decision.option_selector import (
    OptionSelector
)




def main():


    print("=" * 60)

    print(
        "VAJRA OPTION SELECTOR TEST"
    )

    print("=" * 60)



    selector = OptionSelector()



    # Previous successful strategy

    selector.register_success(

        "use_filesystem_cleanup"

    )



    options = [

        "use_filesystem_cleanup",

        "delete_application",

        "manual_cleanup"

    ]



    result = selector.select(

        options,

        risk_scores={

            "use_filesystem_cleanup":1,

            "delete_application":4,

            "manual_cleanup":2

        },

        reliability_scores={

            "use_filesystem_cleanup":5,

            "delete_application":2,

            "manual_cleanup":3

        },

        strategy_scores={

            "use_filesystem_cleanup":4,

            "delete_application":1,

            "manual_cleanup":2

        }

    )



    print()

    print(result)



    print()

    print("=" * 60)

    print(
        "OPTION SELECTOR COMPLETE"
    )

    print("=" * 60)





if __name__ == "__main__":

    main()