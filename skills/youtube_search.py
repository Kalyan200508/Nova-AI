from skills.base import Skill
from automation.engine import automation_engine


class YouTubeSearchSkill(Skill):

    name = "YOUTUBE_SEARCH"

    def can_handle(self, command):
        return command.action == "YOUTUBE_SEARCH"

    def execute(self, command):

        return automation_engine.execute(
            f"search youtube for {command.query}"
        )


youtube_search_skill = YouTubeSearchSkill()