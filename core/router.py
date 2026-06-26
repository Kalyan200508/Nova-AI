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
        # LEARN NAME
        # ---------------------------------

        match = re.search(r"my name is (.+)", text, re.IGNORECASE)

        if match:

            name = match.group(1).strip()

            facts.remember("name", name)

            return f"I'll remember that. Your name is {name}."

        # ---------------------------------
        # RECALL NAME
        # ---------------------------------

        if re.search(r"what is my name", text, re.IGNORECASE):

            name = facts.recall("name")

            if name:
                return f"Your name is {name}."

            return "I don't know your name yet."

        # ---------------------------------
        # COMMAND PLANNER
        # ---------------------------------

        plan = planner.plan(text)

        if plan.commands:

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
        # INTERNET
        # ---------------------------------

        reply = internet_engine.search(text)

        if reply:

            memory.save(text, reply)

            return reply

        # ---------------------------------
        # OPENAI
        # ---------------------------------

        reply = openai_client.ask(text)

        if reply:

            memory.save(text, reply)

            return reply

        return "I'm sorry, I couldn't find an answer for that."


router = Router()