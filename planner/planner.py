import re

from planner.models import Plan
from skills.models import Command


class Planner:

    def plan(self, text: str):

        plan = Plan()

        text = text.lower().strip()

        parts = re.split(r"\band\b", text)

        for part in parts:

            part = part.strip()

            # -------------------------
            # OPEN
            # -------------------------

            match = re.match(r"open (.+)", part)

            if match:

                target = match.group(1).strip()

                plan.add(
                    Command(
                        action="OPEN",
                        target=target,
                    )
                )

                continue

            # -------------------------
            # GOOGLE
            # -------------------------

            match = re.match(
                r"(search google for|google) (.+)",
                part,
            )

            if match:

                query = match.group(2).strip()

                plan.add(
                    Command(
                        action="GOOGLE_SEARCH",
                        query=query,
                    )
                )

                continue

            # -------------------------
            # YOUTUBE
            # -------------------------

            match = re.match(
                r"(search youtube for|youtube) (.+)",
                part,
            )

            if match:

                query = match.group(2).strip()

                plan.add(
                    Command(
                        action="YOUTUBE_SEARCH",
                        query=query,
                    )
                )

                continue

        return plan


planner = Planner()