from memory.conversation import conversation

conversation.add_user("Hello Nova")

conversation.add_assistant("Hello Kalyan!")

conversation.add_user("Open Chrome")

conversation.add_assistant("Opening Chrome.")

print()

print("Conversation")

print("----------------")

for item in conversation.history():

    print(item["role"], ":", item["content"])

print()

print("Messages:", conversation.count())

print()

print("Last:")

print(conversation.last())