from planner.planner import planner
from planner.executor import executor

print()

print("====== NOVA PLANNER ======")

print()

while True:

    text = input("You: ")

    if text.lower() == "exit":
        break

    plan = planner.plan(text)

    if plan.empty:

        print("No command found.")

        continue

    print()

    print("Commands:", len(plan.commands))

    print()

    reply = executor.execute(plan.commands)

    print(reply)

    print()