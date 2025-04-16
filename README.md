# Generador imagen 3D Ancalimë

Proyecto para generar modelos 3D e imágenes renderizadas a partir de descripciones o parámetros definidos por el usuario. Se integra un motor CAD (basado en CadQuery/OCCT), un renderizador simple y una interfaz gráfica interactiva.

## Descripción

Este proyecto busca crear una herramienta modular que permita:
- **Generar modelos 3D:** Utilizando CadQuery para crear sólidos paramétricos (por ejemplo, un cubo de 50 mm de lado).
- **Renderizar los modelos:** Con una interfaz básica basada en PySide6 (con un placeholder para el render real).
- **Interfaz gráfica:** Un GUI sencillo para orquestar la generación y renderizado del modelo.

## Requerimientos

- Python 3.10+
- Conda (opcional, para gestionar el entorno)
- Dependencias listadas en `env.yml`

## Instalación

1. Clona el repositorio:
git clone https://github.com/TuUsuario/Generador-imagen-3D-Ancalimë.git cd Generador-imagen-3D-Ancalimë

csharp
Copiar
2. Crea e instala el entorno virtual (opcional):
conda env create -f env.yml conda activate generador3d-ancalime

markdown
Copiar
3. Ejecuta el script principal para probar:
python src/main.py --generate --render

shell
Copiar

## Uso de la GUI

Para iniciar la interfaz gráfica:
python src/gui.py

sql
Copiar

## Contribuciones

Se aceptan pull requests, issues y sugerencias. Favor de seguir las buenas prácticas de Git y mantener commits descriptivos.

## Licencia

Este proyecto se distribuye bajo la [Licencia MIT](LICENSE).
