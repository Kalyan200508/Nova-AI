import string

from automation.apps import apps


class AutomationEngine:

    def execute(self, text):

        text = text.lower().strip()

        # Remove punctuation like . , ? !
        text = text.translate(
            str.maketrans("", "", string.punctuation)
        )

        if text.startswith("open "):

            app = text.replace("open ", "").strip()

            if apps.open(app):
                return f"Opening {app}."

        return None


automation_engine = AutomationEngine()