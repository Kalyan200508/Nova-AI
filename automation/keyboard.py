import pyautogui
import pyperclip


class Keyboard:

    def write(self, text: str):
        pyautogui.write(text, interval=0.02)
        return True

    def hotkey(self, *keys):
        pyautogui.hotkey(*keys)
        return True

    def press(self, key):
        pyautogui.press(key)
        return True

    def copy(self):
        pyautogui.hotkey("ctrl", "c")
        return pyperclip.paste()

    def paste(self, text):
        pyperclip.copy(text)
        pyautogui.hotkey("ctrl", "v")
        return True


keyboard = Keyboard()