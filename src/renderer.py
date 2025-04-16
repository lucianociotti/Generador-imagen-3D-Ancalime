import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget

class RenderWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Renderizador 3D - Ancalimë")
        self.setGeometry(100, 100, 800, 600)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.label = QLabel("Renderizador 3D en construcción...\n(Aquí se mostrará el modelo STL renderizado)")
        layout.addWidget(self.label)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def render_stl(self, stl_file):
        # Función placeholder: en una versión real se integraría PyOpenGL u otra librería.
        self.label.setText(f"Renderizando: {stl_file}")

def launch_renderer(stl_file):
    app = QApplication(sys.argv)
    window = RenderWindow()
    window.render_stl(stl_file)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    launch_renderer("cube.stl")
