import os, sys
from PySide6.QtWidgets import (
    QApplication, QDialog, QLabel, QPushButton,
    QHBoxLayout, QVBoxLayout
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class ViewDialog(QDialog):
    def __init__(self, pixmap, name, save_dir, index):
        super().__init__()
        self.name = name
        self.save_dir = save_dir
        self.index = index
        self.setWindowTitle(f"Vista: {name}")
        self.init_ui(pixmap)

    def init_ui(self, pixmap):
        lbl = QLabel()
        lbl.setAlignment(Qt.AlignCenter)
        lbl.setPixmap(pixmap.scaled(600,400,Qt.KeepAspectRatio))

        btn_save = QPushButton("Guardar")
        btn_skip = QPushButton("Omitir")

        btn_save.clicked.connect(self.on_save)
        btn_skip.clicked.connect(self.reject)

        h = QHBoxLayout()
        h.addWidget(btn_save)
        h.addWidget(btn_skip)

        v = QVBoxLayout()
        v.addWidget(lbl)
        v.addLayout(h)
        self.setLayout(v)

    def on_save(self):
        filename = f"{self.index:03d}.{self.name}.png"
        out = os.path.join(self.save_dir, filename)
        # El pixmap está en el QLabel, recuperémoslo:
        pix = self.findChild(QLabel).pixmap()
        pix.save(out)
        self.accept()

def interactive_preview(views_dir):
    app = QApplication(sys.argv)
    files = sorted([f for f in os.listdir(views_dir) if f.endswith(".png")])
    for idx, fname in enumerate(files, start=1):
        path = os.path.join(views_dir, fname)
        pix = QPixmap(path)
        dlg = ViewDialog(pix, os.path.splitext(fname)[0], views_dir, idx)
        dlg.exec()
    print("Visor interactivo finalizado.")

if __name__=="__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("views_dir", help="Carpeta con los PNG generados")
    args = p.parse_args()
    interactive_preview(args.views_dir)
