import ctypes
import os
import subprocess


class PowerController:

    def lock(self):

        ctypes.windll.user32.LockWorkStation()

        return "Locking your computer."

    def shutdown(self):

        os.system("shutdown /s /t 0")

        return "Shutting down your computer."

    def restart(self):

        os.system("shutdown /r /t 0")

        return "Restarting your computer."

    def sleep(self):

        subprocess.run(
            [
                "rundll32.exe",
                "powrprof.dll,SetSuspendState",
                "0,1,0",
            ],
            check=False,
        )

        return "Putting your computer to sleep."

    def logout(self):

        os.system("shutdown /l")

        return "Logging out."


power = PowerController()