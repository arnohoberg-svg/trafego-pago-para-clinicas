"""404.html autocontida: o GitHub Pages a serve em qualquer URL inexistente (qualquer profundidade),
então caminhos relativos quebrariam. Todos os links usam {{URL_BASE}} absoluto e o CSS é inline."""
from lib import *


def build(css):
    links = "".join(f'<li><a href="{URL}/{p}">{n}</a></li>' for p, n, *_ in SERVICES)
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Página não encontrada (404) | Arno Hoberg</title>
<meta name="description" content="A página que você procurou não existe ou mudou de endereço. Volte ao início ou fale com Arno Hoberg pelo WhatsApp.">
<meta name="robots" content="noindex,follow">
<link rel="icon" href="{URL}/favicon.ico" sizes="48x48">
<link rel="icon" href="{URL}/favicon.svg" type="image/svg+xml">
<link rel="icon" type="image/png" sizes="32x32" href="{URL}/favicon-32x32.png">
<link rel="apple-touch-icon" href="{URL}/apple-touch-icon.png">
<link rel="manifest" href="{URL}/site.webmanifest">
<meta name="theme-color" content="{THEME}">
<style>{css}</style>
</head>
<body>
<header class="site-header"><div class="container header-inner">
<a class="brand" href="{URL}/" aria-label="Arno Hoberg — página inicial">{logo_svg()}<span class="brand-text"><span class="brand-name">Arno Hoberg</span><span class="brand-tag">Tráfego Pago para Clínicas</span></span></a>
{audit_btn("Auditoria gratuita", "btn btn-primary btn-sm", "404_menu")}
</div></header>
<main id="conteudo">
<section class="hero" aria-labelledby="titulo-principal"><div class="container" style="max-width:760px;padding-top:40px">
<p class="error-code" aria-hidden="true">404</p>
<h1 id="titulo-principal">Página não encontrada</h1>
<p class="lead">O endereço pode ter mudado ou sido digitado errado. Veja abaixo os caminhos mais procurados ou fale direto comigo.</p>
<div class="hero-actions"><a class="btn btn-primary" href="{URL}/">Voltar ao início</a>{wa_btn(MSG_GENERIC, "Falar no WhatsApp", "btn btn-secondary", "404")}</div>
<h2>Páginas mais acessadas</h2>
<ul class="checklist">{links}<li><a href="{URL}/precos/">Preços</a></li><li><a href="{URL}/regras-de-publicidade-para-clinicas/">Regras de publicidade para clínicas</a></li></ul>
</div></section>
</main>
</body>
</html>
'''
