from agent.engine import agent

print()

print("========== NOVA AGENT ==========")

print()

while True:

    text = input("Goal: ")

    if text.lower() == "exit":
        break

    print()

    reply = agent.execute(text)

    print(reply)

    print()