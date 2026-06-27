import sys

from PySide6.QtCore import Qt, QThread
from PySide6.QtWidgets import (
    QApplication,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from gui.widgets.header import Header
from gui.widgets.status import StatusWidget
from gui.widgets.orb import VoiceOrb
from gui.widgets.chat import ChatWidget

from gui.workers import VoiceWorker
from gui.wake_worker import WakeWorker


class NovaWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("NOVA AI")
        self.resize(900, 700)

        self.thread = None
        self.worker = None

        # Wake-word thread
        self.wake_thread = QThread()
        self.wake_worker = WakeWorker()

        self.wake_worker.moveToThread(self.wake_thread)
        self.wake_thread.started.connect(self.wake_worker.run)
        self.wake_thread.start()

        self.setStyleSheet("""
        QWidget{
            background:#10141c;
            color:white;
        }

        QPushButton{
            background:#00BFFF;
            color:white;
            border:none;
            border-radius:10px;
            padding:12px;
            font-size:16px;
        }

        QPushButton:hover{
            background:#009ACD;
        }
        """)

        layout = QVBoxLayout()
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(15)

        # Header
        self.header = Header()
        layout.addWidget(self.header)

        # Status
        self.status = StatusWidget()
        layout.addWidget(self.status)

        # Voice Orb
        self.orb = VoiceOrb()
        layout.addWidget(
            self.orb,
            alignment=Qt.AlignCenter,
        )

        # Chat
        self.chat = ChatWidget()
        layout.addWidget(self.chat, 1)

        # Manual Speak Button
        self.button = QPushButton("🎤 Speak")
        self.button.clicked.connect(self.start_listening)
        layout.addWidget(self.button)

        self.setLayout(layout)

    # -------------------------------------------------

    def start_listening(self):

        if self.thread is not None:
            return

        self.status.set_status("Listening")
        self.button.setEnabled(False)

        self.thread = QThread()

        self.worker = VoiceWorker()
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)

        self.worker.finished.connect(self.update_chat)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)

        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.finished.connect(self.cleanup_thread)

        self.thread.start()

    # -------------------------------------------------

    def update_chat(self, user_text, reply):

        if user_text:
            self.chat.add_user_message(user_text)

        if reply:
            self.chat.add_nova_message(reply)

        self.status.set_status("Ready")

    # -------------------------------------------------

    def cleanup_thread(self):

        self.thread = None
        self.worker = None

        self.button.setEnabled(True)

    # -------------------------------------------------

    def closeEvent(self, event):

        try:

            # Stop manual voice thread
            if self.thread is not None:

                if self.thread.isRunning():

                    self.thread.quit()
                    self.thread.wait(3000)

            # Stop wake-word thread
            if self.wake_thread.isRunning():

                # Tell VoiceManager to stop
                self.wake_worker.stop()

                # Stop Qt thread
                self.wake_thread.quit()

                # Wait for shutdown
                self.wake_thread.wait(5000)

        except RuntimeError:
            pass

        event.accept()


def start_gui():

    app = QApplication(sys.argv)

    window = NovaWindow()

    window.show()

    sys.exit(app.exec())