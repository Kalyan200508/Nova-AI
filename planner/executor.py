from automation.engine import automation_engine


class CommandExecutor:

    def execute(self, commands):

        if commands is None:
            return None

        # Convert a single Command into a list
        if not isinstance(commands, list):
            commands = [commands]

        replies = []

        for command in commands:

            reply = self.execute_one(command)

            if reply:
                replies.append(reply)

        if replies:
            return "\n".join(replies)

        return None

    def execute_one(self, command):

        if command.action == "INTRODUCE_SELF":

            return (
                "I'm Nova, your personal AI assistant. "
                "I'm here to help you automate tasks, "
                "answer questions, and make using your computer easier."
            )

        elif command.action == "OPEN":

            return automation_engine.execute(
                f"open {command.target}"
            )

        elif command.action == "GOOGLE_SEARCH":

            return automation_engine.execute(
                f"search google for {command.query}"
            )

        elif command.action == "YOUTUBE_SEARCH":

            return automation_engine.execute(
                f"search youtube for {command.query}"
            )

        elif command.action == "GITHUB_SEARCH":

            return automation_engine.execute(
                f"search github for {command.query}"
            )

        elif command.action == "WIKIPEDIA_SEARCH":

            return automation_engine.execute(
                f"search wikipedia for {command.query}"
            )

        return None


executor = CommandExecutor()