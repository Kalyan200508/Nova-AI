import json
import os


class Memory:

    def __init__(self):
        self.file = "data/chat_history.json"

        if not os.path.exists("data"):
            os.makedirs("data")

        if not os.path.exists(self.file):
            with open(self.file, "w", encoding="utf-8") as f:
                json.dump([], f)

    def save(self, user, assistant):

        with open(self.file, "r", encoding="utf-8") as f:
            history = json.load(f)

        history.append(
            {
                "user": user,
                "assistant": assistant
            }
        )

        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(history, f, indent=4)

    def load(self):

        with open(self.file, "r", encoding="utf-8") as f:
            return json.load(f)

    def clear(self):

        with open(self.file, "w", encoding="utf-8") as f:
            json.dump([], f)


memory = Memory()