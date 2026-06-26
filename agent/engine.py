from agent.planner import planner
from agent.executor import agent_executor


class Agent:

    def run(self, goal):

        plan = planner.plan(goal)

        if not plan:
            return "I couldn't create a plan."

        return agent_executor.execute(plan)


agent = Agent()