import os
import re
import cadquery as cq
from src.shape_registry import find_shape, parse_params


def generate_model(prompt: str = None, image_path: str = None):
    """
    Genera un sólido CAD a partir de un prompt de texto o imagen.
    Usa el registry de shapes para forma paramétrica.
    """
    # Si viene imagen: stub a cubo de 50 mm
    if image_path:
        return cq.Workplane("XY").box(50, 50, 50)

    prompt = (prompt or "").strip().lower()
    params = parse_params(prompt)
    fn = find_shape(prompt)
    if fn:
        return fn(params)

    # Fallback: cubo de 50 mm
    return cq.Workplane("XY").box(50, 50, 50)


def export_to_stl(model, model_name: str, output_dir: str = "models"):
    """
    Exporta el modelo CAD a STL con numeración automática:
      models/001.nombre.stl, 002.nombre.stl, ...
    Devuelve la ruta al archivo generado.
    """
    os.makedirs(output_dir, exist_ok=True)
    existing = sorted(f for f in os.listdir(output_dir) if f.endswith(".stl"))
    idx = len(existing) + 1
    # Sanear el model_name para ruta válida
    base = re.sub(r"[^\w\-]+", "_", model_name)
    filename = f"{idx:03d}.{base}.stl"
    path = os.path.join(output_dir, filename)
    cq.exporters.export(model, path)
    print(f"Modelo exportado a {path}")
    return path
