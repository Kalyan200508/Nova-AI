from agent.planner import planner
from agent.executor import agent_executor

plan = planner.plan(
    "Prepare my coding environment."
)

print("========== PLAN ==========")
print(plan)

print()
print("========== EXECUTION ==========")

reply = agent_executor.execute(plan)

print(reply)