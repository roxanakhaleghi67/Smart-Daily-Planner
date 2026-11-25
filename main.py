"""Example usage for the emotion-based task planner.

Run:  python main.py happy
"""

import sys

from smart_planner_app.planner import suggest_tasks


def main() -> None:
    emotion = sys.argv[1] if len(sys.argv) > 1 else "happy"
    for task in suggest_tasks(emotion):
        print(task)


if __name__ == "__main__":
    main()
