import pygetwindow as gw


class WindowManager:

    def titles(self):
        return gw.getAllTitles()

    def activate(self, title):

        for window in gw.getAllWindows():

            if title.lower() in window.title.lower():

                window.activate()

                return True

        return False

    def maximize(self, title):

        for window in gw.getAllWindows():

            if title.lower() in window.title.lower():

                window.maximize()

                return True

        return False

    def minimize(self, title):

        for window in gw.getAllWindows():

            if title.lower() in window.title.lower():

                window.minimize()

                return True

        return False

    def close(self, title):

        for window in gw.getAllWindows():

            if title.lower() in window.title.lower():

                window.close()

                return True

        return False


windows = WindowManager()