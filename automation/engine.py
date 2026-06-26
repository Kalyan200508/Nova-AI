import re
import string

from automation.apps import apps
from automation.browser import browser
from automation.search import search
from automation.fuzzy import fuzzy


class AutomationEngine:

    def execute(self, text):

        if not text:
            return None

        text = text.lower().strip()

        text = text.translate(
            str.maketrans("", "", string.punctuation)
        )

        # ---------------------------------
        # SEARCH COMMANDS
        # ---------------------------------

        match = re.match(
            r"search (google|youtube|github|wikipedia) for (.+)",
            text,
        )

        if match:

            engine = match.group(1)
            query = match.group(2).strip()

            if search.search(engine, query):
                return f"Searching {engine} for {query}."

            return None

        # ---------------------------------
        # OPEN APP / WEBSITE
        # ---------------------------------

        match = re.match(r"open (.+)", text)

        if match:

            item = match.group(1).strip()

            # Fuzzy correction
            item = fuzzy.match(item)

            # Try applications
            if apps.open(item):
                return f"Opening {item}."

            # Try websites
            if browser.open(item):
                return f"Opening {item}."

            return f"I couldn't find {item}."

        return None


automation_engine = AutomationEngine()