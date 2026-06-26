from memory.history import history

history.add(
    "Hello",
    "Hello Kalyan!",
)

history.add(
    "Open Chrome",
    "Opening Chrome.",
)

history.add(
    "Search YouTube for Python",
    "Searching YouTube for Python.",
)

print()

print("========= HISTORY =========")

print()

for item in history.all():

    print(item)

print()

print("Total:", history.count())

print()

print("Last:")

print(history.last())