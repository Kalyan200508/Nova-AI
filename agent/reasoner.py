import json

from ai.provider import ai


class AgentReasoner:

    def think(self, goal):

        prompt = f"""
You are Nova's planning engine.

Convert the user's goal into JSON.

Return ONLY valid JSON.

Example:

{{
    "tasks":[
        {{
            "action":"CREATE_FOLDER",
            "name":"MyProject"
        }},
        {{
            "action":"CREATE_FILE",
            "path":"MyProject/main.py"
        }}
    ]
}}

User Goal:
{goal}
"""

        reply = ai.ask(prompt)

        if not reply:
            return None

        try:

            start = reply.find("{")

            end = reply.rfind("}") + 1

            return json.loads(reply[start:end])

        except Exception:

            return None


reasoner = AgentReasoner()