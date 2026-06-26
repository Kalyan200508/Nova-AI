import json
import os


class Memory:

    def __init__(self):
        self.file = "data/chat_history.json"

        os.makedirs("data", exist_ok=True)

        if not os.path.exists(self.file):
            with open(self.file, "w", encoding="utf-8") as f:
                json.dump([], f)

    def save(self, user, assistant):

        history = self.load()

        # If the file contains {} instead of [], reset it.
        if not isinstance(history, list):
            history = []

        history.append({"user": user, "assistant": assistant})

        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(history, f, indent=4, ensure_ascii=False)

    def load(self):

        try:
            with open(self.file, "r", encoding="utf-8") as f:
                data = json.load(f)

            if isinstance(data, list):
                return data

            return []

        except Exception:
            return []

    def clear(self):

        with open(self.file, "w", encoding="utf-8") as f:
            json.dump([], f)


memory = Memory()
