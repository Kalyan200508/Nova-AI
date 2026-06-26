import subprocess


class SystemSkill:

    def shutdown(self):

        try:

            subprocess.Popen("shutdown /s /t 0", shell=True)

            return "Shutting down the computer."

        except Exception as e:

            return str(e)

    def restart(self):

        try:

            subprocess.Popen("shutdown /r /t 0", shell=True)

            return "Restarting the computer."

        except Exception as e:

            return str(e)

    def lock(self):

        try:

            subprocess.Popen(
                "rundll32.exe user32.dll,LockWorkStation",
                shell=True,
            )

            return "Locking the computer."

        except Exception as e:

            return str(e)

    def sleep(self):

        try:

            subprocess.Popen(
                "rundll32.exe powrprof.dll,SetSuspendState 0,1,0",
                shell=True,
            )

            return "Putting the computer to sleep."

        except Exception as e:

            return str(e)

    def settings(self):

        try:

            subprocess.Popen("start ms-settings:", shell=True)

            return "Opening Windows Settings."

        except Exception as e:

            return str(e)


system = SystemSkill()