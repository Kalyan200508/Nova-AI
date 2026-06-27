from system.controller import system


class SystemController:

    def handle(self, text):

        lower = text.lower().strip()

        commands = {
            "lock": "lock",
            "lock pc": "lock",
            "lock my pc": "lock",
            "lock computer": "lock",
            "lock my computer": "lock",

            "sleep": "sleep",
            "sleep pc": "sleep",
            "put computer to sleep": "sleep",
            "put the computer to sleep": "sleep",
            "put my computer to sleep": "sleep",

            "logout": "logout",
            "log out": "logout",
            "log me out": "logout",
            "sign out": "logout",

            "restart": "restart",
            "restart pc": "restart",
            "restart computer": "restart",
            "restart my computer": "restart",

            "shutdown": "shutdown",
            "shut down": "shutdown",
            "shutdown pc": "shutdown",
            "power off": "shutdown",
        }

        command = commands.get(lower)

        if not command:
            return None

        return system.execute(command)


system_controller = SystemController()