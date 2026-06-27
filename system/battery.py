import psutil


class BatteryController:

    def status(self):

        battery = psutil.sensors_battery()

        if battery is None:
            return "No battery detected."

        percent = round(battery.percent)

        charging = battery.power_plugged

        if charging:
            state = "Charging"
        else:
            state = "Not Charging"

        if battery.secsleft in (
            psutil.POWER_TIME_UNLIMITED,
            psutil.POWER_TIME_UNKNOWN,
        ):
            time_left = "Unknown"
        else:

            hours = battery.secsleft // 3600
            minutes = (battery.secsleft % 3600) // 60

            time_left = f"{hours}h {minutes}m"

        return (
            f"Battery: {percent}%\n"
            f"Status: {state}\n"
            f"Time Left: {time_left}"
        )


battery = BatteryController()