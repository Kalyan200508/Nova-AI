from datetime import datetime


class HistoryMemory:

    def __init__(self):

        self.records = []

    def add(self, user, assistant):

        self.records.append(
            {
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "user": user,
                "assistant": assistant,
            }
        )

    def all(self):

        return self.records

    def last(self):

        if not self.records:
            return None

        return self.records[-1]

    def clear(self):

        self.records.clear()

    def count(self):

        return len(self.records)


history = HistoryMemory()