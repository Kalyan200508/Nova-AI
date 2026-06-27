import re
import string

from system.power import power
from system.volume import volume
from system.screenshot import screenshot
from system.battery import battery


class SystemController:

    def handle(self, text):

        lower = (
            text.lower()
            .strip()
            .strip(string.punctuation)
        )

        # ====================================
        # POWER COMMANDS
        # ====================================

        if lower in (
            "lock",
            "lock pc",
            "lock computer",
            "lock my pc",
            "lock my computer",
        ):
            return power.lock()

        if lower in (
            "sleep",
            "sleep pc",
            "sleep computer",
            "put computer to sleep",
            "put the computer to sleep",
            "put my computer to sleep",
        ):
            return power.sleep()

        if lower in (
            "logout",
            "log out",
            "log me out",
            "sign out",
        ):
            return power.logout()

        if lower in (
            "restart",
            "restart pc",
            "restart computer",
            "restart my computer",
            "restart my pc",
        ):
            return power.restart()

        if lower in (
            "shutdown",
            "shut down",
            "shutdown pc",
            "shutdown computer",
            "power off",
        ):
            return power.shutdown()

        # ====================================
        # BATTERY
        # ====================================

        if lower in (
            "battery",
            "battery status",
            "battery percentage",
            "battery level",
            "power status",
            "battery?",
            "how much battery do i have",
            "is my laptop charging",
            "is my computer charging",
        ):
            return battery.status()

        # ====================================
        # SCREENSHOT
        # ====================================

        if lower in (
            "screenshot",
            "take screenshot",
            "take a screenshot",
            "capture screen",
            "capture my screen",
            "take screen shot",
            "screen shot",
            "capture screen",
            "capture screenshot",
        ):
            return screenshot.take()

        # ====================================
        # VOLUME
        # ====================================

        if lower in (
            "mute",
            "mute volume",
            "mute sound",
        ):
            return volume.mute()

        if lower in (
            "unmute",
            "unmute volume",
            "unmute sound",
        ):
            return volume.unmute()

        if lower in (
            "volume up",
            "increase volume",
            "turn volume up",
            "louder",
        ):
            return volume.increase()

        if lower in (
            "volume down",
            "decrease volume",
            "turn volume down",
            "quieter",
        ):
            return volume.decrease()

        if lower in (
            "maximum volume",
            "max volume",
            "full volume",
        ):
            return volume.set(100)

        if lower in (
            "minimum volume",
            "min volume",
        ):
            return volume.set(0)

        # ====================================
        # SET VOLUME (0-100)
        # ====================================

        match = re.search(
            r"(?:volume|set volume(?: to)?|put volume(?: at)?|sound(?: to)?|audio(?: to)?)\s*(\d{1,3})",
            lower,
        )

        if match:

            level = int(match.group(1))

            if 0 <= level <= 100:
                return volume.set(level)

            return "Volume must be between 0 and 100."

        return None


system_controller = SystemController()