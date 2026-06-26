from planner.planner import planner
from planner.executor import executor


while True:

    text = input("You: ")

    if text.lower() == "exit":
        break

    plan = planner.plan(text)

    if plan.empty:

        print("No command detected.")

        continue

    reply = executor.execute(plan.commands)

    print()

    print("Nova:", reply)

    print()