import re
import string

from planner.models import Command


class CommandParser:

    def parse(self, text: str):

        if not text:
            return None

        text = text.lower().strip()

        # Remove punctuation
        text = text.translate(
            str.maketrans("", "", string.punctuation)
        )

        # ---------------------------------
        # OPEN APP / WEBSITE
        # ---------------------------------

        match = re.match(r"open (.+)", text)

        if match:

            return Command(
                action="OPEN",
                target=match.group(1).strip(),
            )

        # ---------------------------------
        # GOOGLE SEARCH
        # ---------------------------------

        match = re.match(
            r"search google for (.+)",
            text,
        )

        if match:

            return Command(
                action="GOOGLE_SEARCH",
                query=match.group(1).strip(),
            )

        # ---------------------------------
        # YOUTUBE SEARCH
        # ---------------------------------

        match = re.match(
            r"search youtube for (.+)",
            text,
        )

        if match:

            return Command(
                action="YOUTUBE_SEARCH",
                query=match.group(1).strip(),
            )

        # ---------------------------------
        # GITHUB SEARCH
        # ---------------------------------

        match = re.match(
            r"search github for (.+)",
            text,
        )

        if match:

            return Command(
                action="GITHUB_SEARCH",
                query=match.group(1).strip(),
            )

        # ---------------------------------
        # WIKIPEDIA SEARCH
        # ---------------------------------

        match = re.match(
            r"search wikipedia for (.+)",
            text,
        )

        if match:

            return Command(
                action="WIKIPEDIA_SEARCH",
                query=match.group(1).strip(),
            )

        # ---------------------------------
        # INTRODUCE SELF
        # ---------------------------------

        if text in (
            "what is your name",
            "who are you",
            "introduce yourself",
            "tell me about yourself",
            "whats your name",
        ):

            return Command(
                action="INTRODUCE_SELF",
            )

        return None


parser = CommandParser()