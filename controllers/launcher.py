from desktop.launcher import launcher


class LauncherController:

    def handle(self, text):

        lower = text.lower().strip()

        open_words = (
            "open ",
            "launch ",
            "start ",
            "run ",
        )

        if not lower.startswith(open_words):
            return None

        target = lower

        for word in open_words:
            if target.startswith(word):
                target = target[len(word):]
                break

        target = (
            target
            .replace("google ", "")
            .replace("microsoft ", "")
            .replace("the ", "")
            .strip(" .,!?")
        )

        reply = launcher.open(target)

        if reply and not reply.startswith("I don't know"):
            return reply

        return None


launcher_controller = LauncherController()