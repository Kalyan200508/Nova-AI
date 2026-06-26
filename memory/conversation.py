from collections import deque


class ConversationMemory:

    def __init__(self, limit=20):

        self.messages = deque(maxlen=limit)

    def add_user(self, text):

        self.messages.append(
            {
                "role": "user",
                "content": text,
            }
        )

    def add_assistant(self, text):

        self.messages.append(
            {
                "role": "assistant",
                "content": text,
            }
        )

    def clear(self):

        self.messages.clear()

    def history(self):

        return list(self.messages)

    def last(self):

        if not self.messages:
            return None

        return self.messages[-1]

    def count(self):

        return len(self.messages)


conversation = ConversationMemory()