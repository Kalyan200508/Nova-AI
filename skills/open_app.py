from skills.base import Skill
from skills.registry import registry
from automation.apps import apps


class OpenAppSkill(Skill):

    name = "OPEN"

    def can_handle(self, command):
        return command.action == "OPEN"

    def execute(self, command):

        if apps.open(command.target):
            return f"Opening {command.target}."

        return None


registry.register(OpenAppSkill())