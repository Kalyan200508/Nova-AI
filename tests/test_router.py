from core.router import router


print()

print("Nova Router Test")

print("----------------")

while True:

    text = input("\nYou : ")

    if text.lower() == "exit":
        break

    reply = router.process(text)

    print()

    print("Nova:", reply)