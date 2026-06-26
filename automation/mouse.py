import pyautogui


class Mouse:

    def move(self, x: int, y: int, duration: float = 0.3):
        pyautogui.moveTo(x, y, duration=duration)
        return True

    def click(self):
        pyautogui.click()
        return True

    def double_click(self):
        pyautogui.doubleClick()
        return True

    def right_click(self):
        pyautogui.rightClick()
        return True

    def scroll(self, amount: int):
        pyautogui.scroll(amount)
        return True

    def drag(self, x: int, y: int, duration: float = 0.5):
        pyautogui.dragTo(x, y, duration=duration)
        return True

    def position(self):
        return pyautogui.position()


mouse = Mouse()