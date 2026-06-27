from system.power import power


class SystemController:

    def execute(self, command):

        command = command.lower().strip()

        if command in (
            "lock",
            "lock pc",
            "lock computer",
            "lock windows",
        ):
            return power.lock()

        if command in (
            "sleep",
            "sleep pc",
            "sleep computer",
        ):
            return power.sleep()

        if command in (
            "logout",
            "log out",
            "sign out",
        ):
            return power.logout()

        if command in (
            "restart",
            "restart pc",
            "restart computer",
        ):
            return power.restart()

        if command in (
            "shutdown",
            "shut down",
            "power off",
        ):
            return power.shutdown()

        return None


system = SystemController()