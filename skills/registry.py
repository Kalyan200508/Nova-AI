from automation.engine import automation_engine


class SkillRegistry:

    def execute(self, command):

        action = command.action.upper()

        if action == "OPEN":

            return automation_engine.execute(
                f"open {command.target}"
            )

        if action == "GOOGLE_SEARCH":

            return automation_engine.execute(
                f"search google for {command.query}"
            )

        if action == "YOUTUBE_SEARCH":

            return automation_engine.execute(
                f"search youtube for {command.query}"
            )

        return None


registry = SkillRegistry()