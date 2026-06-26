import re

from memory.session import session
from core.brain import brain
from core.memory import memory
from core.facts import facts
from ai.openai_client import openai_client


class Router:

    def process(self, text):

        if not text:
            return "I didn't hear anything."

        text = text.strip()

        # -----------------------------
        # LEARN NAME
        # -----------------------------
        match = re.search(r"my name is (.+)", text, re.IGNORECASE)

        if match:

            name = match.group(1).strip()

            facts.remember("name", name)
            session.set("user_name", name)

            reply = f"I'll remember that. Your name is {name}."

            memory.save(text, reply)
            session.set("last_command", text)
            session.set("last_reply", reply)

            return reply

        # -----------------------------
        # RECALL NAME
        # -----------------------------
        if re.search(r"what is my name", text, re.IGNORECASE):

            name = facts.recall("name")

            if name:
                reply = f"Your name is {name}."
            else:
                reply = "I don't know your name yet."

            memory.save(text, reply)
            session.set("last_command", text)
            session.set("last_reply", reply)

            return reply

        # -----------------------------
        # OFFLINE BRAIN
        # -----------------------------
        reply = brain.think(text)

        if reply == "__EXIT__":
            return "__EXIT__"

        if reply is not None:

            memory.save(text, reply)

            session.set("last_command", text)
            session.set("last_reply", reply)

            return reply

        # -----------------------------
        # OPENAI
        # -----------------------------
        reply = openai_client.ask(text)

        if reply:

            memory.save(text, reply)

            session.set("last_command", text)
            session.set("last_reply", reply)

            return reply

        return "I don't know how to answer that yet."


router = Router()