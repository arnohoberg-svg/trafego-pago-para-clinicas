from lib import *

WA_HOME = MSG_GENERIC

hero_img = picture("arno-hoberg-gestor-trafego-pago", [400, 776], 776, 970,
                   "Arno Hoberg, gestor de tráfego pago para clínicas de estética, de terno azul",
                   "(min-width: 900px) 440px, 92vw", eager=True)
about_img = picture("arno-hoberg-especialista-marketing-clinicas", [480, 864], 864, 1080,
                    "Retrato de Arno Hoberg, especialista em marketing digital para clínicas estéticas",
                    "(min-width: 900px) 400px, 92vw", cls="media-rounded")

FAQ = [
    ("Quanto custa o tráfego pago para clínica de estética?",
     "<p>A gestão começa em <strong>R$ 1.200/mês</strong>. A verba de anúncios é separada, paga direto ao Google e à Meta, com mínimo recomendado de <strong>R$ 600/mês (R$ 20/dia)</strong>. Detalhes na <a href=\"@/precos/\">página de preços</a>.</p>"),
    ("Em quanto tempo aparecem os resultados?",
     "<p>Os primeiros contatos costumam chegar nos primeiros dias. A conta fica mais estável a partir do segundo ou terceiro mês, por isso o contrato mínimo é de 3 meses.</p>"),
    ("Google Ads ou Instagram: qual é melhor para clínica?",
     "<p>Depende do procedimento. O <a href=\"@/google-ads-para-clinicas-esteticas/\">Google Ads</a> captura quem já procura; o <a href=\"@/meta-ads-para-clinicas-esteticas/\">Meta Ads</a> gera demanda. Com verba curta, começamos pelo canal de maior intenção.</p>"),
    ("Vocês garantem um número de pacientes?",
     "<p>Não. O resultado depende também de oferta, preço, atendimento e concorrência. Garantimos método, transparência nos números e otimização constante.</p>"),
    ("Os anúncios seguem as regras do CFM e das plataformas?",
     "<p>Sim: sem promessas de resultado e sem “antes e depois” fora das regras. Veja o <a href=\"@/regras-de-publicidade-para-clinicas/\">guia de regras de publicidade para clínicas</a>.</p>"),
]

# Depoimentos. Troque "Dra. 01" etc. pelo nome real e a especialidade/clínica (opcional) de cada cliente,
# e só mantenha o card se ela autorizou por escrito o uso do texto e da foto.
PROOFS = [
    ("01", "Dra. 01", "", "Reduzi bastante o custo do meu tráfego pago e passei a investir de forma mais inteligente."),
    ("02", "Dra. 02", "", "Depois que começamos a trabalhar juntos, o faturamento da clínica aumentou."),
    ("03", "Dra. 03", "", "O Arno me ajudou a implementar IA no atendimento e isso aumentou a nossa taxa de conversão."),
    ("04", "Dra. 04", "", "O Arno é extremamente profissional e atencioso. Ele realmente se preocupa junto comigo com os resultados."),
]


def proof_cards():
    out = []
    for n, nome, esp, texto in PROOFS:
        base = f"cliente-clinica-estetica-depoimento-{n}"
        img = picture(base, [320, 560], 320, 400, f"Foto de {nome}, cliente do Arno Hoberg", "(min-width: 1000px) 260px, 70vw")
        sub = f"<span>{esp}</span>" if esp else ""
        out.append(f'<figure class="proof">{img}<blockquote><p>“{texto}”</p></blockquote>'
                   f'<figcaption><strong>{nome}</strong>{sub}</figcaption></figure>')
    return "\n".join(out)


def service_tiles():
    opts = [("Google Ads", "Google Ads", "search", "Apareça para quem já procura"),
            ("Meta Ads (Instagram/Facebook)", "Meta Ads", "social", "Gere demanda no Instagram"),
            ("Site/landing page", "Site e landing page", "site", "Página que leva ao WhatsApp"),
            ("Automação de WhatsApp", "Automação de WhatsApp", "bot", "Resposta rápida, sem lead esquecido"),
            ("SEO", "SEO", "seo", "Apareça no Google sem pagar clique")]
    return "".join(
        f'<label class="tile"><input type="checkbox" name="servico" value="{v}"><span class="tile-box">'
        f'<span class="tile-icon">{ICONS[i]}</span><span class="tile-text"><strong>{n}</strong><small>{d}</small></span>'
        f'<span class="tile-check" aria-hidden="true"></span></span></label>' for v, n, i, d in opts)


BODY = f'''<section class="hero" aria-labelledby="titulo-principal">
<div class="container hero-grid">
<div>
<p class="eyebrow">Para clínicas de dermatologia e estética</p>
<h1 id="titulo-principal">Tráfego pago para clínicas de estética: mais pacientes, menos verba desperdiçada</h1>
<p class="lead">Google Ads, Meta Ads, site e WhatsApp automático, em um método feito só para clínicas.</p>
<div class="hero-actions">{wa_btn(WA_HOME, "Falar no WhatsApp", loc="hero")}{audit_btn(loc="hero_auditoria", label="Auditoria gratuita")}</div>
<ul class="hero-points"><li>Gestão a partir de R$ 1.200/mês</li><li>Campanhas enxutas, a partir de R$ 20/dia</li><li>100% online, para todo o Brasil</li></ul>
</div>
<div class="hero-media">{hero_img}<p class="hero-badge"><strong>Arno Hoberg</strong>Gestor de tráfego pago para clínicas</p></div>
</div></section>

<section class="strip" id="resultados" aria-labelledby="resultados-titulo">
<div class="container">
<h2 id="resultados-titulo" class="visually-hidden">Resultado típico nas contas atendidas</h2>
<ul class="mini-stats">
<li><strong>≈ 50%</strong><span>menos custo por clique no Google Ads</span></li>
<li><strong>≈ 50%</strong><span>menos custo por lead no Meta Ads</span></li>
<li><strong>+</strong><span>mais pessoas interessadas</span></li>
</ul>
<p class="strip-note">Resultado típico. Varia conforme clínica, oferta e mercado, sem garantia de números.</p>
</div></section>

<section class="section" id="servicos" aria-labelledby="servicos-titulo">
<div class="container">
<div class="section-head center"><span class="eyebrow">Orçamento rápido</span><h2 id="servicos-titulo">O que a sua clínica precisa?</h2>
<p>Marque os serviços e fale com a gente no WhatsApp com a mensagem pronta.</p></div>
<form class="form tiles-form" data-quote novalidate aria-labelledby="servicos-titulo">
<fieldset class="fieldset"><legend class="visually-hidden">Serviços de interesse</legend><div class="tiles">{service_tiles()}</div></fieldset>
<button class="btn btn-primary btn-block" type="submit">{ICONS["wa"]}<span>Pedir orçamento no WhatsApp</span></button>
<p class="form-msg" role="status" aria-live="polite"></p>
</form>
<p class="tiles-links">Saiba mais:
<a href="@/google-ads-para-clinicas-esteticas/">Google Ads</a> ·
<a href="@/meta-ads-para-clinicas-esteticas/">Meta Ads</a> ·
<a href="@/criacao-de-sites-para-clinicas-esteticas/">Sites</a> ·
<a href="@/automacao-whatsapp-para-clinicas/">Automação</a> ·
<a href="@/seo-para-clinicas-esteticas/">SEO</a></p>
</div></section>

<!-- DEPOIMENTOS: use somente com autorização por escrito de cada cliente (texto, nome e foto). Não usar Review/AggregateRating no schema. -->
<section class="section section-alt" id="depoimentos" aria-labelledby="depoimentos-titulo">
<div class="container">
<div class="section-head center"><span class="eyebrow">Prova social</span><h2 id="depoimentos-titulo">Quem já trabalha com o Arno</h2></div>
<div class="proofs">
{proof_cards()}
</div>
<p class="strip-note center">Depoimentos de clientes. Resultados variam conforme clínica, oferta e mercado.</p>
</div></section>

<section class="section" id="como-funciona" aria-labelledby="metodo-titulo">
<div class="container">
<div class="section-head center"><span class="eyebrow">Método</span><h2 id="metodo-titulo">Como funciona em 4 passos</h2></div>
<ol class="steps steps-4 steps-compact">
<li><h3>Auditoria</h3><p>Vemos onde a verba está vazando.</p></li>
<li><h3>Campanhas enxutas</h3><p>Poucas campanhas, nos procedimentos que mais dão retorno.</p></li>
<li><h3>Otimização semanal</h3><p>Ajustes guiados por dados, não por achismo.</p></li>
<li><h3>Escala com controle</h3><p>Aumentamos a verba quando o custo por lead estabiliza.</p></li>
</ol>
<div class="center mt-2">{audit_btn(label="Quero a auditoria gratuita", cls="btn btn-primary", loc="metodo_auditoria")}</div>
</div></section>

<section class="section section-alt" id="precos" aria-labelledby="precos-titulo">
<div class="container">
<div class="section-head center"><span class="eyebrow">Investimento</span><h2 id="precos-titulo">Quanto custa?</h2></div>
<ul class="price-cards">
<li><span>Gestão de tráfego</span><strong>a partir de R$ 1.200/mês</strong></li>
<li><span>Verba de anúncios</span><strong>mín. R$ 600/mês</strong><small>paga direto ao Google/Meta</small></li>
<li><span>Contrato mínimo</span><strong>3 meses</strong></li>
</ul>
<p class="center">Site, landing page e automação: sob orçamento. <a href="@/precos/">Ver detalhes de preços</a></p>
<p class="strip-note center">Anúncios feitos dentro das regras de publicidade em saúde. <a href="@/regras-de-publicidade-para-clinicas/">Leia o guia</a>.</p>
</div></section>

<section class="section" aria-labelledby="sobre-titulo">
<div class="container">
<h2 id="sobre-titulo" class="visually-hidden">Quem cuida da sua conta</h2>
{author_box()}
</div></section>

[[FAQ]]

{cta_band("Vamos ver o que dá para melhorar na sua clínica?", "Conte sobre a sua clínica e receba uma orientação inicial sem compromisso.", WA_HOME, "cta_final", ("auditoria-gratuita-de-anuncios/", "Pedir auditoria gratuita"))}
'''

PAGES = [{
    "path": "",
    "title": "Tráfego Pago para Clínicas de Estética | Arno Hoberg",
    "desc": "Tráfego pago para clínicas de estética e dermatologia: Google Ads, Meta Ads, sites e automação de WhatsApp. Peça sua auditoria gratuita pelo WhatsApp.",
    "body": BODY,
    "faq": FAQ,
    "wa_msg": WA_HOME,
    "schema": [professional_service_schema(), person_schema()],
    "preload": ('<link rel="preload" as="image" type="image/avif" fetchpriority="high" '
                'imagesrcset="@/assets/img/arno-hoberg-gestor-trafego-pago-400.avif 400w, @/assets/img/arno-hoberg-gestor-trafego-pago-776.avif 776w" '
                'imagesizes="(min-width: 900px) 440px, 92vw">\n'),
}]
