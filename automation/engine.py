import webbrowser
import subprocess


class AutomationEngine:

    def execute(self, command: str):

        if not command:
            return None

        command = command.strip().lower()

        try:

            # -----------------------------
            # OPEN APPLICATIONS
            # -----------------------------

            if command == "open chrome":

                subprocess.Popen("start chrome", shell=True)

                return "Opening Chrome."

            elif command == "open notepad":

                subprocess.Popen("notepad")

                return "Opening Notepad."

            elif command == "open calculator":

                subprocess.Popen("calc")

                return "Opening Calculator."

            elif command == "open paint":

                subprocess.Popen("mspaint")

                return "Opening Paint."

            elif command == "open cmd":

                subprocess.Popen("cmd")

                return "Opening Command Prompt."

            elif command == "open explorer":

                subprocess.Popen("explorer")

                return "Opening File Explorer."

            # -----------------------------
            # WEBSITES
            # -----------------------------

            elif command == "open youtube":

                webbrowser.open("https://www.youtube.com")

                return "Opening YouTube."

            elif command == "open gmail":

                webbrowser.open("https://mail.google.com")

                return "Opening Gmail."

            elif command == "open github":

                webbrowser.open("https://github.com")

                return "Opening GitHub."

            elif command == "open chatgpt":

                webbrowser.open("https://chat.openai.com")

                return "Opening ChatGPT."

            # -----------------------------
            # GOOGLE SEARCH
            # -----------------------------

            elif command.startswith("search google for"):

                query = command.replace(
                    "search google for",
                    "",
                ).strip()

                webbrowser.open(
                    "https://www.google.com/search?q="
                    + query.replace(" ", "+")
                )

                return f"Searching Google for {query}."

            # -----------------------------
            # YOUTUBE SEARCH
            # -----------------------------

            elif command.startswith("search youtube for"):

                query = command.replace(
                    "search youtube for",
                    "",
                ).strip()

                webbrowser.open(
                    "https://www.youtube.com/results?search_query="
                    + query.replace(" ", "+")
                )

                return f"Searching YouTube for {query}."

            return None

        except Exception as e:

            return str(e)


automation_engine = AutomationEngine()