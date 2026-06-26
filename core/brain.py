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
            return "I am Jarvis, your personal AI assistant."

        elif intent == "THANKS":
            return "You're welcome."

        elif intent == "SYSTEM_EXIT":
            return exit_system()

        return None


brain = Brain()