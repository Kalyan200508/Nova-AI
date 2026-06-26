import ctypes
import os
import platform
import subprocess

import psutil
import pyautogui


class SystemController:

    def open_notepad(self):
        subprocess.Popen("notepad")

    def open_calculator(self):
        subprocess.Popen("calc")

    def open_cmd(self):
        subprocess.Popen("cmd")

    def open_powershell(self):
        subprocess.Popen("powershell")

    def open_explorer(self):
        subprocess.Popen("explorer")

    def open_chrome(self):
        chrome_paths = [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        ]

        for path in chrome_paths:
            if os.path.exists(path):
                subprocess.Popen(path)
                return True

        return False

    def screenshot(self):
        image = pyautogui.screenshot()
        image.save("screenshots.png")
        return "Screenshot saved."

    def cpu_usage(self):
        return psutil.cpu_percent(interval=1)

    def ram_usage(self):
        return psutil.virtual_memory().percent

    def system_info(self):
        return {
            "OS": platform.system(),
            "Version": platform.version(),
            "Processor": platform.processor(),
        }

    def lock_pc(self):
        ctypes.windll.user32.LockWorkStation()

    def shutdown(self):
        os.system("shutdown /s /t 5")

    def restart(self):
        os.system("shutdown /r /t 5")


system = SystemController()
