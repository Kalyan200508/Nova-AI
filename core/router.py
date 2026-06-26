import re

from ai.provider import ai
from core.brain import brain
from core.facts import facts
from core.memory import memory

from memory.session import session
from memory.context import context
from memory.conversation import conversation
from memory.history import history

from planner.planner import planner
from planner.executor import executor


class Router:

    def process(self, text):

        if not text:
            return "I didn't hear anything."

        text = text.strip()

        # -----------------------------
        # Conversation Memory
        # -----------------------------

        conversation.add_user(text)

        session.set("last_command", text)

        # -----------------------------
        # Learn Name
        # -----------------------------

        match = re.search(
            r"my name is (.+)",
            text,
            re.IGNORECASE,
        )

        if match:

            name = match.group(1).strip()

            facts.remember("name", name)

            session.set("user_name", name)

            reply = f"I'll remember that. Your name is {name}."

            return self.finish(text, reply)

        # -----------------------------
        # Recall Name
        # -----------------------------

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

            return self.finish(text, reply)

        # -----------------------------
        # Planner
        # -----------------------------

        try:

            plan = planner.plan(text)

            if plan and getattr(plan, "commands", None):

                reply = executor.execute(plan.commands)

                if reply:
                    return self.finish(text, reply)

        except Exception:
            pass

        # -----------------------------
        # Offline Brain
        # -----------------------------

        reply = brain.think(text)

        if reply == "__EXIT__":
            return "__EXIT__"

        if reply:

            return self.finish(text, reply)

        # -----------------------------
        # AI Fallback
        # -----------------------------

        reply = ai.ask(prompt=text)

        if reply:

            return self.finish(text, reply)

        return "I'm sorry, I couldn't answer that."

    # =====================================
    # Finish Helper
    # =====================================

    def finish(self, user, reply):

        memory.save(user, reply)

        session.set("last_reply", reply)

        conversation.add_assistant(reply)

        history.add(user, reply)

        return reply


router = Router()