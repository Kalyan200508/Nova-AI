from skills import registry


class CommandExecutor:

    def execute(self, commands):

        if commands is None:
            return None

        # Convert single command into a list
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

        # -----------------------------
        # SKILL REGISTRY
        # -----------------------------

        reply = registry.execute(command)

        if reply:
            return reply

        # -----------------------------
        # INTRODUCE SELF
        # -----------------------------

        if command.action == "INTRODUCE_SELF":

            return (
                "I'm Nova, your personal AI assistant. "
                "I'm here to help you automate tasks, "
                "answer questions, and make using your computer easier."
            )

        return None


executor = CommandExecutor()