import re
import string

from automation.apps import apps
from automation.browser import browser
from automation.search import search


class AutomationEngine:

    def execute(self, text):

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

        # ---------------------------------
        # OPEN APPLICATIONS / WEBSITES
        # ---------------------------------

        if text.startswith("open "):

            item = text.replace("open ", "").strip()

            # Try application first
            if apps.open(item):
                return f"Opening {item}."

            # Then try website
            if browser.open(item):
                return f"Opening {item}."

        return None


automation_engine = AutomationEngine()