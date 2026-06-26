from agent.planner import planner
from agent.executor import executor

goal = planner.plan(
    "Create Python project NovaBot"
)

results = executor.execute(goal)

print()

print("=========== RESULTS ===========")

print()

for result in results:

    print(result.success)

    print(result.message)

    print()

print("Goal Completed:", goal.completed)