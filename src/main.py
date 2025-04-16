import argparse
from src import core_cad
from src.renderer import launch_renderer_cli
from src.view_generator import generate_views

def main():
    parser = argparse.ArgumentParser(description="Generador imagen 3D Ancalimë - Prototipo CLI")
    parser.add_argument("--generate", action="store_true", help="Generar modelo 3D (cubo por defecto)")
    parser.add_argument("--views", action="store_true", help="Generar 5 vistas PNG del modelo")
    parser.add_argument("--render", action="store_true", help="Renderizar el modelo 3D generado")
    args = parser.parse_args()

    stl_filename = "cube.stl"

    if args.generate:
        print("Generando modelo 3D...")
        model = core_cad.generate_cube()
        core_cad.export_to_stl(model, stl_filename)

    if args.views:
        print("Generando vistas PNG...")
        output_dir = generate_views(stl_filename, "views")
        print(f"Vistas guardadas en: {output_dir}")

    if args.render:
        print("Renderizando modelo 3D...")
        launch_renderer_cli(stl_filename)

    if not (args.generate or args.views or args.render):
        parser.print_help()

if __name__ == "__main__":
    main()
