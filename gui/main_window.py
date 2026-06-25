import sys

from PySide6.QtCore import Qt, QThread
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from gui.workers import VoiceWorker
from voice.speech_queue import speech_queue


class JarvisWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("JARVIS AI")
        self.resize(900, 600)

        self.thread = None
        self.worker = None

        self.setStyleSheet("""
        QWidget{
            background:#10141c;
            color:white;
        }

        QTextEdit{
            background:#1b2230;
            border-radius:10px;
            padding:10px;
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

        QLabel{
            color:white;
            font-size:16px;
        }
        """)

        layout = QVBoxLayout()

        title = QLabel("JARVIS")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Segoe UI", 30))

        layout.addWidget(title)

        self.status = QLabel("Status : Ready")
        self.status.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.status)

        self.chat = QTextEdit()
        self.chat.setReadOnly(True)
        layout.addWidget(self.chat)

        self.button = QPushButton("🎤 Speak")
        self.button.clicked.connect(self.start_listening)
        layout.addWidget(self.button)

        self.setLayout(layout)

        # Speech Queue Signals
        speech_queue.speech_started.connect(self.on_speaking)
        speech_queue.speech_finished.connect(self.on_speech_finished)

    def start_listening(self):

        if self.thread is not None:
            return

        self.status.setText("Status : Listening...")
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
            self.chat.append(f"You : {user_text}")

        if reply:
            self.chat.append(f"Jarvis : {reply}")

        self.chat.append("")

    def cleanup_thread(self):

        self.thread = None
        self.worker = None

    def on_speaking(self):

        self.status.setText("Status : Speaking...")
        self.button.setEnabled(False)

    def on_speech_finished(self):

        self.status.setText("Status : Ready")
        self.button.setEnabled(True)

    def closeEvent(self, event):

        try:
            if self.thread is not None and self.thread.isRunning():
                self.thread.quit()
                self.thread.wait()
        except RuntimeError:
            pass

        event.accept()


def start_gui():

    app = QApplication(sys.argv)

    window = JarvisWindow()

    window.show()

    sys.exit(app.exec())