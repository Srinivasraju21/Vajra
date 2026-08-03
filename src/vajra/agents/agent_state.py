"""
Agent State Management

Defines the lifecycle states
of autonomous Vajra agents.

Every agent inside Vajra moves
through these states during its life.
"""

from enum import Enum


class AgentState(Enum):
    """
    Represents the current state
    of a Vajra autonomous agent.
    """

    # Agent object has been created
    CREATED = "created"

    # Agent is available and waiting for work
    READY = "ready"

    # Agent is currently executing a mission/task
    WORKING = "working"

    # Agent is paused and waiting for input/resource
    WAITING = "waiting"

    # Agent completed assigned work successfully
    COMPLETED = "completed"

    # Agent execution failed
    FAILED = "failed"