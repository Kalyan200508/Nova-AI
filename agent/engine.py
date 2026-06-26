from agent.executor import executor
from agent.planner import planner


class AgentEngine:

    def execute(self, text):

        goal = planner.plan(text)

        if not goal.tasks:

            return "I couldn't create a plan for that."

        results = executor.execute(goal)

        replies = []

        for result in results:

            replies.append(result.message)

        return "\n".join(replies)


agent = AgentEngine()