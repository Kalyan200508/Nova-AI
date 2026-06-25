import json
import os


class FactsManager:

    def __init__(self):
        self.file = "memory/facts.json"

        os.makedirs("memory", exist_ok=True)

        if not os.path.exists(self.file):
            with open(self.file, "w", encoding="utf-8") as f:
                json.dump({}, f)

    def load(self):

        try:
            with open(self.file, "r", encoding="utf-8") as f:
                return json.load(f)

        except Exception:
            return {}

    def save(self, data):

        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )

    def remember(self, key, value):

        data = self.load()

        data[key] = value

        self.save(data)

    def recall(self, key):

        data = self.load()

        return data.get(key)

    def forget(self, key):

        data = self.load()

        if key in data:
            del data[key]

        self.save(data)


facts = FactsManager()