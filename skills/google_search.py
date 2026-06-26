from skills.base import Skill
from automation.engine import automation_engine


class GoogleSearchSkill(Skill):

    name = "GOOGLE_SEARCH"

    def can_handle(self, command):
        return command.action == "GOOGLE_SEARCH"

    def execute(self, command):

        return automation_engine.execute(
            f"search google for {command.query}"
        )


google_search_skill = GoogleSearchSkill()