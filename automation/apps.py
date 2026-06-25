import os
import subprocess


class Apps:

    APPS = {
        # Browsers
        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "edge": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",

        # Editors
        "notepad": "notepad.exe",
        "wordpad": "write.exe",

        # Development
        "vscode": "code",
        "visual studio code": "code",
        "cmd": "cmd.exe",
        "command prompt": "cmd.exe",
        "powershell": "powershell.exe",

        # Windows Apps
        "calculator": "calc.exe",
        "paint": "mspaint.exe",
        "task manager": "taskmgr.exe",
        "control panel": "control.exe",
        "settings": "ms-settings:",
        "file explorer": "explorer.exe",
        "explorer": "explorer.exe",
        "snipping tool": "snippingtool.exe",
        "camera": "microsoft.windows.camera:",
        "registry editor": "regedit.exe",
        "device manager": "devmgmt.msc",

        # Office (if installed)
        "excel": "excel",
        "word": "winword",
        "powerpoint": "powerpnt",
    }

    def open(self, app_name: str):

        app_name = app_name.lower().strip()

        if app_name not in self.APPS:
            return False

        command = self.APPS[app_name]

        try:

            if command.startswith("ms-"):
                os.startfile(command)
                return True

            if os.path.exists(command):
                subprocess.Popen(command)
            else:
                subprocess.Popen(command, shell=True)

            return True

        except Exception as e:
            print(f"[Apps] {e}")
            return False


apps = Apps()