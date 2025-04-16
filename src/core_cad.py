import cadquery as cq

def generate_cube(size=50):
    """
    Genera un cubo de dimensiones size x size x size (en milímetros).
    Retorna el objeto de CadQuery que representa el cubo.
    """
    result = cq.Workplane("XY").box(size, size, size)
    return result

def export_to_stl(model, filename="cube.stl"):
    """
    Exporta el modelo dado a un archivo STL.
    """
    cq.exporters.export(model, filename)
    print(f"Modelo exportado a {filename}")

if __name__ == "__main__":
    cube = generate_cube()
    export_to_stl(cube, "cube.stl")
