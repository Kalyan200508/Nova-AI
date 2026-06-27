import re
import string

from ai.provider import ai
from browser.web import browser
from desktop.launcher import launcher
from system.controller import system

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

        match = re.search(r"my name is (.+)", text, re.IGNORECASE)

        if match:
            name = match.group(1).strip()
            facts.remember("name", name)
            session.set("user_name", name)
            reply = f"I'll remember that. Your name is {name}."
            return self.finish(text, reply)

        # -----------------------------
        # Recall Name
        # -----------------------------

        if re.search(r"what is my name", text, re.IGNORECASE):
            name = facts.recall("name")
            reply = f"Your name is {name}." if name else "I don't know your name yet."
            return self.finish(text, reply)

        # -----------------------------
        # Browser
        # -----------------------------

        reply = browser.handle(text)

        if reply:
            return self.finish(text, reply)

        # -----------------------------
        # Desktop Launcher
        # -----------------------------

        open_words = ("open ", "launch ", "start ", "run ")

        if lower.startswith(open_words):

            target = lower

            for word in open_words:
                if target.startswith(word):
                    target = target[len(word):]
                    break

            target = (
                target
                .replace("google ", "")
                .replace("microsoft ", "")
                .replace("the ", "")
                .strip()
            )

            reply = launcher.open(target)

            if reply and not reply.startswith("I don't know"):
                return self.finish(text, reply)

        # -----------------------------
        # System Controls
        # -----------------------------

        system_commands = {
            "lock":                      "lock",
            "lock pc":                   "lock",
            "lock computer":             "lock",
            "lock my pc":                "lock",
            "lock my computer":          "lock",

            "sleep":                     "sleep",
            "sleep pc":                  "sleep",
            "put the computer to sleep": "sleep",
            "put my computer to sleep":  "sleep",

            "logout":                    "logout",
            "log out":                   "logout",
            "sign out":                  "logout",
            "log me out":                "logout",

            "restart":                   "restart",
            "restart pc":                "restart",
            "restart computer":          "restart",
            "restart my computer":       "restart",
            "restart my pc":             "restart",

            "shutdown":                  "shutdown",
            "shut down":                 "shutdown",
            "shutdown pc":               "shutdown",
            "shutdown computer":         "shutdown",
            "power off":                 "shutdown",
        }

        command = system_commands.get(lower)

        if command:
            reply = system.execute(command)
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