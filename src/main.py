import argparse
from src import core_cad
from src import renderer

def main():
    parser = argparse.ArgumentParser(description="Generador imagen 3D Ancalimë - Prototipo")
    parser.add_argument("--generate", action="store_true", help="Generar modelo 3D (cubo por defecto)")
    parser.add_argument("--render", action="store_true", help="Renderizar el modelo 3D generado")
    args = parser.parse_args()

    stl_filename = "cube.stl"

    if args.generate:
        print("Generando modelo 3D...")
        model = core_cad.generate_cube()
        core_cad.export_to_stl(model, stl_filename)

    if args.render:
        print("Renderizando modelo 3D...")
        renderer.launch_renderer(stl_filename)

    if not args.generate and not args.render:
        parser.print_help()

if __name__ == "__main__":
    main()
