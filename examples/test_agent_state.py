"""
Agent State Example

Demonstrates how Vajra tracks
the lifecycle of autonomous agents.
"""

from vajra.agents.agent_state import AgentState


def main():
    """
    Demonstrate agent states.
    """

    print("Vajra Agent State Demo")
    print("----------------------")

    # Initial agent state
    state = AgentState.CREATED

    print(f"Initial State: {state.value}")

    # Agent becomes ready
    state = AgentState.READY

    print(f"Current State: {state.value}")

    # Agent starts working
    state = AgentState.WORKING

    print(f"Execution State: {state.value}")

    # Agent completes task
    state = AgentState.COMPLETED

    print(f"Final State: {state.value}")


if __name__ == "__main__":
    main()