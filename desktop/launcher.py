import os
import subprocess
from pathlib import Path


class DesktopLauncher:

    APPS = {
        "chrome": [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        ],

        "vscode": [
            r"C:\Users\Kalyan\AppData\Local\Programs\Microsoft VS Code\Code.exe",
            r"C:\Program Files\Microsoft VS Code\Code.exe",
        ],

        "notepad": [
            "notepad.exe",
        ],

        "calculator": [
            "calc.exe",
        ],

        "explorer": [
            "explorer.exe",
        ],
    }

    FOLDERS = {
        "downloads": Path.home() / "Downloads",
        "documents": Path.home() / "Documents",
        "desktop": Path.home() / "Desktop",
        "pictures": Path.home() / "Pictures",
    }

    def open(self, target: str):

        target = target.lower().strip()

        # ---------------------------
        # Open folders
        # ---------------------------

        if target in self.FOLDERS:

            path = self.FOLDERS[target]

            if path.exists():
                os.startfile(path)
                return f"Opening {target.title()}."

            return f"{target.title()} folder not found."

        # ---------------------------
        # Open applications
        # ---------------------------

        if target in self.APPS:

            for app in self.APPS[target]:

                try:

                    if app.endswith(".exe"):

                        if os.path.exists(app):

                            subprocess.Popen(app)

                            return f"Opening {target.title()}."

                    else:

                        subprocess.Popen(app)

                        return f"Opening {target.title()}."

                except Exception:
                    continue

            return f"{target.title()} is not installed."

        return None


launcher = DesktopLauncher()