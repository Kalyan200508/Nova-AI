import os
import subprocess


class Apps:

    APPS = {
        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "edge": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "paint": "mspaint.exe",
        "vscode": "code",
    }

    def open(self, app_name: str):

        app_name = app_name.lower().strip()

        if app_name not in self.APPS:
            return False

        app = self.APPS[app_name]

        try:

            if os.path.exists(app):
                subprocess.Popen(app)
            else:
                subprocess.Popen(app, shell=True)

            return True

        except Exception as e:
            print(e)
            return False


apps = Apps()