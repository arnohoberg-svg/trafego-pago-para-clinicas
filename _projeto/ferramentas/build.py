"""Gera o site estático em ROOT. Uso: python build.py"""
import os, re, json, shutil, sys
from html.parser import HTMLParser
from lib import *

ROOT = os.environ.get("SITE_ROOT", r"D:\SITE TRAFEGO PAGO ESTÉTICA")
HERE = os.path.dirname(os.path.abspath(__file__))

import content_home, content_services, content_other
PAGES = content_home.PAGES + content_services.PAGES + content_other.PAGES

# ---------------------------------------------------------------- CSS
css = open(os.path.join(HERE, "style.css"), encoding="utf-8").read()
crit_src, rest_src = css.split("/*! END CRITICAL */")


def minify_css(s):
    s = re.sub(r"/\*.*?\*/", "", s, flags=re.S)
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"\s*([{};:,>])\s*", r"\1", s)
    s = s.replace(";}", "}")
    return s.strip()


CRIT = minify_css(crit_src)
os.makedirs(os.path.join(ROOT, "assets", "css"), exist_ok=True)
os.makedirs(os.path.join(ROOT, "assets", "js"), exist_ok=True)
open(os.path.join(ROOT, "assets", "css", "style.min.css"), "w", encoding="utf-8").write(minify_css(rest_src))
shutil.copy2(os.path.join(HERE, "main.js"), os.path.join(ROOT, "assets", "js", "main.js"))

# ---------------------------------------------------------------- layout
NAV_SERVICES = [
    ("google-ads-para-clinicas-esteticas/", "Google Ads para clínicas"),
    ("meta-ads-para-clinicas-esteticas/", "Meta Ads (Instagram e Facebook)"),
    ("criacao-de-sites-para-clinicas-esteticas/", "Sites e landing pages"),
    ("automacao-whatsapp-para-clinicas/", "Automação de WhatsApp"),
    ("seo-para-clinicas-esteticas/", "SEO para clínicas"),
]
NAV_MAIN = [("precos/", "Preços"), ("regras-de-publicidade-para-clinicas/", "Regras de publicidade"),
            ("sobre/", "Sobre"), ("contato/", "Contato")]


def cur(path, p):
    return ' aria-current="page"' if path == p else ""


def header(path):
    subs = "".join(f'<li><a href="@/{p}"{cur(path, p)}>{n}</a></li>' for p, n in NAV_SERVICES)
    main = "".join(f'<li><a href="@/{p}"{cur(path, p)}>{n}</a></li>' for p, n in NAV_MAIN)
    return f'''<a class="skip-link" href="#conteudo">Pular para o conteúdo</a>
<header class="site-header"><div class="container header-inner">
<a class="brand" href="@/" aria-label="Arno Hoberg, Tráfego Pago para Clínicas — página inicial">{logo_svg()}<span class="brand-text"><span class="brand-name">Arno Hoberg</span><span class="brand-tag">Tráfego Pago para Clínicas</span></span></a>
<button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav"><span class="menu-toggle-bar" aria-hidden="true"></span>Menu</button>
<nav id="site-nav" class="site-nav" aria-label="Menu principal"><ul class="nav-list">
<li class="nav-item-sub"><button class="nav-sub-toggle" type="button" aria-expanded="false" aria-controls="nav-servicos">Serviços</button><ul id="nav-servicos" class="nav-sub" hidden>{subs}</ul></li>
{main}
<li class="nav-cta"><a class="btn btn-primary btn-sm" href="{wa(MSG_AUDIT)}" target="_blank" rel="noopener" data-loc="menu_auditoria">Auditoria gratuita</a></li>
</ul></nav></div></header>'''


def footer(wa_msg):
    subs = "".join(f'<li><a href="@/{p}">{n}</a></li>' for p, n in NAV_SERVICES)
    return f'''<footer class="site-footer"><div class="container">
<div class="footer-grid">
<div><a class="brand" href="@/" aria-label="Página inicial">{logo_svg()}<span class="brand-text"><span class="brand-name">Arno Hoberg</span><span class="brand-tag">Tráfego Pago para Clínicas</span></span></a>
<p>Tráfego pago, sites e automação para clínicas de dermatologia, estética avançada e procedimentos faciais. Atendimento 100% online para todo o Brasil.</p>
{wa_btn(wa_msg, "Conversar no WhatsApp", "btn btn-light btn-sm", "rodape")}</div>
<div><p class="footer-title">Serviços</p><ul class="footer-links">{subs}<li><span>TikTok Ads (em breve)</span></li></ul></div>
<div><p class="footer-title">Conteúdo</p><ul class="footer-links">
<li><a href="@/precos/">Preços e investimento</a></li><li><a href="@/auditoria-gratuita-de-anuncios/">Auditoria gratuita de anúncios</a></li>
<li><a href="@/ebook/">E-book gratuito</a></li><li><a href="@/regras-de-publicidade-para-clinicas/">Regras de publicidade para clínicas</a></li></ul></div>
<div><p class="footer-title">Institucional</p><ul class="footer-links">
<li><a href="@/sobre/">Sobre Arno Hoberg</a></li><li><a href="@/contato/">Contato</a></li>
<li><a href="@/politica-de-privacidade/">Política de Privacidade</a></li><li><a href="@/termos/">Termos de Uso</a></li>
<li><button class="link-button" type="button" data-consent="open">Preferências de cookies</button></li></ul></div>
</div>
<div class="footer-bottom"><span>© 2026 {BRAND}. Todos os direitos reservados.<!-- {{{{CNPJ}}}} --></span><span>Resultados variam conforme clínica, oferta e mercado.</span></div>
</div></footer>
<a class="wa-float" href="{wa(wa_msg)}" target="_blank" rel="noopener" data-loc="botao_flutuante" aria-label="Conversar no WhatsApp">{ICONS["wa"]}</a>
<div class="cookie-banner" id="cookie-banner" role="dialog" aria-live="polite" aria-label="Aviso de cookies" hidden>
<p>Usamos cookies essenciais e, com a sua permissão, cookies de medição (Google e Meta) para entender o desempenho do site e dos anúncios. Saiba mais na <a href="@/politica-de-privacidade/">Política de Privacidade</a>.</p>
<div class="cookie-actions"><button class="btn btn-primary" type="button" data-consent="accept">Aceitar</button><button class="btn btn-ghost-light" type="button" data-consent="reject">Recusar</button></div>
</div>'''


def crumbs_html(crumbs):
    if not crumbs:
        return ""
    items = []
    for i, (n, p) in enumerate(crumbs):
        if i == len(crumbs) - 1:
            items.append(f'<li><span aria-current="page">{n}</span></li>')
        else:
            items.append(f'<li><a href="@/{p}">{n}</a></li>')
    return f'<nav class="breadcrumbs" aria-label="Trilha de navegação"><ol>{"".join(items)}</ol></nav>'


def head(p):
    path = p["path"]
    canon = f"{URL}/{path}"
    robots = p.get("robots", "index,follow")
    preload = p.get("preload", "")
    graph = base_schema() + p.get("schema", [])
    if p.get("crumbs"):
        graph.append(breadcrumb_schema(p["crumbs"]))
    if p.get("faq"):
        graph.append(faq_schema(p["faq"]))
    graph.insert(0, {"@type": "WebPage", "@id": canon + "#pagina", "url": canon, "name": p["title"],
                     "description": p["desc"], "isPartOf": {"@id": SITE_ID}, "inLanguage": "pt-BR",
                     "dateModified": LASTMOD})
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, separators=(",", ":"))
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(p["title"])}</title>
<meta name="description" content="{esc(p["desc"])}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{canon}">
<!-- Verificação do Google Search Console (substitua o código e remova o comentário):
<meta name="google-site-verification" content="{{{{CODIGO_SEARCH_CONSOLE}}}}"> -->
<meta property="og:type" content="{p.get("og_type", "website")}">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="{esc(BRAND)}">
<meta property="og:title" content="{esc(p.get("og_title", p["title"]))}">
<meta property="og:description" content="{esc(p["desc"])}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{URL}/assets/img/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Arno Hoberg — Tráfego pago para clínicas de estética e dermatologia">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(p.get("og_title", p["title"]))}">
<meta name="twitter:description" content="{esc(p["desc"])}">
<meta name="twitter:image" content="{URL}/assets/img/og-image.jpg">
<meta name="twitter:image:alt" content="Arno Hoberg — Tráfego pago para clínicas de estética e dermatologia">
<link rel="icon" href="@/favicon.ico" sizes="48x48">
<link rel="icon" href="@/favicon.svg" type="image/svg+xml">
<link rel="icon" type="image/png" sizes="32x32" href="@/favicon-32x32.png">
<link rel="apple-touch-icon" href="@/apple-touch-icon.png">
<link rel="manifest" href="@/site.webmanifest">
<meta name="theme-color" content="{THEME}">
{preload}<style>{CRIT}</style>
<link rel="stylesheet" href="@/assets/css/style.min.css" media="print" onload="this.media='all'">
<noscript><link rel="stylesheet" href="@/assets/css/style.min.css"><style>.site-nav{{display:block;position:static;box-shadow:none}}.menu-toggle{{display:none}}.nav-sub[hidden]{{display:block}}</style></noscript>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('consent','default',{{ad_storage:'denied',analytics_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',wait_for_update:500}});</script>
<!-- Google Tag Manager / GA4 / Meta Pixel: NÃO cole os snippets aqui.
     Preencha gtmId (ou ga4Id / metaPixelId) em assets/js/main.js — os scripts só carregam após o consentimento (LGPD). -->
<script src="@/assets/js/main.js" defer></script>
<script type="application/ld+json">{ld}</script>
</head>'''


def render(p):
    path = p["path"]
    depth = path.count("/")
    prefix = "./" if depth == 0 else "../" * depth
    body = p["body"].replace("[[CRUMBS]]", crumbs_html(p.get("crumbs")))
    if p.get("faq"):
        body = body.replace("[[FAQ]]", faq_section(p["faq"], p.get("faq_title", "Perguntas frequentes"), p.get("faq_intro", "")))
    doc = (head(p) + "\n<body>\n" + header(path) + '\n<main id="conteudo">\n' + body + "\n</main>\n"
           + footer(p.get("wa_msg", MSG_GENERIC)) + "\n</body>\n</html>\n")
    doc = doc.replace("@/", prefix)
    if p.get("notes"):
        doc = doc.replace("<head>", "<head>\n" + p["notes"], 1)
    out = os.path.join(ROOT, path, "index.html") if path else os.path.join(ROOT, "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write(doc)
    return out, doc


written = [render(p) for p in PAGES]

# 404 autocontida (GitHub Pages serve 404.html em qualquer profundidade → URLs absolutas)
import content_404
open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8").write(content_404.build(CRIT + minify_css(rest_src)))

# ---------------------------------------------------------------- arquivos técnicos
indexable = [p for p in PAGES if p.get("robots", "index,follow").startswith("index")]
prio = {"": "1.0"}
sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for p in indexable:
    sm.append(f"  <url><loc>{URL}/{p['path']}</loc><lastmod>{LASTMOD}</lastmod></url>")
sm.append("</urlset>")
open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write("\n".join(sm) + "\n")

open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8").write(
    "User-agent: *\nAllow: /\nDisallow: /obrigado/\n\n"
    "# Favicons, CSS, JS e imagens ficam liberados para o Google renderizar a página.\n"
    f"Sitemap: {URL}/sitemap.xml\n")

manifest = {"name": BRAND, "short_name": "Arno Hoberg", "lang": "pt-BR", "start_url": "./", "scope": "./",
            "display": "standalone", "background_color": "#FFFFFF", "theme_color": THEME,
            "icons": [{"src": "icon-192.png", "sizes": "192x192", "type": "image/png"},
                      {"src": "icon-512.png", "sizes": "512x512", "type": "image/png"},
                      {"src": "icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}]}
open(os.path.join(ROOT, "site.webmanifest"), "w", encoding="utf-8").write(json.dumps(manifest, ensure_ascii=False, indent=2))
open(os.path.join(ROOT, ".nojekyll"), "w").close()


# ---------------------------------------------------------------- validação
class Audit(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.heads, self.stack, self.text, self.skip, self.in_main = [], None, [], 0, False
        self.imgs, self.links, self.ids, self.comment_depth = [], [], [], 0

    def handle_starttag(self, tag, a):
        a = dict(a)
        if "id" in a:
            self.ids.append(a["id"])
        if tag in ("script", "style", "noscript"):
            self.skip += 1
        if tag == "main":
            self.in_main = True
        if re.fullmatch(r"h[1-6]", tag):
            self.stack = [int(tag[1]), ""]
        if tag == "img":
            self.imgs.append(a)
        if tag == "a" and "href" in a:
            self.links.append(a["href"])

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript"):
            self.skip -= 1
        if tag == "main":
            self.in_main = False
        if self.stack and tag == f"h{self.stack[0]}":
            self.heads.append((self.stack[0], re.sub(r"\s+", " ", self.stack[1]).strip()))
            self.stack = None

    def handle_data(self, d):
        if self.stack:
            self.stack[1] += d
        if self.in_main and not self.skip:
            self.text.append(d)


problems, report = [], []
for (out, doc), p in zip(written, PAGES):
    a = Audit(); a.feed(doc)
    name = "/" + p["path"]
    h1 = [h for h in a.heads if h[0] == 1]
    if len(h1) != 1:
        problems.append(f"{name}: {len(h1)} H1")
    prev = 0
    for lvl, t in a.heads:
        if lvl > prev + 1:
            problems.append(f"{name}: salto de nível H{prev}→H{lvl} em '{t}'")
        prev = lvl
    words = len(re.findall(r"\w+", " ".join(a.text)))
    tl, dl = len(p["title"]), len(p["desc"])
    if tl > 60: problems.append(f"{name}: title {tl} caracteres")
    if not 140 <= dl <= 160: problems.append(f"{name}: description {dl} caracteres")
    for im in a.imgs:
        for k in ("alt", "width", "height"):
            if k not in im: problems.append(f"{name}: img sem {k}: {im.get('src')}")
    dup = {i for i in a.ids if a.ids.count(i) > 1}
    if dup: problems.append(f"{name}: ids duplicados {dup}")
    base = os.path.dirname(out)
    for href in a.links:
        if href.startswith(("http", "mailto:", "tel:", "#")) or "{{" in href:
            continue
        target = os.path.normpath(os.path.join(base, href.split("#")[0].split("?")[0]))
        if os.path.isdir(target): target = os.path.join(target, "index.html")
        if not os.path.exists(target): problems.append(f"{name}: link quebrado {href}")
    for m in re.findall(r'(?:src|srcset|href)="([^"]+\.(?:webp|avif|png|svg|ico|css|js))', re.sub(r"<!--.*?-->", "", doc, flags=re.S)):
        for part in m.split(","):
            f = part.strip().split(" ")[0]
            if f.startswith("http"): continue
            if not os.path.exists(os.path.normpath(os.path.join(base, f))): problems.append(f"{name}: asset ausente {f}")
    report.append((name, p["title"], tl, dl, words, a.heads))

with open(os.path.join(HERE, "report.txt"), "w", encoding="utf-8") as f:
    for name, title, tl, dl, words, heads in report:
        f.write(f"\n## {name}  | title {tl} | desc {dl} | palavras no <main> {words}\n")
        for lvl, t in heads:
            f.write("  " * (lvl - 1) + f"H{lvl} {t}\n")
print("\n".join(f"{n:48} title={tl:3} desc={dl:3} palavras={w}" for n, _, tl, dl, w, _ in report))
print("PROBLEMAS:" if problems else "Nenhum problema encontrado.")
for x in sorted(set(problems)):
    print(" -", x)
