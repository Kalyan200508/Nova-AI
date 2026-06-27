import sys

from PySide6.QtCore import Qt, QThread
from PySide6.QtWidgets import (
    QApplication,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from gui.widgets.header import Header
from gui.widgets.status import StatusWidget
from gui.widgets.orb import VoiceOrb

from gui.workers import VoiceWorker
from gui.wake_worker import WakeWorker


class NovaWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("NOVA AI")
        self.resize(900, 650)

        self.thread = None
        self.worker = None

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

        QTextEdit{
            background:#1b2230;
            border-radius:12px;
            padding:12px;
            font-size:15px;
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

        self.header = Header()
        layout.addWidget(self.header)

        self.status = StatusWidget()
        layout.addWidget(self.status)

        self.orb = VoiceOrb()
        layout.addWidget(self.orb, alignment=Qt.AlignCenter)

        self.chat = QTextEdit()
        self.chat.setReadOnly(True)
        layout.addWidget(self.chat)

        self.button = QPushButton("🎤 Speak")
        self.button.clicked.connect(self.start_listening)
        layout.addWidget(self.button)

        self.setLayout(layout)

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

    def update_chat(self, user_text, reply):

        if user_text:
            self.chat.append(f"👤 You\n{user_text}\n")

        if reply:
            self.chat.append(f"🤖 Nova\n{reply}\n")

        self.status.set_status("Ready")

    def cleanup_thread(self):

        self.thread = None
        self.worker = None

        self.button.setEnabled(True)

    def closeEvent(self, event):

        try:

            if self.thread is not None and self.thread.isRunning():
                self.thread.quit()
                self.thread.wait()

            if self.wake_thread.isRunning():
                self.wake_thread.quit()
                self.wake_thread.wait()

        except RuntimeError:
            pass

        event.accept()


def start_gui():

    app = QApplication(sys.argv)

    window = NovaWindow()

    window.show()

    sys.exit(app.exec())