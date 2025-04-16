import os
import cadquery as cq

def generate_model(prompt: str = None, image_path: str = None):
    """
    Genera un sólido CAD a partir de un prompt de texto o una imagen.
    Por ahora: si detecta 'cilindro' genera un cilindro,
    'esfera' una esfera, y resto un cubo de 50 mm.
    La imagen no se procesa aquí (stub para futuras mejoras).
    """
    # Prioriza imagen (stub: siempre cubo)
    if image_path:
        result = cq.Workplane("XY").box(50, 50, 50)
    else:
        text = (prompt or "").lower()
        if "cilindro" in text or "cylinder" in text:
            result = cq.Workplane("XY").circle(25).extrude(50)
        elif "esfera" in text or "sphere" in text:
            result = cq.Workplane("XY").sphere(25)
        else:
            result = cq.Workplane("XY").box(50, 50, 50)
    return result

def export_to_stl(model, model_name: str, output_dir: str = "models"):
    """
    Exporta el modelo CAD a un archivo STL dentro de output_dir usando
    numeración automática y el nombre base model_name.
    Devuelve la ruta completa del STL generado.
    """
    os.makedirs(output_dir, exist_ok=True)
    # Obtener lista de archivos existentes para numerar
    existing = sorted([f for f in os.listdir(output_dir) if f.endswith(".stl")])
    idx = len(existing) + 1
    filename = f"{idx:03d}.{model_name}.stl"
    path = os.path.join(output_dir, filename)
    cq.exporters.export(model, path)
    print(f"Modelo exportado a {path}")
    return path

# Para pruebas independientes
if __name__ == "__main__":
    # Ejemplo: generar un cilindro
    m = generate_model(prompt="cilindro")
    export_to_stl(m, "cilindro")
