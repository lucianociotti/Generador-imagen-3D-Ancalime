import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget,
    QProgressBar, QTextEdit
)
from PySide6.QtCore import QTimer, Qt

class RenderWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Renderizador 3D - Ancalimë")
        self.setGeometry(100, 100, 800, 600)
        self.init_ui()
        # Variables para la simulación de progreso
        self._progress_value = 0
        self._timer = QTimer(self)
        self._timer.setInterval(100)  # Actualiza cada 100 ms
        self._timer.timeout.connect(self._update_progress)

    def init_ui(self):
        layout = QVBoxLayout()

        # Etiqueta principal
        self.label = QLabel("Renderizador 3D en construcción...\n(Aquí se mostrará el modelo STL renderizado)")
        layout.addWidget(self.label)

        # Barra de progreso
        self.progress = QProgressBar()
        self.progress.setRange(0, 100)
        self.progress.setValue(0)
        layout.addWidget(self.progress)

        # Log de estado
        self.log = QTextEdit()
        self.log.setReadOnly(True)
        self.log.setFixedHeight(150)
        layout.addWidget(self.log)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def render_stl(self, stl_file):
        # Inicia la simulación de renderizado
        self.label.setText(f"Renderizando: {stl_file}")
        self.progress.setValue(0)
        self._progress_value = 0
        self.log.clear()
        self.log.append(f"[0%] Cargando STL: {stl_file}")
        self._timer.start()

    def _update_progress(self):
        # Simula avance
        self._progress_value += 5
        if self._progress_value <= 100:
            self.progress.setValue(self._progress_value)
            self.log.append(f"[{self._progress_value}%] Procesando geometría...")
        if self._progress_value >= 100:
            self._timer.stop()
            self.log.append("[100%] Render completado")
            self.label.setText("Renderización completa ✅")

def create_renderer_window(stl_file):
    """
    Crea y muestra una ventana de renderizado usando la instancia existente de QApplication.
    """
    app = QApplication.instance() or QApplication(sys.argv)
    window = RenderWindow()
    window.render_stl(stl_file)
    window.show()
    return window

def launch_renderer_cli(stl_file):
    """
    Función para CLI: crea la app si hace falta y entra en el bucle de eventos.
    """
    app = QApplication.instance() or QApplication(sys.argv)
    win = RenderWindow()
    win.render_stl(stl_file)
    win.show()
    app.exec()
