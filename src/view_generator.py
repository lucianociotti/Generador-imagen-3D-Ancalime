import os
import numpy as np
import trimesh

def look_at_matrix(eye, target, up):
    """
    Retorna una matriz 4x4 que sitúa la cámara en `eye`,
    mirando hacia `target`, con vector up `up`.
    """
    eye = np.array(eye, dtype=float)
    target = np.array(target, dtype=float)
    up = np.array(up, dtype=float)

    # Forward vector (direccion de la camara)
    fwd = target - eye
    fwd /= np.linalg.norm(fwd)

    # Right vector
    right = np.cross(fwd, up)
    right /= np.linalg.norm(right)

    # Recompute true up
    true_up = np.cross(right, fwd)

    # Montamos la matriz 4x4
    mat = np.eye(4, dtype=float)
    mat[:3, 0] = right      # ejes X
    mat[:3, 1] = true_up    # ejes Y
    mat[:3, 2] = -fwd       # ejes Z (negativo para mirar hacia adelante)
    mat[:3, 3] = eye        # posicion de la camara
    return mat

def generate_views(stl_file, output_dir="views", resolution=(600,400)):
    mesh = trimesh.load_mesh(stl_file)
    scene = mesh.scene()
    os.makedirs(output_dir, exist_ok=True)

    # Nombre base del archivo STL (sin .stl)
    model_name = os.path.splitext(os.path.basename(stl_file))[0]

    views = {
        "frente":   ([0, 5, 0],   [0, 0, 0], [0, 0, 1]),
        "trasera":  ([0, -5, 0],  [0, 0, 0], [0, 0, 1]),
        "izquierda":([-5, 0, 0],  [0, 0, 0], [0, 0, 1]),
        "derecha":  ([5, 0, 0],   [0, 0, 0], [0, 0, 1]),
        "superior": ([0, 0, 5],   [0, 0, 0], [0, 1, 0]),
    }

    for idx, (name, (eye, target, up)) in enumerate(views.items(), start=1):
        transform = look_at_matrix(eye, target, up)
        scene.camera_transform = transform
        png = scene.save_image(resolution=resolution, visible=True)

        filename = f"{idx:03d}.{model_name}.{name}.png"
        out_path = os.path.join(output_dir, filename)

        with open(out_path, "wb") as f:
            f.write(png)
        print(f"Guardado: {out_path}")

    return output_dir

