from pathlib import Path
from datetime import datetime

import pyautogui


class ScreenshotController:

    def take(self):

        folder = Path.home() / "Pictures" / "Nova"

        folder.mkdir(parents=True, exist_ok=True)

        filename = datetime.now().strftime(
            "Screenshot_%Y%m%d_%H%M%S.png"
        )

        path = folder / filename

        image = pyautogui.screenshot()

        image.save(path)

        return f"Screenshot saved to {path}"


screenshot = ScreenshotController()