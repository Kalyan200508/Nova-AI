import subprocess


class OpenAppSkill:

    APPS = {
        "chrome": "start chrome",
        "edge": "start msedge",
        "notepad": "notepad",
        "calculator": "calc",
        "paint": "mspaint",
        "cmd": "cmd",
        "powershell": "powershell",
        "explorer": "explorer",
    }

    def execute(self, app):

        app = app.lower().strip()

        if app not in self.APPS:
            return None

        try:

            subprocess.Popen(
                self.APPS[app],
                shell=True,
            )

            return f"Opening {app.title()}."

        except Exception as e:

            return str(e)


open_app = OpenAppSkill()