import re
import string

from ai.provider import ai

from controllers.browser import browser_controller
from controllers.launcher import launcher_controller
from controllers.system import system_controller

from core.intent.engine import intent_engine
from core.intent.parser import command_parser

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

    # ====================================================
    # Public Entry
    # ====================================================

    def process(self, text):

        if not text:
            return "I didn't hear anything."

        commands = command_parser.split(text)

        last_reply = None

        for command in commands:

            last_reply = self.process_single(command)

            if last_reply == "__EXIT__":
                return "__EXIT__"

        return last_reply

    # ====================================================
    # Single Command Processor
    # ====================================================

    def process_single(self, text):

        text = text.strip()

        lower = (
            text.lower()
            .strip()
            .strip(string.punctuation)
        )

        # -----------------------------
        # Save Conversation
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

            return self.finish(
                text,
                f"I'll remember that. Your name is {name}.",
            )

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
        # Intent Detection
        # -----------------------------

        intent = intent_engine.detect(text)

        # -----------------------------
        # Browser
        # -----------------------------

        if intent.domain == "browser":

            reply = browser_controller.handle(text)

            if reply:
                return self.finish(text, reply)

        # -----------------------------
        # Launcher
        # -----------------------------

        elif intent.domain == "launcher":

            reply = launcher_controller.handle(text)

            if reply:
                return self.finish(text, reply)

        # -----------------------------
        # System
        # -----------------------------

        elif intent.domain == "system":

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
        # AI Fallback
        # -----------------------------

        reply = ai.ask(text)

        if reply:
            return self.finish(text, reply)

        return "I couldn't answer that."

    # ====================================================
    # Finish
    # ====================================================

    def finish(self, user, reply):

        memory.save(user, reply)

        session.set("last_reply", reply)

        conversation.add_assistant(reply)

        history.add(user, reply)

        return reply


router = Router()