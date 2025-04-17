import cadquery as cq
from src.shape_registry import register_shape

@register_shape(["cubo", "box"])
def make_cube(params):
    # Genera un cubo de lado dims[0] o 50 mm por defecto.
    dims = params.get("dims", [])
    side = dims[0] if dims else 50
    return cq.Workplane("XY").box(side, side, side)

@register_shape(["cilindro", "cylinder"])
def make_cylinder(params):
    # Genera un cilindro de radio dims[0] y altura dims[1] (por defecto 25x50 mm).
    dims = params.get("dims", [])
    r = dims[0] if len(dims) > 0 else 25
    h = dims[1] if len(dims) > 1 else 50
    return cq.Workplane("XY").circle(r).extrude(h)

@register_shape(["esfera", "sphere"])
def make_sphere(params):
    # Genera una esfera de radio dims[0] o 25 mm por defecto.
    dims = params.get("dims", [])
    r = dims[0] if dims else 25
    return cq.Workplane("XY").sphere(r)

@register_shape(["cono", "cone"])
def make_cone(params):
    # Genera un cono de radio dims[0] y altura dims[1] (por defecto 25x50 mm).
    dims = params.get("dims", [])
    r = dims[0] if len(dims) > 0 else 25
    h = dims[1] if len(dims) > 1 else 50
    return cq.Workplane("XY").circle(r).cone(h)

@register_shape(["piramide", "pyramid"])
def make_pyramid(params):
    # Genera una pirámide cuadrada de base dims[0] y altura dims[1].
    dims = params.get("dims", [])
    side = dims[0] if len(dims) > 0 else 50
    h = dims[1] if len(dims) > 1 else 50
    base = cq.Workplane("XY").rect(side, side)
    apex = cq.Workplane("XY").center(0, 0).rect(0, 0)
    return base.loft(apex)

@register_shape(["prisma", "prism"])
def make_prism(params):
    # Genera un prisma rectangular dims[0] x dims[1] x dims[2].
    dims = params.get("dims", [])
    L = dims[0] if len(dims) > 0 else 50
    W = dims[1] if len(dims) > 1 else 50
    H = dims[2] if len(dims) > 2 else 50
    return cq.Workplane("XY").box(L, W, H)
