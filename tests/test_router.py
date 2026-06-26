from core.router import router

while True:

    text = input("You: ")

    if text.lower() == "exit":
        break

    reply = router.process(text)

    print()

    print("Nova:", reply)

    print()