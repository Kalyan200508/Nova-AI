from PySide6.QtCore import QObject, Slot

from voice.manager import voice_manager


class WakeWorker(QObject):

    @Slot()
    def run(self):
        voice_manager.run()

    def stop(self):
        voice_manager.stop()