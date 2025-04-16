import sys
import os
import shutil
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout,
    QWidget, QMessageBox, QLineEdit, QLabel, QFileDialog, QHBoxLayout
)
from PySide6.QtGui import QPixmap
from src.core_cad import generate_model, export_to_stl
from src.renderer import create_renderer_window
from src.view_generator import generate_views
from src.interactive_viewer import interactive_preview

class MainGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Generador imagen 3D Ancalimë")
        self.setGeometry(100, 100, 600, 500)
        self.stl_file = None
        self.views_dir = "views"
        self.image_path = None
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Input de texto para prompt
        self.prompt_input = QLineEdit()
        self.prompt_input.setPlaceholderText("Describe tu modelo (p.ej. cubo, cilindro, esfera)")
        layout.addWidget(self.prompt_input)

        # Selector de imagen
        h_img = QHBoxLayout()
        btn_load = QPushButton("Cargar imagen…")
        btn_load.clicked.connect(self.load_image)
        self.img_label = QLabel("Sin imagen cargada")
        h_img.addWidget(btn_load)
        h_img.addWidget(self.img_label)
        layout.addLayout(h_img)

        # Botón 1: Generar modelo 3D
        btn1 = QPushButton("1️⃣ Generar modelo 3D")
        btn1.clicked.connect(self.on_generate)
        layout.addWidget(btn1)

        # Botón 2: Renderizar modelo
        btn2 = QPushButton("2️⃣ Renderizar modelo 3D")
        btn2.clicked.connect(self.on_render)
        layout.addWidget(btn2)

        # Botón 3: Generar y revisar vistas
        btn3 = QPushButton("3️⃣ Generar + Revisar 5 vistas PNG")
        btn3.clicked.connect(self.on_generate_and_review_views)
        layout.addWidget(btn3)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def load_image(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Selecciona imagen", "", "Images (*.png *.jpg *.jpeg)"
        )
        if path:
            self.image_path = path
            self.img_label.setText(os.path.basename(path))
        else:
            self.image_path = None
            self.img_label.setText("Sin imagen cargada")

    def on_generate(self):
        prompt = self.prompt_input.text().strip() or None
        model = generate_model(prompt=prompt, image_path=self.image_path)
        # Determinar nombre base del modelo
        if prompt:
            model_name = prompt.replace(" ", "_")
        elif self.image_path:
            model_name = os.path.splitext(os.path.basename(self.image_path))[0]
        else:
            model_name = "modelo"
        # Exportar STL numerado en folder "models/"
        self.stl_file = export_to_stl(model, model_name, output_dir="models")
        QMessageBox.information(self, "OK", f"STL generado → {self.stl_file}")

    def on_render(self):
        if not self.stl_file or not os.path.isfile(self.stl_file):
            QMessageBox.warning(self, "Error", "Primero genera un STL válido.")
            return
        self._win = create_renderer_window(self.stl_file)

    def on_generate_and_review_views(self):
        if not self.stl_file or not os.path.isfile(self.stl_file):
            QMessageBox.warning(self, "Error", "Primero genera un STL válido.")
            return
        # Limpiar vistas anteriores
        if os.path.isdir(self.views_dir):
            shutil.rmtree(self.views_dir)
        # Generar vistas
        output = generate_views(self.stl_file, self.views_dir)
        QMessageBox.information(self, "OK", f"Vistas guardadas en → {output}")
        # Lanzar visor interactivo
        interactive_preview(output)

def run_gui():
    app = QApplication(sys.argv)
    window = MainGUI()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run_gui()
