import os
import pyautogui


class Screen:

    def screenshot(self, path="screenshots/latest.png"):

        os.makedirs("screenshots", exist_ok=True)

        image = pyautogui.screenshot()

        image.save(path)

        return path

    def size(self):
        return pyautogui.size()

    def pixel(self, x, y):
        return pyautogui.pixel(x, y)


screen = Screen()