import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox
from src import core_cad
from src.renderer import create_renderer_window

class MainGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Generador imagen 3D Ancalimë - GUI")
        self.setGeometry(100, 100, 600, 400)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.generate_btn = QPushButton("Generar modelo 3D (Cubo)")
        self.generate_btn.clicked.connect(self.generate_model)
        layout.addWidget(self.generate_btn)

        self.render_btn = QPushButton("Renderizar modelo 3D")
        self.render_btn.clicked.connect(self.render_model)
        layout.addWidget(self.render_btn)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.stl_file = "cube.stl"

    def generate_model(self):
        model = core_cad.generate_cube()
        core_cad.export_to_stl(model, self.stl_file)
        QMessageBox.information(self, "Generado", f"Modelo 3D generado y exportado a {self.stl_file}")

    def render_model(self):
        # Lanza el renderizador en la misma instancia de QApplication
        # create_renderer_window devuelve la ventana, retén la referencia para que no se cierre
        self._renderer_window = create_renderer_window(self.stl_file)

def run_gui():
    app = QApplication(sys.argv)
    window = MainGUI()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run_gui()
