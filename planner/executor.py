from automation.engine import automation_engine


class CommandExecutor:

    def execute(self, command):

        if command is None:
            return None

        # ---------------------------------
        # INTRODUCE SELF
        # ---------------------------------

        if command.action == "INTRODUCE_SELF":
            return (
                "I'm Nova, your personal AI assistant. "
                "I'm here to help you automate tasks, answer questions, "
                "and make using your computer easier."
            )

        # ---------------------------------
        # OPEN APP / WEBSITE
        # ---------------------------------

        if command.action == "OPEN":

            return automation_engine.execute(
                f"open {command.target}"
            )

        # ---------------------------------
        # GOOGLE SEARCH
        # ---------------------------------

        if command.action == "GOOGLE_SEARCH":

            return automation_engine.execute(
                f"search google for {command.query}"
            )

        # ---------------------------------
        # YOUTUBE SEARCH
        # ---------------------------------

        if command.action == "YOUTUBE_SEARCH":

            return automation_engine.execute(
                f"search youtube for {command.query}"
            )

        # ---------------------------------
        # GITHUB SEARCH
        # ---------------------------------

        if command.action == "GITHUB_SEARCH":

            return automation_engine.execute(
                f"search github for {command.query}"
            )

        # ---------------------------------
        # WIKIPEDIA SEARCH
        # ---------------------------------

        if command.action == "WIKIPEDIA_SEARCH":

            return automation_engine.execute(
                f"search wikipedia for {command.query}"
            )

        return None


executor = CommandExecutor()