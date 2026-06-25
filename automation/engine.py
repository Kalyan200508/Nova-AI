import string

from automation.apps import apps
from automation.browser import browser


class AutomationEngine:

    def execute(self, text):

        text = text.lower().strip()

        text = text.translate(
            str.maketrans("", "", string.punctuation)
        )

        # -----------------------------
        # OPEN APPLICATIONS
        # -----------------------------
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