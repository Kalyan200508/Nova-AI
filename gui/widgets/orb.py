from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPainter, QBrush
from PySide6.QtWidgets import QWidget


class VoiceOrb(QWidget):

    def __init__(self):
        super().__init__()

        self.setMinimumSize(180, 180)

        self.radius = 55

        self.color = QColor("#00BFFF")

    def set_color(self, color):

        self.color = QColor(color)

        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(QPainter.Antialiasing)

        painter.setBrush(QBrush(self.color))

        painter.setPen(Qt.NoPen)

        center_x = self.width() // 2
        center_y = self.height() // 2

        painter.drawEllipse(
            center_x - self.radius,
            center_y - self.radius,
            self.radius * 2,
            self.radius * 2,
        )