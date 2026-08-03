"""
Capability Risk Levels

Defines how much permission a capability requires.
"""

from enum import Enum


class RiskLevel(Enum):
    """
    Risk classification for Vajra capabilities.
    """

    READ_ONLY = "read_only"

    REVERSIBLE = "reversible"

    IRREVERSIBLE = "irreversible"

    FINANCIAL = "financial"