from ai.openai_client import openai_client


SYSTEM_PROMPT = """
You are Nova's Task Planner.

Convert the user's goal into a JSON plan.

Example:

User:
Prepare my coding environment.

Output:

{
    "tasks":[
        {
            "action":"OPEN",
            "target":"vscode"
        },
        {
            "action":"OPEN",
            "target":"chrome"
        },
        {
            "action":"OPEN",
            "target":"github"
        }
    ]
}

Return JSON only.
"""


class AgentPlanner:

    def plan(self, goal):

        return openai_client.ask(
            prompt=goal,
            system_prompt=SYSTEM_PROMPT,
            temperature=0,
        )


planner = AgentPlanner()