import re

from planner.models import Plan
from skills.models import Command


class Planner:

    def plan(self, text: str):

        text = text.lower().strip()

        plan = Plan()

        # -------------------------
        # OPEN
        # -------------------------

        match = re.match(r"open (.+)", text)

        if match:

            target = match.group(1).strip()

            plan.add(
                Command(
                    action="OPEN",
                    target=target,
                )
            )

            return plan

        # -------------------------
        # GOOGLE SEARCH
        # -------------------------

        match = re.match(
            r"(search google for|google) (.+)",
            text,
        )

        if match:

            query = match.group(2).strip()

            plan.add(
                Command(
                    action="GOOGLE_SEARCH",
                    query=query,
                )
            )

            return plan

        # -------------------------
        # YOUTUBE SEARCH
        # -------------------------

        match = re.match(
            r"(search youtube for|youtube) (.+)",
            text,
        )

        if match:

            query = match.group(2).strip()

            plan.add(
                Command(
                    action="YOUTUBE_SEARCH",
                    query=query,
                )
            )

            return plan

        return plan


planner = Planner()