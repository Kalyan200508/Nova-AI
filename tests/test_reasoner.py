from agent.reasoner import reasoner

goal = input("Goal: ")

plan = reasoner.think(goal)

print()

print(plan)