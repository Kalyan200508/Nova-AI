import time

from automation.mouse import mouse

print("Move away from the mouse...")

time.sleep(5)

mouse.move(500, 300)

mouse.click()

print("Mouse position:", mouse.position())