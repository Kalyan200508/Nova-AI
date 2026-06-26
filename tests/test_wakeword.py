from voice.wakeword import wakeword

print()
print("====== NOVA WAKE WORD TEST ======")
print()

while True:

    text = input("You: ")

    if text.lower() == "exit":
        break

    if wakeword.detect(text):

        print("✅ Nova Awakened")

    else:

        print("😴 Sleeping...")