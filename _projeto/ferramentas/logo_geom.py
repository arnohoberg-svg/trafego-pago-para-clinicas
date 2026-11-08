# Geometria vetorial do monograma "AH" (medida a partir do logo.png 800x800)
POLYS = [
    # moldura do triângulo + base esquerda e direita (um único polígono simples)
    [(400, 50), (720, 604), (549, 604), (515, 538), (605, 538), (400, 182),
     (195, 538), (351, 538), (351, 604), (80, 604)],
    # trecho central da base (entre os cortes diagonais)
    [(351, 538), (515, 538), (515, 604), (384, 604)],
    # hastes do "H"
    [(284, 393), (351, 393), (351, 749), (284, 749)],
    [(449, 393), (515, 393), (515, 749), (449, 749)],
]


def svg_paths(fill="currentColor"):
    d = " ".join("M" + " L".join(f"{x} {y}" for x, y in p) + "Z" for p in POLYS)
    return f'<path fill="{fill}" d="{d}"/>'


def draw(img_size, scale, offset, fill, draw_obj):
    for p in POLYS:
        draw_obj.polygon([(offset[0] + x * scale, offset[1] + y * scale) for x, y in p], fill=fill)
