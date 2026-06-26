from core.router import router

print()
print("=========== NOVA ROUTER TEST ===========")
print("Type 'exit' to quit.")
print()

while True:

    text = input("You : ")

    if text.lower() == "exit":
        break

    reply = router.process(text)

    print()

    print("Nova :", reply)

    print()