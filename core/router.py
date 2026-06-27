import re
import string

from ai.provider import ai

from controllers.browser import browser_controller
from controllers.launcher import launcher_controller
from controllers.system import system_controller

from core.brain import brain
from core.memory import memory
from core.facts import facts

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

        lower = (
            text.lower()
            .strip()
            .strip(string.punctuation)
        )

        # -----------------------------
        # Save User Message
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
        # Browser Controller
        # -----------------------------

        reply = browser_controller.handle(text)

        if reply:
            return self.finish(text, reply)

        # -----------------------------
        # Launcher Controller
        # -----------------------------

        reply = launcher_controller.handle(text)

        if reply:
            return self.finish(text, reply)

        # -----------------------------
        # System Controller
        # -----------------------------

        reply = system_controller.handle(text)

        if reply:
            return self.finish(text, reply)

        # -----------------------------
        # Planner
        # -----------------------------

        plan = planner.plan(text)

        if not plan.empty:

            reply = executor.execute(plan.commands)

            if reply:

                if plan.commands:

                    command = plan.commands[0]

                    if command.action == "OPEN":

                        context.set_app(command.target)

                return self.finish(text, reply)

        # -----------------------------
        # Offline Brain
        # -----------------------------

        reply = brain.think(text)

        if reply == "__EXIT__":
            return "__EXIT__"

        if reply:
            return self.finish(text, reply)

        # -----------------------------
        # NVIDIA AI
        # -----------------------------

        reply = ai.ask(text)

        if reply:
            return self.finish(text, reply)

        return "I couldn't answer that."

    # -----------------------------
    # Finish Response
    # -----------------------------

    def finish(self, user, reply):

        memory.save(user, reply)

        session.set("last_reply", reply)

        conversation.add_assistant(reply)

        history.add(user, reply)

        return reply


router = Router()