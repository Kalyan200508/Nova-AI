import time

from voice.conversation import conversation

print()

print("Waiting...")

print()

print(conversation.wake())

while True:

    print("Awake:", conversation.awake())

    print("Sleeping:", conversation.sleeping())

    print()

    if conversation.sleeping():

        print("Nova is sleeping again.")

        break

    time.sleep(2)