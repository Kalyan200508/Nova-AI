import time
from automation.windows import windows

print("Open Notepad in 5 seconds...")

time.sleep(5)

print(windows.titles())

windows.activate("Notepad")