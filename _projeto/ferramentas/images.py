import os, shutil
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import logo_geom as g

SRC = r"D:\SITE TRAFEGO PAGO ESTÉTICA"
OUT = os.path.join(SRC, "assets", "img")
ORIG = os.path.join(OUT, "originais")
os.makedirs(ORIG, exist_ok=True)

ORANGE = (194, 65, 12)       # #C2410C
ORANGE_LIGHT = (249, 115, 22)  # #F97316
DARK = (20, 20, 22)          # #141416

# 1) Cópias intactas dos originais (originais na raiz não são alterados)
copies = {
    "logo.png": "logo-original.png",
    "FOTO SITE.jpg": "foto-site-original.jpg",
    "FOTO PERFIL 01.jpg": "foto-perfil-01-original.jpg",
    "FOTO HOTMART.jpg": "foto-hotmart-original.jpg",
    "FOTO CORRETOR.jpg": "foto-corretor-original.jpg",
}
for src, dst in copies.items():
    shutil.copy2(os.path.join(SRC, src), os.path.join(ORIG, dst))


def save_variants(im, name, widths):
    w0, h0 = im.size
    for w in widths:
        h = round(h0 * w / w0)
        r = im.resize((w, h), Image.LANCZOS)
        r.save(os.path.join(OUT, f"{name}-{w}.webp"), "WEBP", quality=80, method=6)
        r.save(os.path.join(OUT, f"{name}-{w}.avif"), "AVIF", quality=55)
        print(f"{name}-{w}  {w}x{h}")


def open_copy(name):
    return Image.open(os.path.join(ORIG, name)).convert("RGB")

# 2) Fotos responsivas
save_variants(open_copy("foto-site-original.jpg").crop((152, 110, 928, 1080)),
              "arno-hoberg-gestor-trafego-pago", [400, 776])
save_variants(open_copy("foto-perfil-01-original.jpg"),
              "arno-hoberg-consultor-trafego-pago-clinicas", [480, 960])
save_variants(open_copy("foto-hotmart-original.jpg").crop((0, 60, 1080, 1410)),
              "arno-hoberg-especialista-marketing-clinicas", [480, 864])
save_variants(open_copy("foto-corretor-original.jpg"),
              "arno-hoberg-retrato", [400, 800])
save_variants(open_copy("foto-perfil-01-original.jpg").crop((430, 170, 1090, 830)),
              "arno-hoberg-avatar", [96, 192])


# 3) Logo: renderização a partir do vetor (fiel ao original)
def mark(size, fg, bg=None, pad=0.14, radius=0.22):
    S = 4
    big = size * S
    im = Image.new("RGBA", (big, big), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    if bg:
        d.rounded_rectangle((0, 0, big - 1, big - 1), radius=int(big * radius), fill=bg)
    # bbox do desenho: x 80..720, y 50..749 (640 x 699)
    inner = big * (1 - 2 * pad)
    scale = inner / 699
    ox = (big - 640 * scale) / 2 - 80 * scale
    oy = (big - 699 * scale) / 2 - 50 * scale
    g.draw(None, scale, (ox, oy), fg, d)
    return im.resize((size, size), Image.LANCZOS)

# logo transparente para schema/uso geral
mark(512, (17, 17, 17, 255), None, pad=0.06).save(os.path.join(OUT, "logo-arno-hoberg-512.png"), optimize=True)

# favicons (fundo laranja, símbolo branco — legível em 16 px e em abas escuras/claras)
icons = {
    "favicon-16x16.png": 16, "favicon-32x32.png": 32, "favicon-48x48.png": 48,
    "favicon-96x96.png": 96, "apple-touch-icon.png": 180, "icon-192.png": 192, "icon-512.png": 512,
}
for fname, s in icons.items():
    im = mark(s, (255, 255, 255, 255), ORANGE + (255,), pad=0.17 if s >= 48 else 0.13)
    if fname == "apple-touch-icon.png":  # iOS não usa transparência: fundo cheio
        full = Image.new("RGBA", (s, s), ORANGE + (255,))
        full.alpha_composite(mark(s, (255, 255, 255, 255), None, pad=0.2))
        im = full
    im.save(os.path.join(SRC, fname), optimize=True)
# ícone maskable (zona segura de 80%)
full = Image.new("RGBA", (512, 512), ORANGE + (255,))
full.alpha_composite(mark(512, (255, 255, 255, 255), None, pad=0.26))
full.save(os.path.join(SRC, "icon-maskable-512.png"), optimize=True)

ico_imgs = [mark(s, (255, 255, 255, 255), ORANGE + (255,), pad=0.13 if s < 48 else 0.17) for s in (16, 32, 48)]
ico_imgs[2].save(os.path.join(SRC, "favicon.ico"), format="ICO", sizes=[(16, 16), (32, 32), (48, 48)],
                 append_images=ico_imgs[:2])

# favicon.svg e logo.svg
pad = 0.17 * 760
with open(os.path.join(SRC, "favicon.svg"), "w", encoding="utf-8") as f:
    f.write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="-60 -80 920 920">'
            '<rect x="-60" y="-80" width="920" height="920" rx="200" fill="#C2410C"/>'
            + g.svg_paths("#fff") + '</svg>')
with open(os.path.join(OUT, "logo-arno-hoberg.svg"), "w", encoding="utf-8") as f:
    f.write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="80 50 640 700" role="img" aria-label="Logo Arno Hoberg">'
            + g.svg_paths("#111111") + '</svg>')

# 4) Imagem Open Graph 1200x630
W, H = 1200, 630
og = Image.new("RGB", (W, H), DARK)
photo = open_copy("foto-hotmart-original.jpg").crop((0, 0, 1080, 1620))
photo = photo.resize((420, 630), Image.LANCZOS)
og.paste(photo, (W - 420, 0))
# degradê para fundir a foto ao fundo
grad = Image.new("L", (420, 1), 0)
for x in range(420):
    grad.putpixel((x, 0), int(255 * max(0, 1 - x / 220)))
grad = grad.resize((420, H))
og.paste(Image.new("RGB", (420, H), DARK), (W - 420, 0), grad)
d = ImageDraw.Draw(og)
fb = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 58)
fr = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 28)
fs = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 30)
og_mark = mark(120, ORANGE_LIGHT + (255,), None, pad=0.02)
og.paste(og_mark, (72, 70), og_mark)
d.text((210, 92), "Arno Hoberg", font=fs, fill=(255, 255, 255))
d.text((210, 132), "Tráfego Pago para Clínicas", font=fr, fill=(214, 211, 209))
y = 250
for line in ["Tráfego pago para", "clínicas de estética", "e dermatologia"]:
    d.text((72, y), line, font=fb, fill=(255, 255, 255))
    y += 70
d.rectangle((72, 480, 152, 486), fill=ORANGE_LIGHT)
d.text((72, 510), "Google Ads · Meta Ads · Sites · Automação · SEO", font=fr, fill=(214, 211, 209))
og.save(os.path.join(OUT, "og-image.jpg"), "JPEG", quality=85, optimize=True, progressive=True)
print("ok")
