"""
Risk Model

Defines risk categories
for Vajra operations.
"""

from enum import Enum


class RiskLevel(Enum):
    """
    Defines execution risk.
    """

    READ_ONLY = "read_only"

    REVERSIBLE = "reversible"

    IRREVERSIBLE = "irreversible"

    FINANCIAL = "financial"