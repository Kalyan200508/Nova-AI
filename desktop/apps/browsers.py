import os
import subprocess


class BrowserApps:

    BROWSERS = {
        "chrome": [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        ],

        "edge": [
            r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
            r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        ],

        "firefox": [
            r"C:\Program Files\Mozilla Firefox\firefox.exe",
            r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe",
        ],

        "brave": [
            r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
            r"C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe",
        ],

        "opera": [
            os.path.expandvars(
                r"%LOCALAPPDATA%\Programs\Opera\opera.exe"
            ),
        ],
    }

    ALIASES = {
        "google chrome": "chrome",
        "browser": "chrome",
        "microsoft edge": "edge",
        "edge browser": "edge",
        "mozilla firefox": "firefox",
        "brave browser": "brave",
    }

    def open(self, target):

        target = target.lower().strip()

        target = self.ALIASES.get(target, target)

        if target not in self.BROWSERS:
            return None

        for path in self.BROWSERS[target]:

            if os.path.exists(path):

                try:

                    subprocess.Popen(path)

                    return f"Opening {target.title()}."

                except Exception as e:

                    return f"Failed to open {target.title()}: {e}"

        return f"{target.title()} is not installed."


browser_apps = BrowserApps()