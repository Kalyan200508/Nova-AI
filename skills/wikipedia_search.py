from skills.base import Skill
from automation.engine import automation_engine


class WikipediaSearchSkill(Skill):

    name = "WIKIPEDIA_SEARCH"

    def can_handle(self, command):
        return command.action == "WIKIPEDIA_SEARCH"

    def execute(self, command):

        return automation_engine.execute(
            f"search wikipedia for {command.query}"
        )


wikipedia_search_skill = WikipediaSearchSkill()