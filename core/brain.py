from intent.engine import intent_engine
from intent.greeting import execute as greeting
from intent.system import (
    current_time,
    current_date,
    exit_system,
)


class Brain:

    def think(self, command):

        if not command:
            return None

        intent = intent_engine.detect(command)

        if intent == "GREETING":
            return greeting()

        elif intent == "TIME":
            return current_time()

        elif intent == "DATE":
            return current_date()

        elif intent == "WHO_ARE_YOU":
            return (
                "I'm Nova, your personal AI assistant. "
                "I'm here to help you automate tasks, answer questions, "
                "search the web, and make using your computer easier."
            )

        elif intent == "THANKS":
            return "You're very welcome, Kalyan."

        elif intent == "SYSTEM_EXIT":
            return exit_system()

        return None


brain = Brain()