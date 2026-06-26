from automation.screen import screen

print("Screen Size:", screen.size())

path = screen.screenshot()

print("Saved:", path)