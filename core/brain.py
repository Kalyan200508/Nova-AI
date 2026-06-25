from datetime import datetime


class Brain:

    def __init__(self):
        self.name = "JARVIS"

    def think(self, command):

        command = command.lower().strip()

        if command == "":
            return None

        if "hello" in command:
            return "Hello Kalyan."

        elif "how are you" in command:
            return "I am operating perfectly."

        elif "who are you" in command:
            return "I am Jarvis. Your personal artificial intelligence assistant."

        elif "time" in command:
            return f"The time is {datetime.now().strftime('%I:%M %p')}"

        elif "date" in command:
            return f"Today is {datetime.now().strftime('%d %B %Y')}"

        elif "your name" in command:
            return "My name is Jarvis."

        elif "thank" in command:
            return "You are welcome."

        elif "exit" in command:
            return "__EXIT__"

        return None


brain = Brain()