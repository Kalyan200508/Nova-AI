import re

from planner.planner import planner
from planner.executor import executor

from internet.engine import internet_engine
from core.brain import brain
from core.memory import memory
from core.facts import facts
from ai.openai_client import openai_client


class Router:

    def process(self, text):

        if not text:
            return "I didn't hear anything."

        text = text.strip()

        # ---------------------------------
        # LEARN USER NAME
        # ---------------------------------

        match = re.search(
            r"my name is (.+)",
            text,
            re.IGNORECASE,
        )

        if match:

            name = match.group(1).strip()

            facts.remember("name", name)

            reply = f"I'll remember that. Your name is {name}."

            memory.save(text, reply)

            return reply

        # ---------------------------------
        # RECALL USER NAME
        # ---------------------------------

        if re.search(
            r"what is my name",
            text,
            re.IGNORECASE,
        ):

            name = facts.recall("name")

            if name:
                reply = f"Your name is {name}."
            else:
                reply = "I don't know your name yet."

            memory.save(text, reply)

            return reply

        # ---------------------------------
        # COMMAND PLANNER
        # ---------------------------------

        plan = planner.plan(text)

        if plan and plan.commands:

            reply = executor.execute(plan.commands)

            if reply:

                memory.save(text, reply)

                return reply

        # ---------------------------------
        # OFFLINE BRAIN
        # ---------------------------------

        reply = brain.think(text)

        if reply == "__EXIT__":
            return "__EXIT__"

        if reply:

            memory.save(text, reply)

            return reply

        # ---------------------------------
        # INTERNET ENGINE
        # ---------------------------------

        reply = internet_engine.search(text)

        if reply:

            memory.save(text, reply)

            return reply

        # ---------------------------------
        # OPENAI CHAT
        # ---------------------------------

        reply = openai_client.ask(text)

        if reply:

            memory.save(text, reply)

            return reply

        # ---------------------------------
        # DEFAULT
        # ---------------------------------

        return "I'm sorry, I couldn't understand that."


router = Router()