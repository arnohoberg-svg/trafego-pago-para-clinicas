"""Biblioteca do gerador estático. Gera HTML puro — não é necessário para o site funcionar."""
import json, re, html
from urllib.parse import quote
import logo_geom

URL = "https://arnohoberg-svg.github.io/site-trafego-clinicas"  # sem barra final
WA = "5548988387867"            # (48) 98838-7867 — só números com DDI+DDD
MSG_GENERIC = "Olá! Vim pelo site, gostaria de entender mais sobre o seu processo."
MSG_AUDIT = "Olá! Estava no site e gostaria de uma auditoria gratuita."
BRAND = "Arno Hoberg | Tráfego Pago para Clínicas"
LASTMOD = "2026-10-31"
THEME = "#C2410C"

# ---------------------------------------------------------------- ícones
ICONS = {
    "wa": '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path fill="currentColor" d="M12 2a9.9 9.9 0 0 0-8.5 15l-1.4 5 5.2-1.4A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3.1.8.8-3-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.4a.4.4 0 0 0 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.8-1.2 2.2 2.2 0 0 0 .1-1.3c0-.1-.2-.2-.5-.3Z"/></svg>',
    "search": '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><g fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></g></svg>',
    "social": '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><g fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".6" fill="currentColor"/></g></svg>',
    "site": '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><g fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><rect x="2.5" y="4" width="19" height="14" rx="2"/><path d="M8 21h8M2.5 8h19"/></g></svg>',
    "bot": '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><g fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><path d="M4 5h16v11H9l-5 4V5Z"/><path d="M8.5 10.5h.01M12 10.5h.01M15.5 10.5h.01" stroke-linecap="round" stroke-width="2.6"/></g></svg>',
    "seo": '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><g fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 20h18"/><path d="M6 16v-4M11 16V8M16 16v-6"/><path d="m5 8 5-4 4 3 6-4"/></g></svg>',
    "video": '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><g fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><rect x="3" y="5" width="13" height="14" rx="2"/><path d="m16 10 5-3v10l-5-3"/></g></svg>',
}


def logo_svg(cls=""):
    return (f'<svg class="{cls}" viewBox="80 50 640 700" aria-hidden="true" focusable="false">'
            + logo_geom.svg_paths("#141416") + "</svg>")


def wa(msg):
    return f"https://wa.me/{WA}?text={quote(msg)}"


def audit_btn(label="Quero uma auditoria gratuita", cls="btn btn-secondary", loc="auditoria"):
    return wa_btn(MSG_AUDIT, label, cls, loc)


def wa_btn(msg, label="Falar no WhatsApp", cls="btn btn-primary", loc="conteudo"):
    return (f'<a class="{cls}" href="{wa(msg)}" target="_blank" rel="noopener" data-loc="{loc}">'
            f'{ICONS["wa"]}<span>{label}</span></a>')


def esc(s):
    return html.escape(s, quote=True)


def strip_tags(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s)).strip()


# ---------------------------------------------------------------- imagens
def picture(name, widths, w, h, alt, sizes, eager=False, cls=""):
    """<picture> com AVIF + WebP responsivos. name = prefixo do arquivo em assets/img."""
    def srcset(ext):
        return ", ".join(f"@/assets/img/{name}-{x}.{ext} {x}w" for x in widths)
    load = 'fetchpriority="high" decoding="async"' if eager else 'loading="lazy" decoding="async"'
    return (f'<picture class="{cls}">'
            f'<source type="image/avif" srcset="{srcset("avif")}" sizes="{sizes}">'
            f'<source type="image/webp" srcset="{srcset("webp")}" sizes="{sizes}">'
            f'<img src="@/assets/img/{name}-{widths[-1]}.webp" width="{w}" height="{h}" alt="{esc(alt)}" {load}>'
            f"</picture>")


# ---------------------------------------------------------------- blocos reutilizáveis
SERVICES = [
    ("google-ads-para-clinicas-esteticas/", "Google Ads para clínicas", "search",
     "Apareça para quem já está procurando o procedimento na sua cidade, com campanhas de pesquisa enxutas e palavras-chave negativas bem cuidadas."),
    ("meta-ads-para-clinicas-esteticas/", "Meta Ads (Instagram e Facebook)", "social",
     "Gere demanda com anúncios no Instagram e no Facebook dentro das políticas de saúde, com criativos testados e público bem definido."),
    ("criacao-de-sites-para-clinicas-esteticas/", "Sites e landing pages", "site",
     "Páginas rápidas, claras e pensadas para transformar visita em conversa no WhatsApp, respeitando as regras do seu conselho."),
    ("automacao-whatsapp-para-clinicas/", "Automação de WhatsApp", "bot",
     "Primeira resposta imediata, triagem e follow-up dos contatos para que nenhum interessado fique esperando ou seja esquecido."),
    ("seo-para-clinicas-esteticas/", "SEO para clínicas", "seo",
     "Base técnica e conteúdo para a sua clínica aparecer no Google sem pagar por clique, somando ao tráfego pago no médio prazo."),
]


def service_cards(exclude=None, heading_level=3):
    out = []
    for path, name, icon, text in SERVICES:
        if path == exclude:
            continue
        out.append(f'<article class="card"><div class="card-icon">{ICONS[icon]}</div>'
                   f'<h{heading_level}>{name}</h{heading_level}><p>{text}</p>'
                   f'<a class="card-link" href="@/{path}">Conhecer {name.split(" (")[0].replace(" para clínicas", "")}</a></article>')
    return "\n".join(out)


def cta_band(title, text, msg, loc="cta_faixa", secondary=None):
    sec = ""
    if secondary:
        sec = (audit_btn(secondary[1], "btn btn-ghost-light", loc + "_auditoria") if secondary[0].startswith("auditoria")
               else f'<a class="btn btn-ghost-light" href="@/{secondary[0]}">{secondary[1]}</a>')
    return f'''<section class="section" aria-labelledby="cta-{loc}">
<div class="container"><div class="cta-band">
<div><h2 id="cta-{loc}">{title}</h2><p>{text}</p></div>
<div class="hero-actions">{wa_btn(msg, cls="btn btn-light", loc=loc)}{sec}</div>
</div></div></section>'''


def faq_section(items, title="Perguntas frequentes", intro="", sid="faq"):
    qs = "\n".join(
        f'<details><summary><h3>{q}</h3></summary><div class="faq-answer">{a}</div></details>' for q, a in items)
    intro_html = f"<p>{intro}</p>" if intro else ""
    return f'''<section class="section section-alt" id="{sid}" aria-labelledby="{sid}-titulo">
<div class="container"><div class="section-head"><span class="eyebrow">Dúvidas</span><h2 id="{sid}-titulo">{title}</h2>{intro_html}</div>
<div class="faq">{qs}</div></div></section>'''


def typical_results(dark=False):
    cls = "section section-dark" if dark else "section"
    return f'''<section class="{cls}" id="resultados" aria-labelledby="resultados-titulo">
<div class="container">
<div class="section-head"><span class="eyebrow">Resultados</span><h2 id="resultados-titulo">Resultado típico nas contas que assumimos</h2>
<p>Quando uma conta chega desorganizada — público amplo demais, palavras-chave genéricas, nenhum controle de termos de pesquisa — o primeiro ganho costuma vir de cortar desperdício.</p></div>
<div class="stats">
<div class="stat"><span class="stat-value">≈ 50%</span><span class="stat-label">menos custo por clique no Google Ads</span><p>Redução típica do custo por clique/visita após reestruturar campanhas, palavras-chave e lances.</p></div>
<div class="stat"><span class="stat-value">≈ 50%</span><span class="stat-label">menos custo por lead no Meta Ads</span><p>Redução típica do CPL com públicos, criativos e eventos de conversão bem configurados.</p></div>
<div class="stat"><span class="stat-value">+</span><span class="stat-label">mais pessoas interessadas</span><p>Com o mesmo orçamento, mais contatos chegando ao WhatsApp da clínica.</p></div>
</div>
<p class="disclaimer">Resultado típico. Resultados variam conforme clínica, oferta e mercado — não há garantia de números.</p>
<!-- CASES REAIS: quando houver dados autorizados, duplique o bloco abaixo (removendo o comentário).
<article class="card">
  <span class="tag">Case</span>
  <h3>{{{{NOME_DA_CLINICA}}}} — {{{{CIDADE/UF}}}}</h3>
  <p>Especialidade: {{{{ESPECIALIDADE}}}} · Período: {{{{MM/AAAA a MM/AAAA}}}} · Plataforma: {{{{GOOGLE/META}}}}</p>
  <p>CPC: {{{{ANTES}}}} → {{{{DEPOIS}}}} · CPL: {{{{ANTES}}}} → {{{{DEPOIS}}}} · Leads/mês: {{{{ANTES}}}} → {{{{DEPOIS}}}}</p>
  <p class="note">Dados reais do gerenciador de anúncios, divulgados com autorização por escrito de {{{{RESPONSAVEL}}}} em {{{{DATA}}}}.</p>
</article>
-->
</div></section>'''


def testimonials_placeholder():
    return '''<!-- DEPOIMENTOS REAIS: seção pronta, mantida comentada até haver depoimentos autorizados.
Para publicar: remova este comentário e preencha. Não use depoimentos inventados nem de pacientes.
<section class="section section-alt" aria-labelledby="depoimentos-titulo">
  <div class="container">
    <div class="section-head"><span class="eyebrow">Depoimentos</span><h2 id="depoimentos-titulo">O que dizem as clínicas atendidas</h2></div>
    <div class="grid grid-3">
      <figure class="card">
        <blockquote><p>“{{TEXTO_DO_DEPOIMENTO}}”</p></blockquote>
        <figcaption><img src="assets/img/{{FOTO}}.webp" width="56" height="56" alt="{{NOME}}" loading="lazy">
          <strong>{{NOME}}</strong>, {{CARGO}} — {{NOME_DA_CLINICA}}, {{CIDADE/UF}}</figcaption>
        <p class="note">Depoimento autorizado por escrito em {{DATA}}.</p>
      </figure>
    </div>
  </div>
</section>
-->'''


def how_it_works(dark=False, title="Como funciona: o método em 4 etapas"):
    cls = "section section-dark" if dark else "section section-alt"
    return f'''<section class="{cls}" id="como-funciona" aria-labelledby="metodo-titulo">
<div class="container">
<div class="section-head"><span class="eyebrow">Método</span><h2 id="metodo-titulo">{title}</h2>
<p>Um processo simples e previsível, pensado para clínicas que precisam de resultado sem desperdiçar verba.</p></div>
<ol class="steps steps-4">
<li><h3>Diagnóstico e auditoria</h3><p>Analisamos suas contas de anúncio, site, oferta e atendimento no WhatsApp para descobrir onde o dinheiro está vazando.</p></li>
<li><h3>Campanhas enxutas</h3><p>Estruturamos poucas campanhas, bem segmentadas, focadas nos procedimentos que dão mais retorno para a sua clínica.</p></li>
<li><h3>Otimização semanal</h3><p>Ajustamos termos de pesquisa, públicos, criativos e lances com base em dados — não em achismo.</p></li>
<li><h3>Escala com controle</h3><p>Com custo por lead estável, aumentamos a verba aos poucos e expandimos para novos procedimentos ou canais.</p></li>
</ol></div></section>'''


def author_box():
    img = picture("arno-hoberg-avatar", [96, 192], 96, 96, "Arno Hoberg, gestor de tráfego pago para clínicas", "72px")
    return (f'<div class="author-box">{img}<p><strong>Quem cuida da sua conta:</strong> Arno Hoberg, gestor de tráfego pago '
            f'dedicado exclusivamente a clínicas de dermatologia, estética avançada e procedimentos faciais. '
            f'<a href="@/sobre/">Conheça a trajetória</a>.</p></div>')


def lead_form(origem, button, extra_fields="", thanks="../obrigado/"):
    i = origem
    return f'''<form class="form" data-lead="{origem}" data-thanks="{thanks}" novalidate>
<div class="form-row">
<div class="field"><label for="{i}-nome">Seu nome</label><input id="{i}-nome" name="nome" type="text" autocomplete="name" required aria-describedby="{i}-nome-erro"><span class="field-error" id="{i}-nome-erro" aria-live="polite"></span></div>
<div class="field"><label for="{i}-whats">WhatsApp com DDD</label><input id="{i}-whats" name="whatsapp" type="tel" inputmode="tel" autocomplete="tel-national" placeholder="(11) 99999-9999" required aria-describedby="{i}-whats-erro"><span class="field-error" id="{i}-whats-erro" aria-live="polite"></span></div>
</div>
<div class="form-row">
<div class="field"><label for="{i}-clinica">Nome da clínica</label><input id="{i}-clinica" name="clinica" type="text" autocomplete="organization" required aria-describedby="{i}-clinica-erro"><span class="field-error" id="{i}-clinica-erro" aria-live="polite"></span></div>
<div class="field"><label for="{i}-esp">Especialidade</label><select id="{i}-esp" name="especialidade" required aria-describedby="{i}-esp-erro">
<option value="">Selecione</option><option>Dermatologia</option><option>Estética avançada</option><option>Harmonização / procedimentos faciais</option><option>Odontologia estética / HOF</option><option>Outra</option></select><span class="field-error" id="{i}-esp-erro" aria-live="polite"></span></div>
</div>
{extra_fields}
<div class="hp" aria-hidden="true"><label for="{i}-site">Não preencha</label><input id="{i}-site" name="website" type="text" tabindex="-1" autocomplete="off"></div>
<div class="consent"><input id="{i}-lgpd" name="consentimento_lgpd" type="checkbox" required aria-describedby="{i}-lgpd-erro"><label for="{i}-lgpd">Concordo em ser contatado(a) por WhatsApp sobre este pedido e com a <a href="@/politica-de-privacidade/">Política de Privacidade</a>. Posso cancelar quando quiser.</label></div>
<span class="field-error" id="{i}-lgpd-erro" aria-live="polite"></span>
<button class="btn btn-primary" type="submit">{button}</button>
<p class="form-msg" role="status" aria-live="polite"></p>
</form>'''


def quote_form(fid="orcamento"):
    opts = [("Google Ads", "Google Ads"), ("Meta Ads", "Meta Ads (Instagram/Facebook)"),
            ("Site/landing page", "Site ou landing page"), ("Automação de WhatsApp", "Automação de WhatsApp"),
            ("SEO", "SEO")]
    boxes = "".join(f'<label class="option"><input type="checkbox" name="servico" value="{v}"> {l}</label>' for v, l in opts)
    return f'''<form class="form" data-quote novalidate aria-labelledby="{fid}-titulo">
<fieldset class="fieldset"><legend>Quais serviços você procura?</legend><div class="options">{boxes}</div></fieldset>
<div class="form-row">
<div class="field"><label for="{fid}-esp">Especialidade da clínica</label><select id="{fid}-esp" name="especialidade"><option value="">Selecione</option><option>Dermatologia</option><option>Estética avançada</option><option>Harmonização / procedimentos faciais</option><option>Odontologia estética / HOF</option><option>Outra</option></select></div>
<div class="field"><label for="{fid}-verba">Quanto investe hoje em anúncios?</label><select id="{fid}-verba" name="verba"><option value="">Selecione</option><option>Ainda não invisto</option><option>Até R$ 600/mês</option><option>De R$ 600 a R$ 1.500/mês</option><option>De R$ 1.500 a R$ 3.000/mês</option><option>Acima de R$ 3.000/mês</option></select></div>
</div>
<button class="btn btn-primary" type="submit">{ICONS["wa"]}<span>Solicitar orçamento no WhatsApp</span></button>
<p class="form-msg" role="status" aria-live="polite"></p>
<p class="note mb-0">O questionário só monta a mensagem do WhatsApp; nada é armazenado.</p>
</form>'''


# ---------------------------------------------------------------- schema
ORG_ID = f"{URL}/#organizacao"
SITE_ID = f"{URL}/#website"
PS_ID = f"{URL}/#consultoria"
PERSON_ID = f"{URL}/#arno-hoberg"


def base_schema():
    return [
        {"@type": "Organization", "@id": ORG_ID, "name": BRAND, "url": f"{URL}/",
         "logo": {"@type": "ImageObject", "url": f"{URL}/assets/img/logo-arno-hoberg-512.png", "width": 512, "height": 512},
         "founder": {"@id": PERSON_ID}, "areaServed": {"@type": "Country", "name": "Brasil"},
         "contactPoint": {"@type": "ContactPoint", "contactType": "customer service", "areaServed": "BR",
                          "availableLanguage": "Portuguese", "url": f"{URL}/contato/"}},
        {"@type": "WebSite", "@id": SITE_ID, "url": f"{URL}/", "name": BRAND, "inLanguage": "pt-BR",
         "publisher": {"@id": ORG_ID}},
    ]


def person_schema():
    return {"@type": "Person", "@id": PERSON_ID, "name": "Arno Hoberg", "jobTitle": "Gestor de tráfego pago",
            "worksFor": {"@id": ORG_ID}, "url": f"{URL}/sobre/",
            "image": f"{URL}/assets/img/arno-hoberg-consultor-trafego-pago-clinicas-960.webp",
            "knowsAbout": ["Google Ads", "Meta Ads", "Tráfego pago para clínicas de estética", "SEO", "Landing pages"]}


def professional_service_schema():
    return {"@type": "ProfessionalService", "@id": PS_ID, "name": BRAND, "url": f"{URL}/",
            "image": f"{URL}/assets/img/og-image.jpg", "logo": f"{URL}/assets/img/logo-arno-hoberg-512.png",
            "description": "Consultoria de tráfego pago (Google Ads e Meta Ads), criação de sites e landing pages, automação de WhatsApp e SEO para clínicas de dermatologia, estética avançada e procedimentos faciais. Atendimento 100% online.",
            "areaServed": {"@type": "Country", "name": "Brasil"}, "parentOrganization": {"@id": ORG_ID},
            "founder": {"@id": PERSON_ID}, "priceRange": "A partir de R$ 1.200/mês",
            "knowsLanguage": "pt-BR"}


def service_schema(name, stype, desc, path):
    return {"@type": "Service", "@id": f"{URL}/{path}#servico", "name": name, "serviceType": stype,
            "description": desc, "url": f"{URL}/{path}", "provider": {"@id": ORG_ID},
            "areaServed": {"@type": "Country", "name": "Brasil"},
            "audience": {"@type": "BusinessAudience", "audienceType": "Clínicas de dermatologia, estética avançada e procedimentos faciais"}}


def faq_schema(items):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": strip_tags(q), "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}}
        for q, a in items]}


def breadcrumb_schema(crumbs):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": f"{URL}/{p}"} for i, (n, p) in enumerate(crumbs)]}
