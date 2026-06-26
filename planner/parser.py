import re
import string

from planner.models import Command


class CommandParser:

    def normalize(self, text: str):

        text = text.lower().strip()

        text = text.translate(
            str.maketrans("", "", string.punctuation)
        )

        return text

    def parse(self, text: str):

        if not text:
            return None

        text = self.normalize(text)

        # -----------------------------
        # MULTIPLE OPEN COMMANDS
        # -----------------------------

        match = re.match(r"open (.+)", text)

        if match:

            targets = match.group(1)

            # then
            targets = targets.replace(" then ", ",")

            # and
            targets = targets.replace(" and ", ",")

            # split
            parts = [
                x.strip()
                for x in targets.split(",")
                if x.strip()
            ]

            if len(parts) == 1:

                return Command(
                    action="OPEN",
                    target=parts[0],
                )

            return [
                Command(
                    action="OPEN",
                    target=item,
                )
                for item in parts
            ]

        # -----------------------------
        # GOOGLE
        # -----------------------------

        match = re.match(
            r"search google for (.+)",
            text,
        )

        if match:

            return Command(
                action="GOOGLE_SEARCH",
                query=match.group(1),
            )

        # -----------------------------
        # YOUTUBE
        # -----------------------------

        match = re.match(
            r"search youtube for (.+)",
            text,
        )

        if match:

            return Command(
                action="YOUTUBE_SEARCH",
                query=match.group(1),
            )

        # -----------------------------
        # INTRODUCE
        # -----------------------------

        if text in (
            "what is your name",
            "who are you",
            "introduce yourself",
            "tell me about yourself",
            "whats your name",
        ):

            return Command(
                action="INTRODUCE_SELF"
            )

        return None


parser = CommandParser()