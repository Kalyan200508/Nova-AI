class VolumeController:

    def __init__(self):

        from pycaw.pycaw import AudioUtilities

        self.volume = AudioUtilities.GetSpeakers().EndpointVolume

    # ------------------------------

    def get(self):

        return round(
            self.volume.GetMasterVolumeLevelScalar() * 100
        )

    # ------------------------------

    def set(self, percent):

        percent = max(0, min(100, int(percent)))

        self.volume.SetMasterVolumeLevelScalar(
            percent / 100,
            None,
        )

        return f"Volume set to {percent}%."

    # ------------------------------

    def increase(self, step=10):

        return self.set(self.get() + step)

    # ------------------------------

    def decrease(self, step=10):

        return self.set(self.get() - step)

    # ------------------------------

    def mute(self):

        self.volume.SetMute(1, None)

        return "Volume muted."

    # ------------------------------

    def unmute(self):

        self.volume.SetMute(0, None)

        return "Volume unmuted."


volume = VolumeController()