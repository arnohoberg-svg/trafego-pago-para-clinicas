from lib import *


def hero_simple(eyebrow, h1, lead, actions, side=""):
    grid = f'<div class="hero-grid" style="margin-top:20px"><div><p class="eyebrow">{eyebrow}</p><h1 id="titulo-principal">{h1}</h1><p class="lead">{lead}</p><div class="hero-actions">{actions}</div></div>{side}</div>' if side else \
        f'<div style="margin-top:20px;max-width:820px"><p class="eyebrow">{eyebrow}</p><h1 id="titulo-principal">{h1}</h1><p class="lead">{lead}</p><div class="hero-actions">{actions}</div></div>'
    return f'<section class="hero" aria-labelledby="titulo-principal"><div class="container">[[CRUMBS]]{grid}</div></section>'


PAGES = []

# ======================================================================= PREÇOS
p_wa = MSG_GENERIC
p_faq = [
    ("Quanto custa um gestor de tráfego para clínica?",
     "<p>Aqui, a gestão de tráfego começa em <strong>R$ 1.200 por mês</strong>. O valor final depende dos canais (Google Ads, Meta Ads ou ambos) e da quantidade de procedimentos e campanhas.</p>"),
    ("A verba dos anúncios está inclusa na gestão?",
     "<p>Não. A verba é paga diretamente ao Google e à Meta, no cartão ou boleto da clínica. Isso garante transparência: você vê exatamente quanto foi investido em cada plataforma.</p>"),
    ("Qual a verba mínima para anunciar?",
     "<p>Recomendamos no mínimo <strong>R$ 600 por mês (cerca de R$ 20 por dia)</strong>. Com menos que isso, as campanhas demoram a coletar dados e os testes ficam pouco confiáveis.</p>"),
    ("Por que o contrato mínimo é de 3 meses?",
     "<p>O primeiro mês é de estruturação e aprendizado das plataformas; o segundo e o terceiro são de otimização. Avaliar tráfego pago em menos tempo costuma levar a conclusões erradas.</p>"),
    ("Quanto custa um site ou uma automação?",
     "<p>Criação de sites, landing pages, automação de WhatsApp e SEO são <strong>sob orçamento</strong>, porque variam muito conforme o escopo. Use o questionário desta página para pedir o seu.</p>"),
    ("Existe taxa de setup?",
     "<p>Eventuais custos de implantação são informados no orçamento, antes de qualquer contratação. Não há cobranças escondidas.</p>"),
]
PRICE_ROWS = [
    ("Somente Google Ads", "Gestão a partir de R$ 1.200/mês — orçamento personalizado"),
    ("Somente Meta Ads (Instagram e Facebook)", "Gestão a partir de R$ 1.200/mês — orçamento personalizado"),
    ("Google Ads + Meta Ads", "Orçamento personalizado conforme campanhas e procedimentos"),
    ("Site institucional ou landing page", "Sob orçamento"),
    ("Automação de WhatsApp", "Sob orçamento"),
    ("SEO para clínicas", "Sob orçamento"),
]
rows = "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in PRICE_ROWS)
price_side = '''<aside class="price-box" aria-label="Resumo de preços"><p class="price-from">Gestão de tráfego pago</p>
<p class="price-value">a partir de R$ 1.200 <small>/mês</small></p>
<ul class="checklist"><li>Verba mínima recomendada: R$ 600/mês (R$ 20/dia)</li><li>Verba paga direto ao Google e à Meta</li><li>Contrato mínimo de 3 meses</li><li>Sites, automação e SEO sob orçamento</li></ul></aside>'''
PAGES.append({
    "path": "precos/", "title": "Quanto Custa Tráfego Pago para Clínica? Preços e Verba",
    "desc": "Quanto custa tráfego pago para clínica: gestão a partir de R$ 1.200/mês, verba mínima de R$ 600/mês e contrato de 3 meses. Monte seu orçamento no WhatsApp.",
    "crumbs": [("Início", ""), ("Preços", "precos/")], "faq": p_faq, "wa_msg": p_wa,
    "schema": [professional_service_schema(), {
        "@type": "Service", "@id": f"{URL}/precos/#gestao", "name": "Gestão de tráfego pago para clínicas de estética",
        "serviceType": "Gestão de anúncios Google Ads e Meta Ads", "provider": {"@id": ORG_ID},
        "areaServed": {"@type": "Country", "name": "Brasil"}, "url": f"{URL}/precos/",
        "offers": {"@type": "Offer", "url": f"{URL}/precos/", "priceCurrency": "BRL", "availability": "https://schema.org/InStock",
                   "description": "Gestão de tráfego pago a partir de R$ 1.200 por mês. Verba de anúncios à parte (mínimo recomendado R$ 600/mês). Contrato mínimo de 3 meses.",
                   "priceSpecification": {"@type": "UnitPriceSpecification", "minPrice": 1200, "priceCurrency": "BRL",
                                          "unitCode": "MON", "unitText": "mês"}}}],
    "body": hero_simple("Preços e investimento", "Quanto custa tráfego pago para clínica: preços claros, sem surpresas",
                        "Gestão a partir de R$ 1.200 por mês, verba de anúncios separada e paga direto às plataformas, contrato mínimo de 3 meses. Veja o que está incluso e como montar o orçamento ideal para a sua clínica.",
                        wa_btn(p_wa, "Pedir orçamento no WhatsApp", loc="hero") + '<a class="btn btn-secondary" href="#monte-orcamento">Montar orçamento</a>', price_side) + f'''
<section class="section" aria-labelledby="tabela-titulo">
<div class="container split">
<div><span class="eyebrow">Por serviço</span><h2 id="tabela-titulo">Preço da gestão de tráfego por serviço</h2>
<p>O valor da gestão é definido pelo escopo: quantos canais, quantas campanhas e quantos procedimentos serão trabalhados. Clínicas que estão começando costumam iniciar com um canal e ampliar depois.</p>
<p>Em todos os casos, você recebe uma proposta por escrito antes de qualquer contratação.</p></div>
<div><div class="table-wrap"><table class="price-table"><caption class="visually-hidden">Preços por serviço</caption><thead><tr><th scope="col">Serviço</th><th scope="col">Investimento</th></tr></thead><tbody>{rows}</tbody></table></div>
<p class="note">Valores de gestão não incluem a verba de anúncios. TikTok Ads: em breve.</p></div>
</div></section>

<section class="section section-alt" aria-labelledby="verba-titulo">
<div class="container split">
<div><span class="eyebrow">Verba de anúncios</span><h2 id="verba-titulo">Quanto investir em tráfego pago para clínica</h2>
<p><strong>Resposta curta:</strong> comece com pelo menos <strong>R$ 600 por mês</strong> em anúncios, o que dá cerca de <strong>R$ 20 por dia</strong>. Esse valor é pago diretamente ao Google e/ou à Meta e é separado da gestão.</p>
<p>Esse mínimo permite que as plataformas coletem dados suficientes para otimizar a entrega. Abaixo disso, as campanhas tendem a ficar instáveis e os testes, inconclusivos.</p></div>
<div><h3>Quando vale investir mais que o mínimo</h3>
<ul class="checklist"><li>Clínicas em capitais ou cidades com muita concorrência</li><li>Quando se quer trabalhar vários procedimentos ao mesmo tempo</li><li>Quando Google Ads e Meta Ads rodam juntos</li><li>Quando a agenda tem capacidade para receber mais avaliações</li></ul>
<p>O aumento de verba é sempre gradual e baseado no custo por contato que a conta já está entregando.</p></div>
</div></section>

<section class="section" aria-labelledby="incluso-titulo">
<div class="container split">
<div><span class="eyebrow">O que está incluso</span><h2 id="incluso-titulo">O que a gestão de tráfego inclui</h2>
<ul class="checklist"><li>Diagnóstico inicial e planejamento das campanhas</li><li>Criação e configuração das campanhas e conversões</li><li>Textos e edição de criativos de anúncio</li><li>Otimizações semanais</li><li>Relatório mensal com custo por contato</li><li>Reunião mensal de alinhamento por vídeo</li><li>Suporte pelo WhatsApp em horário comercial</li></ul></div>
<div><h3>Por que o contrato mínimo é de 3 meses</h3>
<p>Tráfego pago tem fase de aprendizado. No primeiro mês, as campanhas são estruturadas e as plataformas aprendem quem converte. No segundo e no terceiro, cortamos desperdícios e reforçamos o que funciona. Encerrar antes disso costuma desperdiçar justamente o investimento de aprendizado.</p>
<h3>Como medir o retorno do investimento</h3>
<ol><li><strong>Custo por contato</strong> = verba investida ÷ número de contatos recebidos.</li><li><strong>Taxa de agendamento</strong> = avaliações marcadas ÷ contatos recebidos.</li><li><strong>Custo por paciente</strong> = (verba + gestão) ÷ novos pacientes atendidos.</li></ol>
<p>Compare o custo por paciente com o valor médio dos procedimentos para saber se a conta está dando retorno. Ajudamos você a montar esse controle.</p></div>
</div></section>

<section class="section section-alt" id="monte-orcamento" aria-labelledby="orcamento-titulo">
<div class="container split">
<div><span class="eyebrow">Orçamento</span><h2 id="orcamento-titulo">Solicitar orçamento</h2>
<p>Marque os serviços que interessam, informe a especialidade e quanto investe hoje. O questionário monta uma mensagem pronta e abre o WhatsApp.</p>
<p>Ainda em dúvida sobre por onde começar? Peça antes uma <a href="@/auditoria-gratuita-de-anuncios/">auditoria gratuita de anúncios</a> ou veja os serviços de <a href="@/google-ads-para-clinicas-esteticas/">Google Ads</a> e <a href="@/meta-ads-para-clinicas-esteticas/">Meta Ads para clínicas</a>.</p></div>
<div class="form-card">{quote_form("orcamento")}</div>
</div></section>

[[FAQ]]

{cta_band("Prefere conversar antes de decidir?", "Explico como funcionaria para a sua clínica e qual investimento faz sentido, sem compromisso.", p_wa, "cta_final")}
'''})

# ======================================================================= AUDITORIA
au_wa = MSG_AUDIT
au_faq = [
    ("A auditoria é realmente gratuita?",
     "<p>Sim. Você não paga nada e não assume compromisso de contratar. É a forma que temos de mostrar como trabalhamos.</p>"),
    ("Preciso dar acesso à minha conta?",
     "<p>Para uma análise completa, sim: você concede acesso de leitura ao Google Ads e/ou ao Gerenciador de Negócios da Meta, que pode ser removido a qualquer momento. Também é possível fazer uma análise preliminar por chamada de vídeo com compartilhamento de tela.</p>"),
    ("E se eu ainda não anuncio?",
     "<p>Sem problema. Nesse caso analisamos o site, o perfil, o atendimento no WhatsApp e a concorrência na sua região, e indicamos por onde começar.</p>"),
    ("Quanto tempo leva?",
     "<p>Depois do acesso concedido, a análise costuma ser concluída em poucos dias úteis e é apresentada em uma conversa por vídeo.</p>"),
    ("Por que meus anúncios não trazem pacientes?",
     "<p>Os motivos mais comuns são público ou palavras-chave amplas demais, objetivo de campanha errado, página de destino fraca, ausência de medição e demora no atendimento. A auditoria aponta quais deles estão afetando a sua conta.</p>"),
]
au_form = f'''<div class="form-card" id="formulario"><h2 id="form-titulo">Solicite sua auditoria gratuita</h2><p class="note">Leva menos de 1 minuto. Respondo pelo WhatsApp.</p>
{lead_form("auditoria", "Quero minha auditoria gratuita", extra_fields='<div class="field"><label for="auditoria-plat">Onde você anuncia hoje?</label><select id="auditoria-plat" name="plataforma"><option value="">Selecione</option><option>Google Ads</option><option>Meta Ads (Instagram/Facebook)</option><option>Google e Meta</option><option>Só impulsiono posts</option><option>Ainda não anuncio</option></select></div>')}</div>'''
retrato = picture("arno-hoberg-retrato", [400, 800], 800, 800, "Retrato em preto e branco de Arno Hoberg, que realiza as auditorias de anúncios",
                  "(min-width: 900px) 360px, 92vw", cls="media-rounded")
PAGES.append({
    "path": "auditoria-gratuita-de-anuncios/", "title": "Auditoria Gratuita de Anúncios para Clínicas | Google e Meta",
    "desc": "Auditoria gratuita de anúncios para clínicas: análise do Google Ads e do Meta Ads para descobrir onde sua verba vaza. Solicite agora, sem compromisso.",
    "crumbs": [("Início", ""), ("Auditoria gratuita", "auditoria-gratuita-de-anuncios/")], "faq": au_faq,
    "schema": [service_schema("Auditoria gratuita de anúncios para clínicas", "Auditoria de contas de Google Ads e Meta Ads",
                              "Análise gratuita de contas de anúncios de clínicas de estética e dermatologia, com diagnóstico de desperdícios e oportunidades.", "auditoria-gratuita-de-anuncios/")],
    "body": f'''<section class="hero" aria-labelledby="titulo-principal"><div class="container">[[CRUMBS]]
<div class="hero-grid" style="margin-top:20px">
<div><p class="eyebrow">Isca gratuita · sem compromisso</p><h1 id="titulo-principal">Auditoria gratuita de anúncios para clínicas: descubra onde sua verba está vazando</h1>
<p class="lead">Analiso suas campanhas de Google Ads e Meta Ads, sua página de destino e seu atendimento no WhatsApp, e mostro com clareza o que corrigir primeiro, mesmo que você decida não contratar.</p>
<div class="hero-actions"><a class="btn btn-primary" href="#formulario">Preencher formulário</a>{wa_btn(au_wa, "Pedir pelo WhatsApp", "btn btn-secondary", "hero")}</div>
<ul class="hero-points"><li>Diagnóstico individual, feito por mim, não por robô</li><li>Apresentação por vídeo com prioridades claras</li><li>Acesso de leitura, removível a qualquer momento</li></ul></div>
{au_form}
</div></div></section>

<section class="section" aria-labelledby="analise-titulo">
<div class="container"><div class="section-head"><span class="eyebrow">O que analisamos</span><h2 id="analise-titulo">O que entra na análise da sua conta de anúncios</h2>
<p>Uma auditoria de verdade vai além de olhar o painel. Seguimos o caminho completo do paciente: do anúncio até a conversa no WhatsApp.</p></div>
<div class="grid grid-3">
<article class="card"><h3>Google Ads</h3><ul class="checklist"><li>Estrutura de campanhas e grupos</li><li>Palavras-chave e termos de pesquisa</li><li>Palavras negativas e segmentação geográfica</li><li>Conversões configuradas e Índice de Qualidade</li></ul></article>
<article class="card"><h3>Meta Ads</h3><ul class="checklist"><li>Objetivos de campanha</li><li>Públicos, exclusões e faixa etária</li><li>Criativos, frequência e reprovações</li><li>Pixel, eventos e API de Conversões</li></ul></article>
<article class="card"><h3>Página e WhatsApp</h3><ul class="checklist"><li>Velocidade e clareza da página de destino</li><li>Caminho até o WhatsApp</li><li>Tempo e qualidade da primeira resposta</li><li>Conformidade com regras de publicidade</li></ul></article>
</div></div></section>

<section class="section section-alt" aria-labelledby="como-titulo">
<div class="container"><div class="section-head"><span class="eyebrow">Como funciona</span><h2 id="como-titulo">Como funciona a auditoria gratuita</h2></div>
<ol class="steps steps-4"><li><h3>Você preenche o formulário</h3><p>Nome, WhatsApp, clínica e especialidade. Leva menos de um minuto.</p></li>
<li><h3>Combinamos o acesso</h3><p>Envio pelo WhatsApp o passo a passo para liberar acesso de leitura às contas.</p></li>
<li><h3>Análise detalhada</h3><p>Reviso campanhas, página e atendimento e organizo as oportunidades por prioridade.</p></li>
<li><h3>Apresentação por vídeo</h3><p>Mostro o diagnóstico e o que eu faria. Você decide, sem pressão, se quer seguir comigo.</p></li></ol></div></section>

<section class="section" aria-labelledby="sinais-titulo">
<div class="container split split-media"><div>{retrato}</div>
<div><span class="eyebrow">Diagnóstico de tráfego pago para clínica</span><h2 id="sinais-titulo">Sinais de que sua conta precisa de uma auditoria</h2>
<ul class="xlist"><li>O custo por contato subiu e você não sabe por quê</li><li>Recebe mensagens de pessoas de outras cidades ou fora do perfil</li><li>Seus anúncios são reprovados com frequência</li><li>Não sabe quantos pacientes vieram dos anúncios</li><li>Só impulsiona posts e nunca usou o Gerenciador de Anúncios</li><li>Trocou de agência e não sabe o que foi feito na conta</li></ul>
<p>Se você se identificou com dois ou mais itens, provavelmente há verba sendo desperdiçada. Conheça também como trabalho com <a href="@/google-ads-para-clinicas-esteticas/">Google Ads</a> e <a href="@/meta-ads-para-clinicas-esteticas/">Meta Ads para clínicas</a>, e os <a href="@/precos/">preços da gestão</a>.</p></div>
</div></section>

[[FAQ]]

{cta_band("Prefere pedir pelo WhatsApp?", "Mande uma mensagem e eu explico o passo a passo da auditoria.", au_wa, "cta_final")}
'''})

# ======================================================================= E-BOOK
e_wa = MSG_GENERIC
ebook_img = picture("arno-hoberg-retrato", [400, 800], 800, 800, "Arno Hoberg, autor do e-book sobre tráfego pago para clínicas",
                    "(min-width: 900px) 360px, 92vw", cls="media-rounded")
PAGES.append({
    "path": "ebook/", "title": "E-book Grátis: Tráfego Pago para Clínicas de Estética",
    "desc": "Baixe grátis o e-book de tráfego pago para clínicas de estética: verba, erros comuns e regras de anúncios em saúde. Preencha o formulário e receba agora.",
    "crumbs": [("Início", ""), ("E-book gratuito", "ebook/")], "wa_msg": e_wa,
    "notes": "<!-- DEFINIR TEMA DO E-BOOK: título, subtítulo e tópicos desta página são provisórios. Atualize H1, title, description e a lista 'O que você vai aprender'. Configure ebookUrl em assets/js/main.js. -->",
    "schema": [],
    "body": f'''<section class="hero" aria-labelledby="titulo-principal"><div class="container">[[CRUMBS]]
<div class="hero-grid" style="margin-top:20px">
<div><p class="eyebrow">Material gratuito</p>
<!-- TÍTULO PROVISÓRIO DO E-BOOK — substituir quando o tema for definido -->
<h1 id="titulo-principal">E-book gratuito: guia prático de tráfego pago para clínicas de estética</h1>
<p class="lead">Um material direto ao ponto para donos de clínica que querem entender quanto investir, quais erros evitar e como anunciar dentro das regras, antes de gastar mais um real em anúncios.</p>
<div class="hero-actions"><a class="btn btn-primary" href="#formulario">Quero o e-book</a>{wa_btn(e_wa, "Receber pelo WhatsApp", "btn btn-secondary", "hero")}</div></div>
<div class="form-card" id="formulario"><h2 id="form-titulo">Receba o e-book gratuitamente</h2><p class="note">Preencha os dados e libere o download na hora.</p>{lead_form("ebook", "Baixar e-book gratuito")}</div>
</div></div></section>

<section class="section" aria-labelledby="aprender-titulo">
<div class="container split split-media"><div>{ebook_img}</div>
<div><span class="eyebrow">Conteúdo</span><h2 id="aprender-titulo">O que você vai aprender</h2>
<!-- TÓPICOS PROVISÓRIOS — ajustar conforme o tema definitivo -->
<ul class="checklist"><li>Como definir a verba inicial de anúncios da clínica</li><li>Google Ads ou Instagram: qual escolher para cada procedimento</li><li>Os erros mais comuns que encarecem o custo por contato</li><li>Checklist de regras de publicidade em saúde antes de publicar</li><li>Como medir quantos pacientes vieram dos anúncios</li></ul>
<p>Enquanto isso, você também pode ler o <a href="@/regras-de-publicidade-para-clinicas/">guia de regras de publicidade para clínicas</a> ou pedir uma <a href="@/auditoria-gratuita-de-anuncios/">auditoria gratuita dos seus anúncios</a>.</p></div>
</div></section>

<section class="section section-alt" aria-labelledby="para-quem-titulo">
<div class="container"><div class="section-head"><span class="eyebrow">Para quem é</span><h2 id="para-quem-titulo">Para quem é este e-book</h2></div>
<div class="grid grid-3">
<article class="card"><h3>Clínicas que ainda não anunciam</h3><p>Para começar do jeito certo, sem desperdiçar os primeiros meses de verba.</p></article>
<article class="card"><h3>Quem só impulsiona posts</h3><p>Para entender a diferença entre impulsionar e fazer campanhas de verdade.</p></article>
<article class="card"><h3>Quem já investe e quer melhorar</h3><p>Para identificar onde o custo por contato pode cair.</p></article>
</div></div></section>

{cta_band("Prefere tirar dúvidas direto comigo?", "Fale no WhatsApp e eu indico o melhor próximo passo para a sua clínica.", e_wa, "cta_final")}
'''})

# ======================================================================= SOBRE
so_wa = MSG_GENERIC
sobre_img = picture("arno-hoberg-consultor-trafego-pago-clinicas", [480, 960], 960, 960,
                    "Arno Hoberg, consultor de tráfego pago para clínicas de estética e dermatologia",
                    "(min-width: 900px) 420px, 92vw", eager=True)
PAGES.append({
    "path": "sobre/", "title": "Sobre Arno Hoberg | Gestor de Tráfego para Clínicas",
    "desc": "Conheça Arno Hoberg, gestor de tráfego pago especializado em clínicas de estética e dermatologia. Método próprio e campanhas enxutas. Fale no WhatsApp.",
    "crumbs": [("Início", ""), ("Sobre", "sobre/")], "wa_msg": so_wa, "og_type": "profile",
    "schema": [person_schema(), professional_service_schema()],
    "body": f'''<section class="hero" aria-labelledby="titulo-principal"><div class="container">[[CRUMBS]]
<div class="hero-grid" style="margin-top:20px">
<div><p class="eyebrow">Sobre</p><h1 id="titulo-principal">Arno Hoberg, gestor de tráfego pago para clínicas de estética</h1>
<p class="lead">Ajudo clínicas de dermatologia, estética avançada e procedimentos faciais a atrair mais pessoas interessadas com anúncios enxutos, sites que convertem e atendimento ágil no WhatsApp.</p>
<div class="hero-actions">{wa_btn(so_wa, loc="hero")}{audit_btn("Auditoria gratuita", loc="hero_auditoria")}</div></div>
<div class="hero-media">{sobre_img}</div>
</div></div></section>

<section class="section" aria-labelledby="porque-titulo">
<div class="container split">
<div><span class="eyebrow">Especialização</span><h2 id="porque-titulo">Por que escolhi trabalhar só com clínicas</h2>
<p>Ao longo do tempo percebi que clínicas de saúde e estética têm desafios muito diferentes dos outros negócios: o paciente pesquisa bastante, a confiança decide mais que o preço e a publicidade é limitada por conselhos profissionais, pela Anvisa e por políticas rígidas do Google e da Meta.</p>
<p>Atender um único nicho me permite conhecer de perto esse cenário: quais procedimentos geram mais procura em cada época, que tipo de criativo é aprovado, quais palavras-chave trazem curiosos e quais trazem pacientes.</p>
<!-- CONFIRMAR: dado "60 clientes" — é média de contatos no primeiro mês ou total de clientes atendidos? Não publicar até validar. --></div>
<div><h3>Especialista em tráfego para clínicas estéticas</h3>
<p>Trabalho com Google Ads, Meta Ads (Instagram e Facebook), criação de sites e landing pages, automação de atendimento no WhatsApp e SEO. TikTok Ads está em preparação.</p>
<h3>Consultor de marketing digital, não um painel de métricas</h3>
<p>Meu papel é traduzir números em decisões: onde investir, o que pausar, que procedimento priorizar. Você fala diretamente comigo.</p></div>
</div></section>

<section class="section section-alt" aria-labelledby="como-trabalho-titulo">
<div class="container"><div class="section-head"><span class="eyebrow">Princípios</span><h2 id="como-trabalho-titulo">Como eu trabalho</h2></div>
<div class="grid grid-4">
<article class="card"><h3>Campanhas enxutas</h3><p>Poucas campanhas, bem feitas, concentrando verba onde existe intenção real de agendar.</p></article>
<article class="card"><h3>Transparência</h3><p>Contas no nome da clínica, verba paga direto às plataformas e relatórios com custo por contato.</p></article>
<article class="card"><h3>Ética em primeiro lugar</h3><p>Nada de promessas de resultado ou “antes e depois” fora das regras. A reputação da sua clínica vem primeiro.</p></article>
<article class="card"><h3>Comunicação direta</h3><p>Reuniões mensais por vídeo e contato pelo WhatsApp, sem intermediários.</p></article>
</div></div></section>

{how_it_works(dark=True, title="Meu método em 4 etapas")}

{cta_band("Vamos conversar sobre a sua clínica?", "Conte seu momento atual e eu digo, com sinceridade, se e como posso ajudar.", so_wa, "cta_final", ("precos/", "Ver preços"))}
'''})

# ======================================================================= REGRAS DE PUBLICIDADE
r_wa = MSG_GENERIC
r_faq = [
    ("Clínica de estética pode postar antes e depois?",
     "<p>Depende do conselho do profissional responsável e do canal. Para médicos, a Resolução CFM nº 2.336/2023 passou a admitir o uso em situações específicas, com finalidade educativa e uma série de condições; na Meta, anúncios com “antes e depois” de saúde e aparência são, em regra, proibidos. Consulte sempre a norma vigente do seu conselho.</p>"),
    ("Pode anunciar botox no Instagram ou no Google?",
     "<p>A toxina botulínica é medicamento de venda sob prescrição, e a legislação sanitária restringe a propaganda desse tipo de produto ao público leigo. Na prática, recomenda-se não citar marcas comerciais nem colocar o produto como protagonista do anúncio, comunicando o procedimento e a avaliação profissional com cautela.</p>"),
    ("Posso prometer resultado em um anúncio de clínica?",
     "<p>Não é recomendável. Garantir resultados é vedado ou restrito pelos conselhos profissionais e pode configurar publicidade enganosa pelo Código de Defesa do Consumidor, além de violar políticas do Google e da Meta.</p>"),
    ("Quem é responsável pelo conteúdo do anúncio?",
     "<p>O profissional e a clínica respondem eticamente pelo que é divulgado em seu nome, mesmo quando a campanha é feita por uma agência. Por isso, toda peça deve ser revisada pelo responsável técnico antes da publicação.</p>"),
    ("Preciso de consentimento para usar dados dos leads?",
     "<p>Sim, é preciso ter uma base legal na LGPD. Para comunicações de marketing, o consentimento claro é o caminho mais seguro; e qualquer dado de saúde é dado sensível, com regras mais rígidas.</p>"),
]
rules_aside = f'''<aside><div class="aside-sticky"><div class="form-card"><p class="footer-title" style="color:var(--ink)">Quer anunciar com segurança?</p>
<p class="note">Campanhas criadas considerando as regras do seu conselho e das plataformas.</p>{wa_btn(r_wa, "Falar no WhatsApp", "btn btn-primary btn-sm", "aside")}
<p class="note mt-2 mb-0">Veja também: <a href="@/meta-ads-para-clinicas-esteticas/">Meta Ads para clínicas</a> · <a href="@/google-ads-para-clinicas-esteticas/">Google Ads para clínicas</a> · <a href="@/auditoria-gratuita-de-anuncios/">Auditoria gratuita</a></p></div></div></aside>'''
PAGES.append({
    "path": "regras-de-publicidade-para-clinicas/", "title": "Regras de Publicidade para Clínicas de Estética: Guia",
    "desc": "Guia de regras de publicidade para clínicas de estética: CFM, conselhos, Anvisa, CDC, CONAR, Google Ads, Meta Ads e LGPD. Leia e anuncie com mais segurança.",
    "crumbs": [("Início", ""), ("Regras de publicidade", "regras-de-publicidade-para-clinicas/")], "faq": r_faq, "wa_msg": r_wa,
    "og_type": "article",
    "notes": "<!-- VALIDAÇÃO JURÍDICA OBRIGATÓRIA: revisar todo o conteúdo desta página com assessoria jurídica antes de publicar. Conferir se as normas citadas continuam vigentes na data da publicação. -->",
    "schema": [{"@type": "Article", "@id": f"{URL}/regras-de-publicidade-para-clinicas/#artigo",
                "headline": "Regras de publicidade para clínicas de estética: guia prático", "inLanguage": "pt-BR",
                "datePublished": LASTMOD, "dateModified": LASTMOD, "author": {"@id": PERSON_ID}, "publisher": {"@id": ORG_ID},
                "image": f"{URL}/assets/img/og-image.jpg",
                "mainEntityOfPage": f"{URL}/regras-de-publicidade-para-clinicas/"}, person_schema()],
    "body": hero_simple("Guia gratuito", "Regras de publicidade para clínicas de estética: guia prático para anunciar com segurança",
                        "Um resumo organizado das normas que afetam anúncios de clínicas de dermatologia, estética e procedimentos faciais: conselhos profissionais, Anvisa, Código de Defesa do Consumidor, CONAR, Google Ads, Meta Ads e LGPD.",
                        wa_btn(r_wa, loc="hero") + '<a class="btn btn-secondary" href="#checklist">Ir para o checklist</a>') + f'''
<section class="section" aria-label="Conteúdo do guia">
<div class="container layout-aside">
<article class="prose">
<div class="callout"><p><strong>Este conteúdo é informativo e não substitui orientação jurídica.</strong> As normas mudam com frequência: sempre consulte o texto oficial vigente do seu conselho profissional, da Anvisa e das plataformas, e valide suas peças com assessoria jurídica.</p>
<p class="note">Última revisão: <time datetime="{LASTMOD}">31 de outubro de 2026</time>. Autor: Arno Hoberg.</p></div>

<nav class="toc" aria-label="Sumário do guia"><p>Neste guia</p><ol>
<li><a href="#por-que">Por que as regras importam</a></li><li><a href="#cfm">Publicidade médica: CFM e CRM</a></li>
<li><a href="#conselhos">Outros conselhos profissionais</a></li><li><a href="#anvisa">Anvisa: medicamentos e produtos</a></li>
<li><a href="#cdc">Código de Defesa do Consumidor e CONAR</a></li><li><a href="#google">Políticas do Google Ads</a></li>
<li><a href="#meta">Políticas do Meta Ads</a></li><li><a href="#lgpd">LGPD e dados de leads</a></li>
<li><a href="#checklist">Checklist antes de publicar</a></li><li><a href="#fontes">Fontes oficiais</a></li></ol></nav>

<h2 id="por-que">Por que as regras de publicidade importam para clínicas</h2>
<p>Anúncios de saúde e estética estão sujeitos a várias camadas de regras ao mesmo tempo: a ética do conselho do profissional responsável, a legislação sanitária, a proteção do consumidor, a autorregulamentação publicitária e as políticas privadas de cada plataforma. Uma peça pode ser aceita pelo Instagram e, ainda assim, gerar um processo ético no conselho — ou o contrário.</p>
<p>As consequências vão de anúncios reprovados e contas de anúncio restritas até processos éticos, multas e danos à reputação da clínica. Por isso, a regra de ouro é: <strong>informar com responsabilidade, sem prometer resultados</strong>.</p>

<h2 id="cfm">Publicidade médica: regras do CFM e do CRM</h2>
<h3>Resolução CFM nº 2.336/2023</h3>
<p>A publicidade médica é regulada atualmente pela Resolução CFM nº 2.336/2023, que entrou em vigor em 2024 e substituiu a antiga Resolução CFM nº 1.974/2011. Ela trouxe flexibilizações — especialmente para o uso de redes sociais e de imagens — mas manteve proibições importantes. Leia o texto integral e o manual da comissão de divulgação (Codame) do CRM do seu estado.</p>
<h3>Pontos de atenção na publicidade médica</h3>
<ul>
<li>Identificação do médico com nome e número do CRM; ao anunciar especialidade, também o RQE (Registro de Qualificação de Especialista).</li>
<li>Proibição de garantir ou prometer resultados e de usar linguagem sensacionalista.</li>
<li>Cuidado ao divulgar especialidade ou título que o profissional não possua formalmente registrado.</li>
<li>Restrições a sorteios, brindes e condições comerciais usadas como chamariz — verifique o que a norma admite.</li>
</ul>
<h3>Imagens de “antes e depois” na medicina</h3>
<p>A resolução vigente passou a admitir imagens de pacientes, incluindo “antes e depois”, em contextos específicos e mediante condições (como finalidade educativa, consentimento do paciente e informações sobre indicações e limitações). Não interprete essa flexibilização como autorização ampla: confira as condições exatas no texto oficial e as orientações do seu CRM antes de usar qualquer imagem.</p>

<h2 id="conselhos">Outros conselhos profissionais (biomedicina, enfermagem, odontologia e mais)</h2>
<p>Muitas clínicas de estética contam com profissionais de diferentes categorias. Cada um responde ao seu próprio conselho, com regras próprias de publicidade e de escopo de atuação:</p>
<h3>Odontologia (CFO e CROs)</h3>
<p>A publicidade odontológica segue o Código de Ética Odontológica e resoluções do CFO, como a Resolução CFO nº 196/2019, que trata da divulgação de imagens de diagnóstico e resultado final. Harmonização orofacial é especialidade odontológica reconhecida pelo CFO; verifique as regras do seu CRO.</p>
<h3>Biomedicina (CFBM e CRBMs)</h3>
<p>Biomédicos com habilitação em estética devem observar o Código de Ética da profissão e as resoluções do CFBM sobre atuação em estética e publicidade.</p>
<h3>Enfermagem (Cofen e Corens)</h3>
<p>A atuação de enfermeiros em estética e a publicidade desses serviços são disciplinadas por resoluções do Cofen e pelo Código de Ética dos Profissionais de Enfermagem.</p>
<h3>Fisioterapia, farmácia e esteticistas</h3>
<p>Fisioterapeutas (Coffito/Crefitos) e farmacêuticos (CFF/CRFs) também têm normas próprias para estética. A profissão de esteticista é regulamentada pela Lei nº 13.643/2018. Em todos os casos, anuncie apenas procedimentos compatíveis com a habilitação do profissional responsável.</p>

<h2 id="anvisa">Anvisa: propaganda de medicamentos e produtos para saúde</h2>
<h3>Toxina botulínica e medicamentos sob prescrição</h3>
<p>A toxina botulínica é medicamento de venda sob prescrição. A legislação sanitária (Lei nº 6.360/1976, Lei nº 9.294/1996 e a RDC Anvisa nº 96/2008, entre outras) restringe a propaganda de medicamentos de prescrição ao público leigo. Na prática, evite citar marcas comerciais e não faça do produto o foco do anúncio.</p>
<h3>Preenchedores e outros produtos para saúde</h3>
<p>Preenchedores (como os de ácido hialurônico), fios e equipamentos são produtos regulados pela Anvisa. Divulgue o procedimento e a avaliação profissional, não o produto, e nunca anuncie produtos sem registro ou para uso diferente do aprovado.</p>

<h2 id="cdc">Código de Defesa do Consumidor e CONAR</h2>
<p>O Código de Defesa do Consumidor (Lei nº 8.078/1990) proíbe publicidade enganosa (que induz o consumidor a erro, inclusive por omissão) e abusiva (que explora medo, superstição ou desrespeita valores), e atribui ao anunciante o ônus de provar a veracidade do que afirma. Promessas como “resultado garantido” ou “sem riscos” são exemplos de alto risco.</p>
<p>O Código Brasileiro de Autorregulamentação Publicitária, aplicado pelo CONAR, também exige veracidade, responsabilidade social e cuidado especial com temas de saúde e com o público menor de idade.</p>

<h2 id="google">Políticas do Google Ads para saúde e estética</h2>
<ul>
<li><strong>Saúde e medicamentos:</strong> anúncios de medicamentos de venda sob prescrição são proibidos ou fortemente restritos no Brasil, o que inclui palavras-chave e textos com marcas comerciais.</li>
<li><strong>Publicidade personalizada:</strong> o Google limita o uso de categorias sensíveis de saúde em remarketing e públicos personalizados.</li>
<li><strong>Deturpação:</strong> afirmações enganosas ou irreais, como resultados garantidos, podem levar à reprovação de anúncios e à suspensão da conta.</li>
<li><strong>Conteúdo sensível:</strong> imagens que exploram nudez ou partes do corpo de forma sexualizada são restritas.</li>
</ul>
<p>As políticas são atualizadas com frequência; consulte a Central de Políticas do Google Ads antes de cada nova campanha. Veja como estruturamos campanhas de <a href="@/google-ads-para-clinicas-esteticas/">Google Ads para clínicas</a>.</p>

<h2 id="meta">Políticas do Meta Ads (Instagram e Facebook)</h2>
<ul>
<li><strong>Saúde e aparência pessoal:</strong> anúncios não podem conter imagens de “antes e depois” nem resultados inesperados ou improváveis, e não podem gerar autopercepção negativa.</li>
<li><strong>Atributos pessoais:</strong> o texto não pode afirmar ou insinuar características do leitor (ex.: “Você tem manchas no rosto?”). Prefira “Conheça o tratamento para manchas”.</li>
<li><strong>Procedimentos estéticos:</strong> anúncios de procedimentos cosméticos devem ser direcionados a pessoas com 18 anos ou mais.</li>
<li><strong>Segmentação:</strong> opções de segmentação detalhada ligadas a temas sensíveis, como condições de saúde, foram removidas.</li>
</ul>
<p>Saiba como trabalhamos com <a href="@/meta-ads-para-clinicas-esteticas/">Meta Ads para clínicas de estética</a> respeitando essas regras.</p>

<h2 id="lgpd">LGPD: dados de leads e de pacientes</h2>
<p>A Lei Geral de Proteção de Dados (Lei nº 13.709/2018) se aplica a todos os dados coletados por anúncios, formulários e WhatsApp. Dados de saúde são <strong>dados pessoais sensíveis</strong> e têm regras mais rígidas.</p>
<ul>
<li>Colete apenas o necessário (nome, contato e interesse) e informe a finalidade.</li>
<li>Tenha uma base legal adequada; para marketing, use consentimento claro e registrado.</li>
<li>Mantenha uma política de privacidade acessível e um canal para o titular exercer seus direitos.</li>
<li>Não use dados de pacientes (prontuários, imagens, diagnósticos) em anúncios ou públicos sem base legal e autorização específica.</li>
<li>Restrinja o acesso às conversas e listas de contatos e defina por quanto tempo os dados serão mantidos.</li>
</ul>
<p>Um bom ponto de partida é implementar <a href="@/automacao-whatsapp-para-clinicas/">automação de WhatsApp</a> que colete apenas o essencial e ofereça a opção de descadastro.</p>

<h2 id="checklist">Checklist antes de publicar um anúncio de clínica</h2>
<ol>
<li>O profissional responsável está identificado conforme exige o seu conselho?</li>
<li>O anúncio evita prometer ou garantir resultados?</li>
<li>Não há “antes e depois” fora das condições do conselho e das plataformas?</li>
<li>Nenhuma marca de medicamento de prescrição é citada?</li>
<li>O texto fala do procedimento, e não de um “defeito” do leitor?</li>
<li>O público está configurado para 18 anos ou mais em procedimentos estéticos?</li>
<li>Os procedimentos anunciados são compatíveis com a habilitação do profissional?</li>
<li>Formulários e WhatsApp seguem a LGPD, com consentimento e política de privacidade?</li>
<li>As imagens de pacientes têm autorização por escrito?</li>
<li>A peça foi revisada pelo responsável técnico da clínica?</li>
</ol>

<h2 id="fontes">Fontes oficiais para consulta</h2>
<ul>
<li><a href="https://portal.cfm.org.br/" target="_blank" rel="noopener">Conselho Federal de Medicina (CFM)</a> e o CRM do seu estado</li>
<li><a href="https://website.cfo.org.br/" target="_blank" rel="noopener">Conselho Federal de Odontologia (CFO)</a></li>
<li><a href="https://cfbm.gov.br/" target="_blank" rel="noopener">Conselho Federal de Biomedicina (CFBM)</a></li>
<li><a href="https://www.cofen.gov.br/" target="_blank" rel="noopener">Conselho Federal de Enfermagem (Cofen)</a></li>
<li><a href="https://www.gov.br/anvisa/" target="_blank" rel="noopener">Agência Nacional de Vigilância Sanitária (Anvisa)</a></li>
<li><a href="https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm" target="_blank" rel="noopener">Código de Defesa do Consumidor (Lei nº 8.078/1990)</a></li>
<li><a href="http://www.conar.org.br/" target="_blank" rel="noopener">CONAR — Código Brasileiro de Autorregulamentação Publicitária</a></li>
<li><a href="https://support.google.com/adspolicy/" target="_blank" rel="noopener">Central de Políticas do Google Ads</a></li>
<li><a href="https://transparency.meta.com/policies/ad-standards/" target="_blank" rel="noopener">Padrões de Publicidade da Meta</a></li>
<li><a href="https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm" target="_blank" rel="noopener">LGPD (Lei nº 13.709/2018)</a> e <a href="https://www.gov.br/anpd/" target="_blank" rel="noopener">ANPD</a></li>
</ul>
<p class="note">Este conteúdo é informativo e não substitui orientação jurídica. Nenhuma prática citada deve ser considerada automaticamente permitida: a aplicação depende do caso concreto, do conselho profissional e da versão vigente de cada norma.</p>
</article>
{rules_aside}
</div></section>

[[FAQ]]

{cta_band("Quer campanhas que respeitam essas regras?", "Crio e gerencio anúncios para clínicas pensando em resultado e em conformidade desde o primeiro dia.", r_wa, "cta_final", ("auditoria-gratuita-de-anuncios/", "Auditoria gratuita"))}
'''})

# ======================================================================= CONTATO
c_wa = MSG_GENERIC
c_form = f'''<div class="form-card"><h2 id="form-titulo">Prefere deixar uma mensagem?</h2><p class="note">Preencha e eu retorno pelo WhatsApp.</p>
{lead_form("contato", "Enviar mensagem", extra_fields='<div class="field"><label for="contato-msg">Mensagem (opcional)</label><textarea id="contato-msg" name="mensagem" rows="4"></textarea></div>')}</div>'''
PAGES.append({
    "path": "contato/", "title": "Contato | Gestor de Tráfego para Clínicas de Estética",
    "desc": "Fale com Arno Hoberg, gestor de tráfego para clínicas de estética e dermatologia. Atendimento 100% online para todo o Brasil. Chame agora no WhatsApp.",
    "crumbs": [("Início", ""), ("Contato", "contato/")], "wa_msg": c_wa,
    "schema": [professional_service_schema()],
    "body": f'''<section class="hero" aria-labelledby="titulo-principal"><div class="container">[[CRUMBS]]
<div class="hero-grid" style="margin-top:20px">
<div><p class="eyebrow">Contato</p><h1 id="titulo-principal">Contato: fale com um gestor de tráfego especializado em clínicas</h1>
<p class="lead">O caminho mais rápido é o WhatsApp: você fala diretamente comigo. O atendimento é 100% online, para clínicas de todo o Brasil.</p>
<div class="hero-actions">{wa_btn(c_wa, "Chamar no WhatsApp", loc="hero")}</div>
<ul class="hero-points"><li>Conversa inicial sem compromisso</li><li>Reuniões por videochamada</li><li>Sem endereço físico: atendimento online</li></ul>
<!-- E-MAIL DE CONTATO: adicionar quando definido, ex.: <p>E-mail: <a href="mailto:{{{{EMAIL}}}}">{{{{EMAIL}}}}</a></p> -->
</div>
{c_form}
</div></div></section>

<section class="section" aria-labelledby="proximos-titulo">
<div class="container"><div class="section-head"><span class="eyebrow">Próximos passos</span><h2 id="proximos-titulo">O que acontece depois do seu contato</h2></div>
<ol class="steps steps-4"><li><h3>Primeira conversa</h3><p>Entendo a clínica, os procedimentos, a região e o que já foi feito em anúncios.</p></li>
<li><h3>Diagnóstico</h3><p>Se fizer sentido, faço uma <a href="@/auditoria-gratuita-de-anuncios/">auditoria gratuita</a> das suas contas.</p></li>
<li><h3>Proposta</h3><p>Envio uma proposta por escrito, com escopo e valores (veja os <a href="@/precos/">preços</a>).</p></li>
<li><h3>Início</h3><p>Com o contrato assinado, começamos a estruturação das campanhas.</p></li></ol></div></section>

{cta_band("Pronto para conversar?", "Mande uma mensagem agora e receba uma orientação inicial.", c_wa, "cta_final")}
'''})

# ======================================================================= PRIVACIDADE
LEGAL_NOTE = "<!-- MODELO: validar com assessoria jurídica e preencher {{RAZAO_SOCIAL}}, {{CNPJ}}, {{EMAIL}}, {{CIDADE/UF}} antes de publicar. -->"
PAGES.append({
    "path": "politica-de-privacidade/", "title": "Política de Privacidade (LGPD) | Arno Hoberg",
    "desc": "Política de Privacidade conforme a LGPD: quais dados coletamos no site, para que usamos, cookies, compartilhamento e como exercer seus direitos de titular.",
    "crumbs": [("Início", ""), ("Política de Privacidade", "politica-de-privacidade/")], "notes": LEGAL_NOTE, "schema": [],
    "body": hero_simple("Privacidade", "Política de Privacidade", "Como tratamos os dados pessoais coletados neste site, em conformidade com a Lei Geral de Proteção de Dados (Lei nº 13.709/2018).",
                        wa_btn(MSG_GENERIC, "Dúvidas pelo WhatsApp", loc="hero")) + f'''
<section class="section"><div class="container"><div class="prose">
<p class="note">Última atualização: <time datetime="{LASTMOD}">31 de outubro de 2026</time>.</p>
<h2>1. Quem é o controlador dos dados</h2>
<p>O controlador é {{{{RAZAO_SOCIAL}}}}, inscrito no CNPJ {{{{CNPJ}}}}, nome fantasia {BRAND}, com atendimento 100% online. Contato para assuntos de privacidade: {{{{EMAIL}}}}.</p>
<h2>2. Quais dados coletamos</h2>
<ul><li><strong>Formulários:</strong> nome, WhatsApp, nome da clínica, especialidade e, opcionalmente, mensagem e plataforma de anúncios utilizada.</li>
<li><strong>WhatsApp:</strong> dados que você compartilhar na conversa.</li>
<li><strong>Navegação:</strong> com o seu consentimento, dados de uso coletados por cookies de medição (Google Analytics/Tag Manager e Meta Pixel), como páginas visitadas e cliques.</li></ul>
<p>Não solicitamos dados de saúde por este site. Pedimos que você não envie informações clínicas pelos formulários.</p>
<h2>3. Para que usamos os dados e bases legais</h2>
<ul><li>Responder ao seu contato, enviar o material solicitado e apresentar propostas — <em>consentimento</em> e <em>procedimentos preliminares a contrato</em>.</li>
<li>Medir o desempenho do site e dos anúncios — <em>consentimento</em> (cookies de medição).</li>
<li>Cumprir obrigações legais e exercer direitos — <em>obrigação legal</em> e <em>exercício regular de direitos</em>.</li></ul>
<h2>4. Cookies</h2>
<p>Usamos armazenamento local essencial para lembrar a sua escolha de cookies. Cookies de medição e publicidade só são ativados se você clicar em “Aceitar”. Você pode mudar a escolha a qualquer momento em “Preferências de cookies”, no rodapé.</p>
<h2>5. Compartilhamento</h2>
<p>Os dados podem ser tratados por fornecedores que viabilizam o serviço, como a hospedagem do site (GitHub Pages), o serviço de envio de formulários, o WhatsApp/Meta e o Google. Não vendemos dados pessoais.</p>
<h2>6. Transferência internacional</h2>
<p>Alguns fornecedores armazenam dados fora do Brasil. Nesses casos, a transferência ocorre nas hipóteses permitidas pela LGPD.</p>
<h2>7. Por quanto tempo guardamos</h2>
<p>Os dados de contato são mantidos enquanto houver relacionamento ou interesse legítimo e excluídos quando você solicitar, salvo obrigação legal de guarda.</p>
<h2>8. Seus direitos</h2>
<p>Você pode solicitar confirmação de tratamento, acesso, correção, anonimização, portabilidade, eliminação, informação sobre compartilhamento e revogação do consentimento (art. 18 da LGPD), pelo e-mail {{{{EMAIL}}}}. Também pode reclamar à Autoridade Nacional de Proteção de Dados (ANPD).</p>
<h2>9. Segurança</h2>
<p>Adotamos medidas técnicas e administrativas razoáveis para proteger os dados, como conexão segura (HTTPS) e acesso restrito às informações.</p>
<h2>10. Alterações</h2>
<p>Esta política pode ser atualizada. A data da última atualização fica sempre indicada no topo da página.</p>
</div></div></section>'''})

# ======================================================================= TERMOS
PAGES.append({
    "path": "termos/", "title": "Termos de Uso | Arno Hoberg Tráfego Pago para Clínicas",
    "desc": "Termos de Uso do site Arno Hoberg | Tráfego Pago para Clínicas: condições de uso do conteúdo, ausência de garantia de resultados, links externos e contato.",
    "crumbs": [("Início", ""), ("Termos de Uso", "termos/")], "notes": LEGAL_NOTE, "schema": [],
    "body": hero_simple("Termos", "Termos de Uso", "Condições para uso deste site e de seus conteúdos.",
                        wa_btn(MSG_GENERIC, "Dúvidas pelo WhatsApp", loc="hero")) + f'''
<section class="section"><div class="container"><div class="prose">
<p class="note">Última atualização: <time datetime="{LASTMOD}">31 de outubro de 2026</time>.</p>
<h2>1. Aceitação</h2>
<p>Ao usar este site, você concorda com estes Termos de Uso e com a <a href="@/politica-de-privacidade/">Política de Privacidade</a>.</p>
<h2>2. Sobre o conteúdo</h2>
<p>O conteúdo tem caráter informativo e comercial. Os guias, incluindo o de <a href="@/regras-de-publicidade-para-clinicas/">regras de publicidade</a>, não substituem orientação jurídica nem as normas oficiais dos conselhos profissionais e órgãos reguladores.</p>
<h2>3. Sem garantia de resultados</h2>
<p>Os resultados mencionados são típicos e variam conforme clínica, oferta e mercado. Nenhuma informação deste site representa promessa ou garantia de resultados financeiros, de pacientes ou de faturamento.</p>
<h2>4. Contratação de serviços</h2>
<p>Os serviços são contratados mediante proposta e contrato específicos, que prevalecem sobre as informações do site. Os valores divulgados são “a partir de” e podem mudar sem aviso prévio.</p>
<h2>5. Propriedade intelectual</h2>
<p>Textos, imagens, logotipo e layout pertencem a {{{{RAZAO_SOCIAL}}}} ou são usados com autorização. A reprodução sem permissão é proibida.</p>
<h2>6. Links externos</h2>
<p>O site pode conter links para sites de terceiros, como conselhos profissionais e plataformas de anúncios. Não nos responsabilizamos pelo conteúdo desses sites.</p>
<h2>7. Legislação e foro</h2>
<p>Estes termos são regidos pela legislação brasileira. Fica eleito o foro da comarca de {{{{CIDADE/UF}}}}, salvo disposição legal em contrário.</p>
<h2>8. Contato</h2>
<p>Dúvidas: {{{{EMAIL}}}} ou pelo WhatsApp.</p>
</div></div></section>'''})

# ======================================================================= OBRIGADO (noindex)
PAGES.append({
    "path": "obrigado/", "title": "Obrigado! Recebemos seu pedido | Arno Hoberg",
    "desc": "Recebemos seu pedido. Em breve Arno Hoberg entrará em contato pelo WhatsApp. Enquanto isso, conheça os serviços de tráfego pago para clínicas de estética.",
    "robots": "noindex,follow", "schema": [],
    "body": f'''<section class="hero" aria-labelledby="titulo-principal" data-thanks-page><div class="container"><div style="margin-top:20px;max-width:760px">
<p class="eyebrow">Tudo certo</p><h1 id="titulo-principal">Obrigado! Recebemos seu pedido</h1>
<p class="lead">Vou analisar as informações e responder pessoalmente pelo WhatsApp. Se preferir agilizar, mande uma mensagem agora.</p>
<div id="ebook-download" class="callout" hidden><p><strong>Seu e-book está pronto.</strong></p><p><a class="btn btn-primary" href="@/ebook/" download>Baixar e-book</a></p></div>
<div class="hero-actions">{wa_btn(MSG_GENERIC, "Chamar no WhatsApp", loc="obrigado")}<a class="btn btn-secondary" href="@/">Voltar ao início</a></div>
</div></div></section>
<section class="section"><div class="container"><div class="section-head"><h2>Enquanto isso, conheça os serviços</h2></div><div class="grid grid-3">{service_cards()}</div></div></section>'''})
