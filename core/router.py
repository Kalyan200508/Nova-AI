from core.brain import brain
from core.memory import memory
from ai.openai_client import openai_client


class Router:

    def process(self, text):

        if not text:
            return None

        # Try offline brain first
        reply = brain.think(text)

        if reply == "__EXIT__":
            return "__EXIT__"

        if reply is not None:
            memory.save(text, reply)
            return reply

        # Try OpenAI if available
        reply = openai_client.ask(text)

        if reply:
            memory.save(text, reply)
            return reply

        return "I don't know how to answer that yet."


router = Router()