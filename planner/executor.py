from skills.registry import registry


class PlannerExecutor:

    def execute(self, commands):

        if commands is None:
            return None

        if not isinstance(commands, list):
            commands = [commands]

        replies = []

        for command in commands:

            reply = registry.execute(command)

            if reply:
                replies.append(reply)

        if replies:
            return "\n".join(replies)

        return None


executor = PlannerExecutor()