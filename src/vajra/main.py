"""
Vajra Runtime Entry Point

This file starts the Vajra system.

Future runtime responsibilities:
- Initialize Goal Engine
- Load Memory System
- Register Capabilities
- Start Planning Engine
"""


from vajra import __version__

# Import Vajra's first intelligence component
from vajra.core.goal.goal_engine import GoalEngine


def main():
    """
    Main execution function for Vajra runtime.
    """

    # Display Vajra startup information
    print("Project Vajra")
    print(f"Version: {__version__}")
    print("AI-Native Operating Layer initializing...")
    
    print()

    # Initialize the Goal Engine
    goal_engine = GoalEngine()

    # Example user objective
    # Later this will come from:
    # - Text input
    # - Voice input
    # - External applications
    user_input = "Create a project report"

    # Convert user intention into a Vajra Goal
    goal = goal_engine.create_goal(user_input)

    # Display processed goal
    print("Goal received:")
    print(goal.objective)

    print()

    print("Goal status:")
    print(goal.status)


# Start Vajra runtime
if __name__ == "__main__":
    main()