import time


class ConversationManager:

    def __init__(self):
        self.active = False
        self.timeout = 15
        self.last_activity = 0

    def wake(self):
        self.active = True
        self.last_activity = time.time()
        return "Yes?"

    def touch(self):
        self.last_activity = time.time()

    def sleeping(self):
        if not self.active:
            return True

        if time.time() - self.last_activity > self.timeout:
            self.active = False
            return True

        return False

    def awake(self):
        return self.active


conversation = ConversationManager()