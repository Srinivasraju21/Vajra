"""
Vajra Risk Analyzer Test
"""


from vajra.decision.risk_analyzer import (
    RiskAnalyzer
)


from vajra.planning.risk import (
    RiskLevel
)





def main():


    print("=" * 60)

    print(
        "VAJRA RISK ANALYZER TEST"
    )

    print("=" * 60)



    analyzer = RiskAnalyzer()



    risks = [

        RiskLevel.READ_ONLY,

        RiskLevel.REVERSIBLE,

        RiskLevel.IRREVERSIBLE,

        RiskLevel.FINANCIAL

    ]



    for risk in risks:


        result = analyzer.analyze(
            risk
        )


        print()

        print(result)



    print()

    print("=" * 60)

    print(
        "RISK ANALYZER COMPLETE"
    )

    print("=" * 60)


   
if __name__ == "__main__":

    main()