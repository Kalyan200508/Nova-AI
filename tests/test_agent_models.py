from agent.models import Goal
from agent.models import Task

goal = Goal(
    text="Create a Python project"
)

goal.add(
    Task(
        action="CREATE_FOLDER",
        data={
            "name": "NovaBot"
        }
    )
)

goal.add(
    Task(
        action="CREATE_FILE",
        data={
            "name": "main.py"
        }
    )
)

print()

print(goal)

print()

for task in goal.tasks:

    print(task)