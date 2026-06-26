import re

from agent.models import Goal
from agent.models import Task


class AgentPlanner:

    def plan(self, text: str):

        text = text.strip()

        goal = Goal(text=text)

        # -----------------------------
        # Create Python Project
        # -----------------------------

        match = re.match(
            r"create (?:a )?python project(?: called)? (.+)",
            text,
            re.IGNORECASE,
        )

        if match:

            project = match.group(1).strip()

            goal.add(
                Task(
                    action="CREATE_FOLDER",
                    data={
                        "name": project,
                    },
                )
            )

            goal.add(
                Task(
                    action="CREATE_FILE",
                    data={
                        "path": f"{project}/main.py",
                    },
                )
            )

            goal.add(
                Task(
                    action="CREATE_FILE",
                    data={
                        "path": f"{project}/requirements.txt",
                    },
                )
            )

            goal.add(
                Task(
                    action="CREATE_FILE",
                    data={
                        "path": f"{project}/README.md",
                    },
                )
            )

        return goal


planner = AgentPlanner()