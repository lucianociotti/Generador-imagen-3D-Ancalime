import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget,
    QProgressBar, QTextEdit
)
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QPixmap
import trimesh

class RenderWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Renderizador 3D - Ancalimë")
        self.setGeometry(100, 100, 800, 600)
        self.init_ui()
        self._progress = 0
        self._timer = QTimer(self)
        self._timer.setInterval(100)
        self._timer.timeout.connect(self._update_progress)

    def init_ui(self):
        layout = QVBoxLayout()
        self.label = QLabel("Renderizador 3D en construcción...")
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)
        self.progress = QProgressBar()
        self.progress.setRange(0, 100)
        layout.addWidget(self.progress)
        self.log = QTextEdit()
        self.log.setReadOnly(True)
        self.log.setFixedHeight(150)
        layout.addWidget(self.log)
        self.preview = QLabel()
        self.preview.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.preview)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def render_stl(self, stl_file):
        self.label.setText(f"Renderizando: {stl_file}")
        self.progress.setValue(0)
        self._progress = 0
        self.log.clear()
        self.log.append(f"[0%] Cargando STL: {stl_file}")
        self._stl = stl_file
        self._timer.start()

    def _update_progress(self):
        self._progress += 10
        if self._progress <= 100:
            self.progress.setValue(self._progress)
            self.log.append(f"[{self._progress}%] Procesando geometría...")
        if self._progress >= 100:
            self._timer.stop()
            self.log.append("[100%] Render completado")
            self.label.setText("Renderización completa ✅")
            self._show_preview(self._stl)

    def _show_preview(self, stl_file):
        mesh = trimesh.load_mesh(stl_file)
        png = mesh.scene().save_image(resolution=(600,400), visible=True)
        pix = QPixmap()
        pix.loadFromData(png)
        self.preview.setPixmap(pix)

def create_renderer_window(stl_file):
    app = QApplication.instance() or QApplication(sys.argv)
    win = RenderWindow()
    win.render_stl(stl_file)
    win.show()
    return win

def launch_renderer_cli(stl_file):
    app = QApplication.instance() or QApplication(sys.argv)
    win = RenderWindow()
    win.render_stl(stl_file)
    win.show()
    app.exec()
