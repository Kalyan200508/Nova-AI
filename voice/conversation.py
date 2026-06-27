from time import time


class Conversation:

    def __init__(self):

        self._awake = False
        self.timeout = 15  # seconds
        self.last_activity = 0

    def wake(self):

        self._awake = True
        self.last_activity = time()

    def sleep(self):

        self._awake = False

    def awake(self):

        return self._awake

    def touch(self):

        self.last_activity = time()

    def sleeping(self):

        if not self._awake:
            return False

        if time() - self.last_activity > self.timeout:

            self.sleep()

            return True

        return False


conversation = Conversation()