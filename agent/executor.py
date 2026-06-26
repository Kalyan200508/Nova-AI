import json

from planner.models import Command
from planner.executor import executor


class AgentExecutor:

    def execute(self, plan):

        if not plan:
            return "No plan."

        try:

            data = json.loads(plan)

        except Exception:

            return "Invalid plan."

        replies = []

        for item in data.get("tasks", []):

            command = Command(
                action=item.get("action"),
                target=item.get("target"),
                query=item.get("query"),
            )

            reply = executor.execute(command)

            if reply:
                replies.append(reply)

        if replies:
            return "\n".join(replies)

        return "Nothing executed."


agent_executor = AgentExecutor()