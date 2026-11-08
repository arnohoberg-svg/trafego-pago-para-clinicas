from lib import *


def steps_html(steps):
    return "".join(f"<li><h3>{h}</h3><p>{t}</p></li>" for h, t in steps)


def service_page(path, crumb, title, desc, h1, eyebrow, lead, summary, problem_h2, problem_html,
                 how_h2, steps, deliv_h2, deliverables, results_html, extra, faq, wa_msg, schema):
    dl = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in summary)
    deliv = "".join(f"<li>{d}</li>" for d in deliverables)
    body = f'''<section class="hero" aria-labelledby="titulo-principal">
<div class="container">[[CRUMBS]]
<div class="hero-grid" style="margin-top:20px">
<div><p class="eyebrow">{eyebrow}</p>
<h1 id="titulo-principal">{h1}</h1>
<p class="lead">{lead}</p>
<div class="hero-actions">{wa_btn(wa_msg, loc="hero")}{audit_btn("Auditoria gratuita", loc="hero_auditoria")}</div></div>
<aside class="hero-card" aria-label="Resumo do serviço"><dl>{dl}</dl><p class="note">Resultados variam conforme clínica, oferta e mercado.</p></aside>
</div></div></section>

<section class="section" aria-labelledby="problema-titulo">
<div class="container split"><div><span class="eyebrow">O problema</span><h2 id="problema-titulo">{problem_h2}</h2></div><div>{problem_html}</div></div></section>

<section class="section section-alt" aria-labelledby="como-titulo">
<div class="container"><div class="section-head"><span class="eyebrow">Como funciona</span><h2 id="como-titulo">{how_h2}</h2></div>
<ol class="steps steps-4">{steps_html(steps)}</ol></div></section>

{extra}

<section class="section section-alt" aria-labelledby="entregaveis-titulo">
<div class="container split"><div><span class="eyebrow">Entregáveis</span><h2 id="entregaveis-titulo">{deliv_h2}</h2>
<p>Tudo documentado e acessível para você. As contas de anúncio e os ativos digitais ficam no nome da clínica.</p></div>
<div><ul class="checklist">{deliv}</ul></div></div></section>

{results_html}

<section class="section" aria-labelledby="relacionados-titulo">
<div class="container"><div class="section-head"><span class="eyebrow">Serviços relacionados</span><h2 id="relacionados-titulo">Combine com outros serviços</h2>
<p>Os melhores resultados aparecem quando anúncio, página e atendimento trabalham juntos. Veja também os <a href="@/precos/">preços de tráfego pago para clínicas</a> e o nosso <a href="@/regras-de-publicidade-para-clinicas/">guia de regras de publicidade</a>.</p></div>
<div class="grid grid-4">{service_cards(exclude=path)}</div>
<div class="mt-3">{author_box()}</div></div></section>

[[FAQ]]

{cta_band("Quer saber se esse serviço faz sentido para sua clínica?", "Me conte sobre seus procedimentos e sua região. Respondo pessoalmente pelo WhatsApp.", wa_msg, "cta_final", ("precos/", "Ver preços"))}
'''
    return {"path": path, "title": title, "desc": desc, "body": body, "faq": faq, "wa_msg": wa_msg,
            "crumbs": [("Início", ""), (crumb, path)], "schema": [schema]}


def results_ads(kind):
    if kind == "google":
        stat = ('<div class="stat"><span class="stat-value">≈ 50%</span><span class="stat-label">menos custo por clique/visita</span>'
                '<p>Redução típica após reorganizar campanhas, palavras-chave, negativas e lances.</p></div>'
                '<div class="stat"><span class="stat-value">+</span><span class="stat-label">mais buscas qualificadas</span>'
                '<p>Com o mesmo orçamento, mais visitas de pessoas procurando o seu procedimento na sua região.</p></div>'
                '<div class="stat"><span class="stat-value">100%</span><span class="stat-label">dos termos revisados</span>'
                '<p>Revisão contínua dos termos de pesquisa para cortar o que não tem intenção de agendar.</p></div>')
        intro = "Em contas de Google Ads que chegam sem estrutura, o ganho mais comum vem de parar de pagar por buscas irrelevantes."
    else:
        stat = ('<div class="stat"><span class="stat-value">≈ 50%</span><span class="stat-label">menos custo por lead (CPL)</span>'
                '<p>Redução típica com objetivos de campanha corretos, públicos e criativos testados.</p></div>'
                '<div class="stat"><span class="stat-value">+</span><span class="stat-label">mais pessoas interessadas</span>'
                '<p>Mais conversas iniciadas no WhatsApp com o mesmo investimento.</p></div>'
                '<div class="stat"><span class="stat-value">18+</span><span class="stat-label">público dentro das regras</span>'
                '<p>Segmentação adequada às políticas da Meta para procedimentos estéticos.</p></div>')
        intro = "Quando a conta deixa de “impulsionar posts” e passa a trabalhar com campanhas de verdade, o custo por contato costuma cair."
    return f'''<section class="section section-dark" aria-labelledby="resultados-titulo">
<div class="container"><div class="section-head"><span class="eyebrow">Resultados típicos</span><h2 id="resultados-titulo">O que costuma mudar nos primeiros meses</h2><p>{intro}</p></div>
<div class="stats">{stat}</div>
<p class="disclaimer">Resultado típico. Resultados variam conforme clínica, oferta e mercado.</p>
<!-- CASE REAL: insira aqui antes/depois de CPC e CPL quando houver dados autorizados (ver modelo na home). -->
</div></section>'''


def results_qual(title, items, intro):
    cards = "".join(f'<div class="stat"><span class="stat-label">{h}</span><p>{t}</p></div>' for h, t in items)
    return f'''<section class="section section-dark" aria-labelledby="resultados-titulo">
<div class="container"><div class="section-head"><span class="eyebrow">Resultados típicos</span><h2 id="resultados-titulo">{title}</h2><p>{intro}</p></div>
<div class="stats">{cards}</div>
<p class="disclaimer">Resultados variam conforme clínica, oferta e mercado. Não prometemos números para este serviço.</p>
</div></section>'''


SUMMARY_ADS = [("Resultado típico", "{r}"), ("Investimento", "Gestão a partir de R$ 1.200/mês + verba a partir de R$ 600/mês"),
               ("Contrato", "Mínimo de 3 meses"), ("Atendimento", "100% online, todo o Brasil")]

# ======================================================================= GOOGLE ADS
g_path = "google-ads-para-clinicas-esteticas/"
g_wa = MSG_GENERIC
g_faq = [
    ("Quanto investir em Google Ads para clínica de estética?",
     "<p>Recomendamos começar com no mínimo <strong>R$ 600 por mês (R$ 20 por dia)</strong> de verba, paga direto ao Google, além da gestão a partir de R$ 1.200/mês. Em cidades grandes ou com muita concorrência, a verba ideal pode ser maior; isso é avaliado no diagnóstico.</p>"),
    ("Posso anunciar “botox” no Google?",
     "<p>Termos ligados a medicamentos de venda sob prescrição, como marcas de toxina botulínica, sofrem restrições tanto nas políticas do Google quanto nas normas da Anvisa. Por isso, trabalhamos com termos do procedimento e da especialidade, sem citar marcas comerciais. Detalhes no <a href=\"@/regras-de-publicidade-para-clinicas/\">guia de regras de publicidade</a>.</p>"),
    ("O Google Ads funciona para clínica pequena?",
     "<p>Sim, desde que a campanha seja enxuta: poucos procedimentos, região bem delimitada e palavras-chave de alta intenção. Clínicas pequenas costumam se beneficiar justamente porque não podem desperdiçar verba com termos genéricos.</p>"),
    ("Quanto tempo leva para ver resultado no Google Ads?",
     "<p>Os anúncios podem gerar cliques no mesmo dia em que são aprovados. A fase de aprendizado e ajuste costuma levar de 4 a 8 semanas; a partir daí, a conta tende a ficar mais estável.</p>"),
    ("A conta do Google Ads fica no nome de quem?",
     "<p>No nome da clínica. Você é dona da conta, do histórico e dos dados, e me concede acesso de gestor. Se um dia encerrarmos o trabalho, tudo continua com você.</p>"),
    ("Como sei se os cliques viraram pacientes?",
     "<p>Configuramos conversões para cliques no WhatsApp, ligações e formulários. Para fechar a conta, orientamos a clínica a registrar quantos contatos viraram avaliação e procedimento.</p>"),
    ("Vocês usam Performance Max?",
     "<p>Só quando faz sentido. Para a maioria das clínicas com verba limitada, campanhas de pesquisa bem controladas trazem contatos mais qualificados. Formatos automáticos podem entrar depois, com acompanhamento de perto.</p>"),
]
g_extra = f'''<section class="section" aria-labelledby="estrutura-titulo">
<div class="container split">
<div><span class="eyebrow">Estrutura</span><h2 id="estrutura-titulo">Campanhas de Google Ads pensadas para clínicas</h2>
<p>Quem digita “dermatologista em Curitiba” ou “clínica de limpeza de pele perto de mim” está muito mais perto de agendar do que quem rola o feed. O trabalho é aparecer nessas buscas pagando o mínimo possível por clique.</p>
<h3>Rede de Pesquisa com intenção alta</h3>
<p>Grupos de anúncios separados por procedimento ou especialidade, com palavras-chave específicas e anúncios que respondem exatamente ao que a pessoa buscou.</p>
<h3>Palavras-chave negativas desde o primeiro dia</h3>
<p>Bloqueamos buscas como “curso”, “vaga”, “gratuito”, “como fazer em casa” e cidades onde você não atende. É aqui que boa parte da verba costuma ser recuperada.</p>
<h3>Recursos do anúncio e localização</h3>
<p>Sitelinks, frases de destaque, ligação e local ajudam o anúncio a ocupar mais espaço e a passar mais confiança, sem custo adicional por exibição.</p></div>
<div><h3>Como reduzir o custo por clique da clínica no Google Ads</h3>
<ol>
<li>Separe campanhas por procedimento e por região.</li>
<li>Use correspondência de frase e exata nas palavras-chave principais.</li>
<li>Revise o relatório de termos de pesquisa toda semana.</li>
<li>Ajuste horários e dias de veiculação ao horário de atendimento.</li>
<li>Melhore a página de destino para aumentar o Índice de Qualidade.</li>
<li>Escreva anúncios relevantes, sem promessas de resultado.</li>
</ol>
<h3>Políticas de saúde do Google</h3>
<p>O Google restringe anúncios de medicamentos de prescrição e limita o remarketing baseado em temas de saúde. Planejamos as campanhas considerando essas regras para evitar reprovações e suspensões de conta.</p></div>
</div></section>'''
g = service_page(
    g_path, "Google Ads para clínicas",
    "Google Ads para Clínica de Estética | Arno Hoberg",
    "Google Ads para clínica de estética e dermatologia com campanhas enxutas e custo por clique menor. Fale no WhatsApp e peça sua auditoria gratuita da conta.",
    "Google Ads para clínica de estética: apareça para quem já está procurando você",
    "Anúncios no Google para clínicas",
    "Campanhas de pesquisa enxutas para dermatologia, estética avançada e procedimentos faciais. Menos cliques desperdiçados, mais pessoas da sua região chamando no WhatsApp.",
    [(k, v.format(r="≈ 50% menos custo por clique")) for k, v in SUMMARY_ADS],
    "Por que o Google Ads da sua clínica gasta muito e traz pouco",
    """<p>O Google Ads é o canal com maior intenção de compra: a pessoa está ativamente procurando o procedimento. Mesmo assim, muitas clínicas desistem dele porque “o clique é caro e não vira paciente”.</p>
<p>Quase sempre, a causa é estrutural: campanhas configuradas pelo assistente automático, palavras-chave amplas demais, nenhuma palavra negativa, anúncios exibidos fora da região de atendimento e conversões que não medem o que importa.</p>
<ul class="xlist"><li>Pagando por buscas de quem quer fazer curso ou procurar emprego</li><li>Anúncios aparecendo em outras cidades e estados</li><li>Uma única campanha para todos os procedimentos</li><li>Nenhuma medição de cliques no WhatsApp</li></ul>""",
    "Como funciona a gestão de Google Ads para clínicas",
    [("Auditoria da conta", "Analisamos campanhas, termos de pesquisa, conversões e histórico para identificar desperdícios."),
     ("Pesquisa de palavras-chave", "Mapeamos como seus pacientes buscam cada procedimento na sua região e o custo estimado."),
     ("Estrutura enxuta", "Criamos campanhas por procedimento, com anúncios específicos e negativas desde o início."),
     ("Otimização semanal", "Revisamos termos, lances, horários e anúncios, e reinvestimos no que gera contatos.")],
    "O que você recebe na gestão de Google Ads",
    ["Auditoria inicial da conta (ou criação de conta nova no nome da clínica)",
     "Pesquisa de palavras-chave por procedimento e região", "Estrutura de campanhas de pesquisa e lista de negativas",
     "Anúncios redigidos dentro das políticas de saúde", "Configuração de conversões: WhatsApp, ligação e formulário",
     "Otimizações semanais e relatório mensal com custo por contato", "Reunião mensal de alinhamento por vídeo"],
    results_ads("google"), g_extra, g_faq, g_wa,
    service_schema("Gestão de Google Ads para clínicas de estética", "Gestão de anúncios no Google Ads",
                   "Criação e gestão de campanhas de Google Ads para clínicas de dermatologia, estética avançada e procedimentos faciais.", g_path))

# ======================================================================= META ADS
m_path = "meta-ads-para-clinicas-esteticas/"
m_wa = MSG_GENERIC
m_faq = [
    ("Impulsionar post é a mesma coisa que fazer Meta Ads?",
     "<p>Não. O botão “impulsionar” oferece poucas opções de objetivo, público e medição. No Gerenciador de Anúncios é possível escolher o objetivo certo (como mensagens no WhatsApp), testar criativos, excluir públicos e medir o custo por contato.</p>"),
    ("Posso usar fotos de antes e depois nos anúncios do Instagram?",
     "<p>As políticas da Meta para saúde e aparência proíbem, em regra, imagens de “antes e depois” em anúncios, além das restrições dos conselhos profissionais. Trabalhamos com conteúdo educativo, bastidores e apresentação da equipe. Veja o <a href=\"@/regras-de-publicidade-para-clinicas/\">guia de regras de publicidade</a>.</p>"),
    ("Quanto investir em anúncios no Instagram para clínica?",
     "<p>O mínimo recomendado é <strong>R$ 600 por mês (R$ 20 por dia)</strong> de verba, paga direto à Meta, mais a gestão a partir de R$ 1.200/mês. Com isso já é possível testar criativos e públicos com consistência.</p>"),
    ("Anúncios para harmonização facial são permitidos?",
     "<p>Em geral é possível anunciar o serviço de forma informativa, com público de 18 anos ou mais e sem prometer resultado, sem “antes e depois” e sem citar marcas de medicamentos. As regras do conselho do profissional responsável também precisam ser respeitadas, então cada peça é validada com a clínica.</p>"),
    ("Quem produz os criativos dos anúncios?",
     "<p>Orientamos a captação de fotos e vídeos simples (bastidores, equipe, explicações) e cuidamos da edição dos formatos de anúncio e dos textos. O foco é exclusivamente a campanha paga.</p>"),
    ("Por que meus anúncios na Meta são reprovados?",
     "<p>Os motivos mais comuns são afirmações sobre atributos pessoais (como “você tem rugas?”), imagens que destacam partes do corpo, promessas de resultado e “antes e depois”. Reescrever o anúncio no tom certo costuma resolver.</p>"),
    ("O que é um bom custo por lead para clínica?",
     "<p>Não existe número universal: varia com a cidade, o procedimento e a oferta. O melhor parâmetro é o histórico da sua própria conta e quanto custa, no fim, cada avaliação marcada.</p>"),
]
m_extra = f'''<section class="section" aria-labelledby="estrategia-titulo">
<div class="container split">
<div><span class="eyebrow">Estratégia</span><h2 id="estrategia-titulo">Anúncios no Instagram para clínica de estética que geram conversas</h2>
<p>No Instagram, a maioria das pessoas ainda não está procurando um procedimento. O anúncio precisa despertar interesse, educar e transmitir confiança, tudo em poucos segundos e dentro das regras.</p>
<h3>Objetivo certo: mensagens no WhatsApp</h3>
<p>Usamos campanhas com objetivo de mensagens ou de leads, otimizadas para quem tende a iniciar conversa, em vez de buscar apenas curtidas e alcance.</p>
<h3>Criativos que educam, não que prometem</h3>
<p>Vídeos curtos explicando o procedimento, mostrando a estrutura e a equipe, respondendo dúvidas comuns. Esse formato costuma performar bem e respeita as políticas de saúde.</p>
<h3>Públicos de acordo com as regras</h3>
<p>Desde 2022 a Meta limitou opções de segmentação ligadas a temas sensíveis como saúde. Trabalhamos com localização, faixa etária adequada (18+ para procedimentos estéticos), públicos semelhantes e remarketing de quem interagiu com o perfil.</p></div>
<div><h3>Como reduzir o custo por lead da clínica estética no Meta Ads</h3>
<ol>
<li>Escolha o objetivo de campanha de mensagens ou leads, não de alcance.</li>
<li>Teste de 3 a 5 criativos por vez e mantenha só os vencedores.</li>
<li>Delimite o raio de atendimento real da clínica.</li>
<li>Use uma mensagem de boas-vindas que inicie a triagem.</li>
<li>Responda os contatos em minutos — tempo de resposta afeta conversão.</li>
<li>Renove os criativos antes que a frequência fique alta.</li>
</ol>
<h3>Anúncios para harmonização facial e dermatologia</h3>
<p>São nichos com alta concorrência e muita fiscalização. A diferença está em comunicar segurança, formação do profissional e processo de avaliação, em vez de resultados. Saiba mais nas <a href="@/regras-de-publicidade-para-clinicas/">regras de publicidade para clínicas</a>.</p></div>
</div></section>'''
m = service_page(
    m_path, "Meta Ads para clínicas",
    "Meta Ads para Clínica de Estética | Instagram e Facebook",
    "Meta Ads para clínica de estética: anúncios no Instagram e Facebook dentro das regras, com custo por lead menor. Fale no WhatsApp e solicite um orçamento.",
    "Meta Ads para clínica de estética: anúncios no Instagram que geram conversas, não só curtidas",
    "Anúncios no Instagram e Facebook",
    "Campanhas no Instagram e no Facebook para clínicas de dermatologia, estética avançada e procedimentos faciais, com criativos educativos, público certo e foco em contatos no WhatsApp.",
    [(k, v.format(r="≈ 50% menos custo por lead")) for k, v in SUMMARY_ADS],
    "Por que impulsionar posts não enche a agenda da clínica",
    """<p>Impulsionar um post bonito pode trazer curtidas e seguidores, mas raramente traz pacientes. O botão de impulsionamento escolhe objetivos genéricos, mostra o anúncio para pessoas pouco propensas a agendar e não mede o custo por contato.</p>
<p>Além disso, anúncios de saúde e estética têm regras específicas na Meta. Quem ignora isso enfrenta reprovações constantes, entrega limitada e, em casos extremos, restrição da conta de anúncios.</p>
<ul class="xlist"><li>Objetivo de alcance ou engajamento em vez de mensagens</li><li>Público de todo o estado, sem relação com a clínica</li><li>Textos que citam “rugas”, “flacidez” ou “gordura” do leitor</li><li>Sem teste de criativos nem acompanhamento de custo por lead</li></ul>""",
    "Como funciona a gestão de Meta Ads para clínicas",
    [("Diagnóstico", "Revisamos a conta, o pixel, o perfil e os anúncios anteriores para entender o ponto de partida."),
     ("Plano de criativos", "Definimos ângulos de comunicação e o roteiro de fotos e vídeos simples que a clínica pode gravar."),
     ("Campanhas de mensagens", "Estruturamos campanhas com objetivo de conversa no WhatsApp ou formulário, com público 18+ e região definida."),
     ("Testes e otimização", "Comparamos criativos e públicos, pausamos o que não funciona e escalamos o que traz contatos.")],
    "O que você recebe na gestão de Meta Ads",
    ["Diagnóstico da conta de anúncios, pixel e Gerenciador de Negócios", "Plano de criativos com roteiros simples de gravação",
     "Edição de formatos de anúncio (feed, stories e reels) e textos", "Configuração de eventos de conversão e da API de Conversões, quando aplicável",
     "Campanhas de mensagens/leads com públicos e exclusões", "Testes A/B de criativos e relatório mensal com custo por lead",
     "Revisão de conformidade com as políticas de saúde da Meta"],
    results_ads("meta"), m_extra, m_faq, m_wa,
    service_schema("Gestão de Meta Ads para clínicas de estética", "Gestão de anúncios no Instagram e Facebook",
                   "Criação e gestão de campanhas de Meta Ads (Instagram e Facebook) para clínicas de dermatologia, estética avançada e procedimentos faciais.", m_path))

# ======================================================================= SITES
s_path = "criacao-de-sites-para-clinicas-esteticas/"
s_wa = MSG_GENERIC
s_faq = [
    ("Quanto custa um site para clínica de estética?",
     "<p>A criação de sites e landing pages é <strong>sob orçamento</strong>, porque depende do número de páginas, dos procedimentos apresentados e das integrações. Peça um orçamento pelo WhatsApp com o que você precisa.</p>"),
    ("Qual a diferença entre site e landing page?",
     "<p>O site institucional apresenta a clínica como um todo, com várias páginas. A landing page é uma página única, focada em um procedimento ou campanha, feita para converter o visitante que veio de um anúncio. Muitas clínicas começam pela landing page.</p>"),
    ("Em quanto tempo o site fica pronto?",
     "<p>Uma landing page costuma ficar pronta em poucas semanas após recebermos textos, fotos e aprovações. Sites com mais páginas levam mais tempo. O prazo exato é definido no orçamento.</p>"),
    ("O site vai aparecer no Google?",
     "<p>Entregamos o site com a base técnica de SEO: velocidade, títulos, estrutura de headings, dados estruturados e sitemap. Para ganhar posições de forma consistente, recomendamos complementar com o serviço de <a href=\"@/seo-para-clinicas-esteticas/\">SEO para clínicas</a>.</p>"),
    ("Posso colocar fotos de antes e depois no site?",
     "<p>Depende das regras do conselho do profissional responsável e do contexto. Para médicos, a Resolução CFM nº 2.336/2023 trouxe condições específicas; outros conselhos têm regras próprias. Avaliamos com a clínica antes de publicar qualquer imagem de paciente, sempre com autorização por escrito.</p>"),
    ("O site fica no meu nome?",
     "<p>Sim. O domínio e a hospedagem ficam registrados no nome da clínica, e você recebe os acessos.</p>"),
]
s_extra = '''<section class="section" aria-labelledby="pagina-titulo">
<div class="container split">
<div><span class="eyebrow">O que não pode faltar</span><h2 id="pagina-titulo">O que uma landing page para clínica estética precisa ter</h2>
<p>Um bom site de clínica não precisa de efeitos chamativos. Ele precisa carregar rápido no celular, responder às dúvidas do paciente e deixar claro como agendar.</p>
<ul class="checklist">
<li>Título que diz exatamente qual procedimento ou especialidade você atende e onde</li>
<li>Botão de WhatsApp visível o tempo todo, com mensagem pré-preenchida</li>
<li>Apresentação do profissional com nome, registro no conselho e especialidade, quando exigido</li>
<li>Explicação do procedimento: indicação, como funciona, cuidados e etapas da avaliação</li>
<li>Fotos reais da estrutura e da equipe, otimizadas para não deixar a página lenta</li>
<li>Perguntas frequentes respondidas com clareza, sem promessas de resultado</li>
<li>Política de privacidade e formulários com consentimento, conforme a LGPD</li>
</ul></div>
<div><h3>Site institucional ou landing page?</h3>
<p><strong>Landing page</strong> é ideal para campanhas de anúncios: uma página por procedimento, com um único objetivo. <strong>Site institucional</strong> é ideal para fortalecer a marca e aparecer no Google para várias buscas. Muitas clínicas combinam os dois: site para a marca e landing pages para as campanhas.</p>
<h3>Velocidade também é conversão</h3>
<p>Páginas que demoram a carregar perdem visitantes antes mesmo de exibir o conteúdo. Construímos com código leve, imagens em formatos modernos (WebP/AVIF) e foco nas métricas de Core Web Vitals do Google.</p>
<h3>Site para dermatologista e clínica de harmonização facial</h3>
<p>Cada especialidade tem dúvidas e restrições próprias. Em dermatologia, por exemplo, a página deve diferenciar consulta, tratamentos clínicos e procedimentos; em harmonização, o foco é segurança, avaliação individual e formação do profissional.</p></div>
</div></section>'''
s = service_page(
    s_path, "Criação de sites para clínicas",
    "Criação de Site para Clínica de Estética e Landing Page",
    "Criação de site para clínica de estética e landing page focada em WhatsApp: rápida, clara e dentro das regras do seu conselho. Peça seu orçamento agora.",
    "Criação de site para clínica de estética e landing pages que transformam visitas em agendamentos",
    "Sites e landing pages para clínicas",
    "Sites rápidos, objetivos e preparados para anúncios e para o Google, com um caminho claro até o WhatsApp da sua clínica e linguagem que respeita as regras de publicidade em saúde.",
    [("Formato", "Landing page por procedimento ou site institucional"), ("Investimento", "Sob orçamento"),
     ("Foco", "Velocidade, clareza e conversão para WhatsApp"), ("Atendimento", "100% online, todo o Brasil")],
    "Por que tantos sites de clínica não geram contatos",
    """<p>Muitos sites de clínica foram feitos para ser bonitos, não para converter. Eles carregam devagar no celular, escondem o botão de contato, falam mais da clínica do que das dúvidas do paciente e não mostram claramente quem é o profissional responsável.</p>
<p>Quando esse site recebe tráfego pago, o problema aumenta: você paga pelo clique e o visitante vai embora sem chamar. Uma página bem construída é o que permite que o investimento em anúncios dê retorno.</p>
<ul class="xlist"><li>Página que demora mais de 3 segundos para abrir no 4G</li><li>Texto genérico, igual ao de qualquer outra clínica</li><li>Nenhum botão de WhatsApp acima da dobra</li><li>Formulários sem política de privacidade nem consentimento</li></ul>""",
    "Como funciona a criação do site ou da landing page",
    [("Briefing", "Entendemos procedimentos, público, diferenciais e regras do conselho aplicáveis à sua clínica."),
     ("Estrutura e textos", "Definimos as seções e escrevemos textos claros, orientados à dúvida do paciente e sem promessas."),
     ("Design e desenvolvimento", "Construímos a página leve, responsiva e acessível, com WhatsApp, formulário e medição."),
     ("Publicação e ajustes", "Publicamos, configuramos Search Console e conversões e ajustamos conforme os primeiros dados.")],
    "O que você recebe na criação do site",
    ["Estrutura de páginas e textos persuasivos e éticos", "Layout responsivo, pensado primeiro para o celular",
     "Botão de WhatsApp com mensagem pré-preenchida e formulário com consentimento LGPD",
     "SEO técnico básico: títulos, headings, dados estruturados e sitemap",
     "Instalação de medição (Google Tag Manager, GA4 e Pixel, com aviso de cookies)",
     "Política de privacidade e termos de uso (modelo para validação jurídica)", "Treinamento rápido para pequenas edições"],
    results_qual("O que costuma melhorar com uma página bem feita",
                 [("Mais contatos por visita", "Com uma página clara e rápida, uma parcela maior dos visitantes chama no WhatsApp."),
                  ("Anúncios mais eficientes", "Páginas relevantes ajudam o Índice de Qualidade do Google e a aprovação de anúncios."),
                  ("Medição confiável", "Com conversões configuradas, fica claro quanto custa cada contato.")],
                 "Uma boa página não cria demanda sozinha, mas faz o tráfego que já existe render mais."),
    s_extra, s_faq, s_wa,
    service_schema("Criação de sites e landing pages para clínicas de estética", "Criação de sites e landing pages",
                   "Desenvolvimento de sites institucionais e landing pages otimizadas para conversão e SEO para clínicas de estética e dermatologia.", s_path))

# ======================================================================= AUTOMAÇÃO
a_path = "automacao-whatsapp-para-clinicas/"
a_wa = MSG_GENERIC
a_faq = [
    ("A automação vai substituir minha recepcionista?",
     "<p>Não. A automação cuida da primeira resposta, da triagem básica e dos lembretes. A conversa sobre avaliação, valores e agenda continua com a sua equipe, que recebe o contato já organizado.</p>"),
    ("Funciona com o WhatsApp Business que eu já uso?",
     "<p>Depende do nível de automação. Recursos simples funcionam no aplicativo WhatsApp Business; fluxos mais completos exigem a plataforma oficial da Meta (API) e uma ferramenta homologada. Avaliamos o que faz sentido para o volume da clínica.</p>"),
    ("Quanto custa a automação de WhatsApp para clínica?",
     "<p>É <strong>sob orçamento</strong>, conforme a complexidade dos fluxos e a ferramenta escolhida. Ferramentas e eventuais custos de mensagens da Meta são pagos à parte, diretamente aos fornecedores.</p>"),
    ("Posso enviar mensagens para quem não respondeu?",
     "<p>Sim, dentro das regras: a pessoa precisa ter iniciado o contato ou autorizado receber mensagens, e mensagens fora da janela de 24 horas usam modelos aprovados pela Meta. Também é preciso respeitar quem pede para não receber mais mensagens.</p>"),
    ("A automação pede dados de saúde do paciente?",
     "<p>Não recomendamos. Dados de saúde são dados sensíveis pela LGPD. A triagem automática se limita ao necessário para o atendimento, como procedimento de interesse e melhor horário; detalhes clínicos ficam para a avaliação com o profissional.</p>"),
    ("Em quanto tempo a automação fica pronta?",
     "<p>Fluxos simples de boas-vindas e follow-up costumam ficar prontos em poucas semanas, incluindo testes. Integrações maiores levam mais tempo e são planejadas no orçamento.</p>"),
]
a_extra = '''<section class="section" aria-labelledby="fluxos-titulo">
<div class="container split">
<div><span class="eyebrow">Fluxos</span><h2 id="fluxos-titulo">Atendimento automático no WhatsApp para clínica de estética</h2>
<p>Cada clínica tem seu jeito de atender. Desenhamos os fluxos junto com a sua equipe para que a automação pareça uma extensão natural da recepção, e não um robô engessado.</p>
<h3>Boas-vindas imediata, inclusive fora do horário</h3>
<p>Quem chama às 22h recebe uma resposta na hora, sabe quando será atendido e já responde as primeiras perguntas.</p>
<h3>Triagem simples</h3>
<p>Procedimento de interesse, região e melhor horário para contato. Sua equipe recebe o contato pronto para conversar.</p>
<h3>Follow-up programado</h3>
<p>Mensagens de acompanhamento para quem parou de responder, em intervalos definidos e com linguagem respeitosa.</p>
<h3>Lembretes de avaliação</h3>
<p>Confirmações e lembretes antes do horário marcado ajudam a reduzir faltas.</p></div>
<div><h3>Por que o tempo de resposta importa tanto</h3>
<p>Quem clica em um anúncio de clínica normalmente pesquisa mais de uma opção ao mesmo tempo. A primeira clínica que responde com clareza tem mais chance de marcar a avaliação. Quando a resposta leva horas, o contato esfria e o dinheiro investido no anúncio se perde.</p>
<h3>Follow-up de leads: onde está o dinheiro esquecido</h3>
<p>Uma parte relevante dos contatos não agenda na primeira conversa. Sem um processo de acompanhamento, essas pessoas simplesmente somem. Um follow-up organizado recupera conversas que, de outra forma, seriam perdidas.</p>
<h3>Automação com responsabilidade</h3>
<p>Seguimos as políticas do WhatsApp Business, coletamos apenas os dados necessários e sempre oferecemos a opção de falar com uma pessoa ou de parar de receber mensagens. Entenda mais sobre LGPD no <a href="@/regras-de-publicidade-para-clinicas/">guia de regras de publicidade para clínicas</a>.</p></div>
</div></section>'''
a = service_page(
    a_path, "Automação de WhatsApp",
    "Automação de WhatsApp para Clínica | Atendimento e Follow-up",
    "Automação de WhatsApp para clínica: resposta imediata, triagem e follow-up de leads para não perder pacientes. Fale no WhatsApp e solicite seu orçamento.",
    "Automação de WhatsApp para clínica: responda em segundos e não perca nenhum interessado",
    "Atendimento e follow-up automatizados",
    "Primeira resposta imediata, triagem dos contatos e follow-up organizado, para que cada pessoa que chega pelos anúncios seja atendida rápido e acompanhada até a avaliação.",
    [("Para quem", "Clínicas que recebem contatos e não conseguem responder rápido"), ("Investimento", "Sob orçamento"),
     ("Ferramentas", "WhatsApp Business ou plataforma oficial (API)"), ("Atendimento", "100% online, todo o Brasil")],
    "Quanto custa um contato que ninguém respondeu?",
    """<p>Você investe em anúncios, o interessado chama no WhatsApp... e espera. A recepção está atendendo quem está na clínica, o contato chegou fora do horário ou simplesmente se perdeu no meio de dezenas de conversas.</p>
<p>Cada contato sem resposta é verba de anúncio desperdiçada. E cada pessoa que não agendou na primeira conversa e nunca recebeu um retorno é uma oportunidade que foi parar na concorrência.</p>
<ul class="xlist"><li>Contatos respondidos horas ou dias depois</li><li>Nenhum retorno para quem pediu valores e sumiu</li><li>Faltas em avaliações por falta de lembrete</li><li>Equipe sobrecarregada com as mesmas perguntas</li></ul>""",
    "Como funciona a automação de WhatsApp para clínicas",
    [("Mapeamento do atendimento", "Entendemos como a sua equipe atende hoje, as dúvidas mais comuns e onde os contatos se perdem."),
     ("Desenho dos fluxos", "Criamos boas-vindas, triagem, follow-up e lembretes com a linguagem da clínica."),
     ("Implementação e testes", "Configuramos a ferramenta adequada e testamos cada caminho antes de ativar."),
     ("Acompanhamento", "Ajustamos mensagens e intervalos conforme as respostas reais dos pacientes.")],
    "O que você recebe na automação de WhatsApp",
    ["Mapeamento do processo de atendimento atual", "Fluxo de boas-vindas e triagem com encaminhamento para humano",
     "Sequência de follow-up para contatos que não responderam", "Mensagens de confirmação e lembrete de avaliação",
     "Etiquetas para organizar contatos por procedimento e etapa", "Orientação de privacidade e opção de descadastro (LGPD)",
     "Treinamento da equipe para usar o fluxo no dia a dia"],
    results_qual("O que costuma melhorar com a automação",
                 [("Tempo de primeira resposta", "Todo contato recebe retorno imediato, inclusive à noite e nos fins de semana."),
                  ("Contatos recuperados", "O follow-up traz de volta conversas que seriam esquecidas."),
                  ("Equipe mais produtiva", "Menos tempo respondendo perguntas repetidas, mais tempo agendando.")],
                 "A automação potencializa o tráfego pago: o mesmo investimento em anúncios passa a gerar mais avaliações."),
    a_extra, a_faq, a_wa,
    service_schema("Automação de WhatsApp para clínicas", "Automação de atendimento e follow-up via WhatsApp",
                   "Implementação de fluxos automáticos de atendimento, triagem, follow-up e lembretes no WhatsApp para clínicas de estética e dermatologia.", a_path))

# ======================================================================= SEO
o_path = "seo-para-clinicas-esteticas/"
o_wa = MSG_GENERIC
o_faq = [
    ("Quanto tempo o SEO leva para dar resultado?",
     "<p>SEO é um trabalho de médio prazo. Os primeiros sinais costumam aparecer em alguns meses, dependendo da concorrência na sua cidade, da situação atual do site e da frequência de publicação. Por isso ele complementa, e não substitui, o tráfego pago no início.</p>"),
    ("Qual a diferença entre SEO e Google Ads?",
     "<p>No <a href=\"@/google-ads-para-clinicas-esteticas/\">Google Ads</a> você paga por clique e aparece rapidamente. No SEO você não paga por clique, mas leva mais tempo para conquistar posições. A combinação dos dois costuma ser a mais eficiente.</p>"),
    ("O Perfil da Empresa no Google (Google Meu Negócio) faz parte do SEO?",
     "<p>Sim. Para uma clínica com endereço físico, o Perfil da Empresa no Google é essencial para aparecer no mapa e em buscas como “dermatologista perto de mim”. Otimizamos categorias, serviços, fotos e informações.</p>"),
    ("Posso pedir avaliações para meus pacientes no Google?",
     "<p>Pedir avaliações de forma espontânea e sem incentivo é permitido pelas políticas do Google, desde que você não ofereça brindes ou descontos em troca e não filtre quem pode avaliar. Também é importante respeitar o sigilo profissional nas respostas.</p>"),
    ("Quanto custa SEO para clínica de estética?",
     "<p>O SEO é cotado sob orçamento, conforme o tamanho do site e o número de páginas e procedimentos a trabalhar. Fale no WhatsApp para receber uma proposta.</p>"),
    ("Preciso ter um blog para fazer SEO?",
     "<p>Não necessariamente. Para muitas clínicas, páginas bem feitas para cada procedimento e um Perfil da Empresa otimizado já trazem bons resultados. O blog passa a fazer sentido quando há capacidade de produzir conteúdo útil com regularidade.</p>"),
]
o_extra = '''<section class="section" aria-labelledby="pilares-titulo">
<div class="container split">
<div><span class="eyebrow">Pilares</span><h2 id="pilares-titulo">Os 4 pilares do SEO para clínicas de estética</h2>
<h3>1. SEO técnico</h3>
<p>Site rápido, seguro, responsivo e fácil de rastrear: títulos únicos, estrutura de headings, sitemap, dados estruturados e correção de erros no Search Console.</p>
<h3>2. Páginas de procedimento</h3>
<p>Uma página para cada procedimento ou especialidade importante, respondendo as dúvidas reais do paciente com informação correta e linguagem ética.</p>
<h3>3. SEO local</h3>
<p>Perfil da Empresa no Google otimizado, informações consistentes (nome, endereço e telefone) em diretórios e páginas que mencionam a sua região de atendimento.</p>
<h3>4. Autoridade</h3>
<p>Menções e links de sites relevantes: associações, parceiros, imprensa local e diretórios de saúde confiáveis.</p></div>
<div><h3>Como fazer a clínica aparecer no Google sem pagar por clique</h3>
<ol>
<li>Cadastre e otimize o Perfil da Empresa no Google com categoria e serviços corretos.</li>
<li>Crie uma página no site para cada procedimento prioritário.</li>
<li>Use títulos e descrições que digam o procedimento e a cidade.</li>
<li>Garanta que o site carregue rápido no celular.</li>
<li>Peça avaliações de forma ética e responda todas com cuidado.</li>
<li>Acompanhe buscas e cliques no Google Search Console.</li>
</ol>
<h3>SEO e tráfego pago juntos</h3>
<p>Os dados das campanhas de Google Ads mostram quais buscas mais trazem contatos. Usamos essas informações para priorizar as páginas de SEO, e o SEO, com o tempo, reduz a dependência de anúncios.</p></div>
</div></section>'''
o = service_page(
    o_path, "SEO para clínicas",
    "SEO para Clínica de Estética | Apareça no Google",
    "SEO para clínica de estética e dermatologia: site técnico, páginas de procedimento e SEO local para aparecer no Google sem pagar por clique. Fale conosco.",
    "SEO para clínica de estética: seja encontrada no Google sem depender só de anúncios",
    "Otimização para buscadores",
    "SEO técnico, páginas de procedimento bem estruturadas e otimização local para que a sua clínica apareça nas buscas da sua região, somando ao tráfego pago no médio prazo.",
    [("Prazo", "Médio prazo, com evolução mês a mês"), ("Investimento", "Sob orçamento"),
     ("Foco", "SEO técnico, páginas de procedimento e SEO local"), ("Atendimento", "100% online, todo o Brasil")],
    "Por que a sua clínica não aparece no Google",
    """<p>Muitas clínicas têm um site, mas ele não aparece quando alguém procura “clínica de estética em [sua cidade]”. Os motivos são quase sempre os mesmos: site lento, páginas sem foco em procedimentos, títulos genéricos, Perfil da Empresa incompleto e nenhuma estratégia de conteúdo.</p>
<p>Enquanto isso, concorrentes com sites mais organizados ocupam as primeiras posições e recebem os pacientes que buscam ativamente pelo serviço — sem pagar por cada clique.</p>
<ul class="xlist"><li>Um único texto genérico para todos os procedimentos</li><li>Site sem Search Console configurado</li><li>Perfil da Empresa no Google desatualizado</li><li>Nenhuma página respondendo dúvidas reais dos pacientes</li></ul>""",
    "Como funciona o SEO para clínicas",
    [("Diagnóstico", "Auditoria técnica do site, análise do Search Console e das buscas da sua região."),
     ("Plano de palavras-chave", "Definimos os procedimentos e termos prioritários, sem canibalizar páginas."),
     ("Otimização", "Ajustes técnicos, novas páginas de procedimento e otimização do Perfil da Empresa."),
     ("Acompanhamento", "Relatório mensal de posições, cliques e contatos vindos do Google.")],
    "O que você recebe no serviço de SEO",
    ["Auditoria técnica de SEO e plano de correções", "Pesquisa de palavras-chave por procedimento e região",
     "Otimização de títulos, descrições, headings e dados estruturados", "Estrutura e textos de páginas de procedimento",
     "Otimização do Perfil da Empresa no Google", "Configuração e monitoramento do Google Search Console",
     "Relatório mensal de evolução"],
    results_qual("O que costuma melhorar com SEO",
                 [("Mais visibilidade local", "A clínica passa a aparecer em mais buscas da região, no mapa e nos resultados orgânicos."),
                  ("Menos dependência de anúncios", "Uma parte dos contatos passa a chegar sem custo por clique."),
                  ("Mais confiança", "Quem encontra a clínica bem posicionada e com informação útil tende a confiar mais.")],
                 "O SEO é cumulativo: o trabalho de cada mês continua rendendo nos meses seguintes."),
    o_extra, o_faq, o_wa,
    service_schema("SEO para clínicas de estética", "Otimização para mecanismos de busca (SEO)",
                   "SEO técnico, páginas de procedimento e SEO local para clínicas de estética e dermatologia.", o_path))

PAGES = [g, m, s, a, o]
