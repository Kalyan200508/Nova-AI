from agent.planner import planner

goal = planner.plan(
    "Create Python project NovaBot"
)

print()

print(goal)

print()

for i, task in enumerate(goal.tasks, start=1):

    print(f"{i}. {task.action}")

    print(task.data)

    print()