import subprocess


class DevelopmentApps:

    def __init__(self):
        self.apps = {
            # VS Code
            "vscode":               "code",
            "vs code":              "code",
            "visual studio code":   "code",
            "code":                 "code",
            # JetBrains
            "pycharm":              "pycharm64.exe",
            "intellij":             "idea64.exe",
            "android studio":       "studio64.exe",
            # Git
            "git":                  "git-bash.exe",
            "git bash":             "git-bash.exe",
            # Terminal
            "terminal":             "wt",
            "windows terminal":     "wt",
        }

    def open(self, target):
        target = target.lower().strip()
        app = self.apps.get(target)

        if app is None:
            return None

        try:
            subprocess.Popen(app, shell=True)
            return f"Opening {target.title()}."
        except Exception as e:
            return f"Unable to open {target}. ({e})"


development_apps = DevelopmentApps()