import subprocess


class WindowsApps:

    APPS = {
        "notepad": "notepad",
        "calculator": "calc",
        "paint": "mspaint",
        "cmd": "cmd",
        "command prompt": "cmd",
        "powershell": "powershell",
        "terminal": "wt",
        "task manager": "taskmgr",
        "registry editor": "regedit",
        "control panel": "control",
        "settings": "ms-settings:",
        "file explorer": "explorer",
        "explorer": "explorer",
    }

    def open(self, target):

        target = target.lower().strip()

        if target not in self.APPS:
            return None

        command = self.APPS[target]

        try:

            if command == "ms-settings:":

                subprocess.Popen(
                    [
                        "cmd",
                        "/c",
                        "start",
                        "",
                        "ms-settings:",
                    ],
                    shell=True,
                )

            else:

                subprocess.Popen(command, shell=True)

            return f"Opening {target.title()}."

        except Exception as e:

            return f"Failed to open {target.title()}: {e}"


windows_apps = WindowsApps()