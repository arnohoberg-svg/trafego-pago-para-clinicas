# Site Arno Hoberg | Tráfego Pago para Clínicas — Entregáveis

Gerado em 31/10/2026. Pasta: `D:\SITE TRAFEGO PAGO ESTÉTICA`. A pasta `_projeto/` **não** é publicada (está no `.gitignore`).

---

## 1. Antes de publicar — substituições globais (buscar e substituir em todos os arquivos)

| Placeholder | Onde aparece | Trocar por |
|---|---|---|
| `{{URL_BASE}}` | canonical, OG, Twitter, JSON-LD, sitemap.xml, robots.txt, 404.html | URL sem barra final. Ex.: `https://usuario.github.io/repositorio` ou `https://www.seudominio.com.br` |
| ~~`{{WHATSAPP}}`~~ ✅ | já configurado: `5548988387867` ((48) 98838-7867) | Mensagens: botões de "auditoria gratuita" → *"Olá! Estava no site e gostaria de uma auditoria gratuita."*; questionário de orçamento → mensagem montada com tudo o que foi selecionado; demais contatos → *"Olá! Vim pelo site, gostaria de entender mais sobre o seu processo."* Para mudar: `MSG_GENERIC`/`MSG_AUDIT` em `_projeto/ferramentas/lib.py` (e rodar o build) |
| `{{FORM_ENDPOINT}}` | `assets/js/main.js` | Endpoint POST JSON (Formspree, Getform, Make, etc.). Sem endpoint, os formulários seguem pelo WhatsApp com os dados preenchidos |
| `{{EBOOK_PDF_URL}}` | `assets/js/main.js` | Link do PDF do e-book |
| `{{CODIGO_SEARCH_CONSOLE}}` | `<head>` de cada página (comentado) | Código de verificação (ou use verificação por DNS, recomendado com domínio próprio) |
| `{{RAZAO_SOCIAL}}`, `{{CNPJ}}`, `{{EMAIL}}`, `{{CIDADE/UF}}` | política de privacidade, termos, rodapé (comentado), contato (comentado) | Dados reais |
| `gtmId` / `ga4Id` / `metaPixelId` | `assets/js/main.js` (bloco CONFIG) | IDs reais. Recomendado: só GTM e configurar GA4 + Pixel dentro dele |

Comentários `<!-- CONFIRMAR -->`, `<!-- DEFINIR TEMA DO E-BOOK -->`, `<!-- VALIDAÇÃO JURÍDICA OBRIGATÓRIA -->`, `<!-- MODELO -->`, `<!-- CASES REAIS -->` e `<!-- DEPOIMENTOS REAIS -->` marcam os pontos que dependem de você.

**Editar o site depois:** dá para editar os HTML direto. Se preferir regenerar tudo, edite os arquivos em `_projeto/ferramentas/` e rode `python _projeto/ferramentas/build.py` (requer Python + Pillow). Atenção: o build sobrescreve os HTML, `style.min.css` e `main.js`. Edite o `main.js` de `_projeto/ferramentas/` ou refaça as edições depois do build.

---

## 2. Estrutura de arquivos

```
D:\SITE TRAFEGO PAGO ESTÉTICA\
├── index.html                                   Home
├── google-ads-para-clinicas-esteticas\index.html
├── meta-ads-para-clinicas-esteticas\index.html
├── criacao-de-sites-para-clinicas-esteticas\index.html
├── automacao-whatsapp-para-clinicas\index.html
├── seo-para-clinicas-esteticas\index.html
├── auditoria-gratuita-de-anuncios\index.html    captura
├── ebook\index.html                             captura (tema a definir)
├── sobre\index.html
├── precos\index.html
├── regras-de-publicidade-para-clinicas\index.html
├── contato\index.html
├── politica-de-privacidade\index.html
├── termos\index.html
├── obrigado\index.html                          noindex (fora do sitemap)
├── 404.html                                     noindex, autocontida (CSS inline, links absolutos)
├── robots.txt · sitemap.xml · site.webmanifest · .nojekyll · .gitignore
├── favicon.ico (16/32/48) · favicon.svg · favicon-16x16/32x32/48x48/96x96.png
├── apple-touch-icon.png (180) · icon-192.png · icon-512.png · icon-maskable-512.png
├── assets\css\style.min.css                     CSS não crítico (o crítico vai inline em cada página)
├── assets\js\main.js                            menu, cookies/LGPD, eventos, questionário, formulários
├── assets\img\                                  fotos WebP+AVIF responsivas, logo, OG
│   └── originais\                               cópias intactas (não publicar)
├── [originais na raiz: logo.png e FOTO *.jpg — intocados, não publicar]
└── _projeto\                                    documentação + gerador (não publicar)
```

**Caminhos relativos:** todas as páginas usam caminhos relativos (`./` na home, `../` nas internas). O site funciona igual em `usuario.github.io/repositorio/` e num domínio próprio, sem trocar caminhos. A exceção é a `404.html`: o GitHub Pages a serve em qualquer profundidade de URL, por isso ela usa `{{URL_BASE}}` absoluto. Por esse motivo os favicons não usam `/favicon.ico` absoluto como no modelo do briefing: em subpasta de projeto, `/` apontaria para `usuario.github.io/`.

---

## 3. Keywords por página

| Página | Keyword principal | Secundárias | Intenção |
|---|---|---|---|
| `/` | tráfego pago para clínicas de estética | marketing digital para clínicas estéticas; agência de tráfego pago para clínicas; como captar pacientes para clínica de estética; tráfego pago para dermatologistas; gestor de tráfego para clínicas | Comercial / navegacional |
| `/google-ads-para-clinicas-esteticas/` | Google Ads para clínica de estética | anúncios no Google para clínica; reduzir custo por clique clínica; gestor de Google Ads para clínicas; campanha de pesquisa para dermatologia; anunciar botox no Google | Comercial |
| `/meta-ads-para-clinicas-esteticas/` | Meta Ads para clínica de estética | anúncios no Instagram para clínica de estética; anúncios para harmonização facial; reduzir custo por lead clínica estética; Facebook Ads para clínicas; antes e depois Instagram anúncio | Comercial |
| `/criacao-de-sites-para-clinicas-esteticas/` | criação de site para clínica de estética | landing page para clínica estética; site para dermatologista; site para clínica de harmonização facial; quanto custa site para clínica | Comercial / transacional |
| `/automacao-whatsapp-para-clinicas/` | automação de WhatsApp para clínica | atendimento automático WhatsApp clínica de estética; follow-up de leads clínica; chatbot para clínica de estética; tempo de resposta leads | Comercial |
| `/seo-para-clinicas-esteticas/` | SEO para clínica de estética | aparecer no Google clínica de estética; SEO local para clínicas; Google Meu Negócio para clínica; SEO para dermatologista | Comercial / informacional |
| `/precos/` | quanto custa tráfego pago para clínica | quanto investir em tráfego pago para clínica; preço gestor de tráfego clínica; verba mínima Google Ads; valor gestão de anúncios | Comercial (pesquisa de preço) |
| `/auditoria-gratuita-de-anuncios/` | auditoria gratuita de anúncios | análise de conta Google Ads; diagnóstico de tráfego pago para clínica; por que meus anúncios não trazem pacientes | Transacional (lead) |
| `/ebook/` | e-book tráfego pago para clínicas de estética (provisório) | material gratuito marketing para clínicas; guia de anúncios para clínicas | Transacional (lead) |
| `/sobre/` | gestor de tráfego pago para clínicas (Arno Hoberg) | especialista em tráfego para clínicas estéticas; consultor de marketing digital para clínicas | Navegacional / confiança |
| `/regras-de-publicidade-para-clinicas/` | regras de publicidade para clínicas de estética | publicidade médica CFM 2.336/2023; pode postar antes e depois clínica; anúncio de botox é permitido; políticas Google Ads saúde; Meta Ads antes e depois | Informacional (topo de funil + autoridade) |
| `/contato/` | contato gestor de tráfego para clínicas | falar com gestor de tráfego; WhatsApp tráfego pago clínica | Navegacional |

Para evitar canibalização: a home concentra o termo genérico ("tráfego pago para clínicas") e cada serviço tem o seu termo de plataforma. A intenção "quanto investir" aparece resumida na home e completa em `/precos/` (a home linka para lá).

---

## 4. Árvore de headings
Validada automaticamente: **cada página tem exatamente 1 H1 e nenhum salto de nível** (H1→H2→H3). Logo, menu e rodapé não usam headings. A árvore completa de cada página está no fim deste arquivo (seção 10).

Métricas por página: todos os títulos com ≤ 60 caracteres; descriptions entre 150 e 156 caracteres; páginas de serviço com 1.087 a 1.248 palavras; home com 1.911; guia de regras com 1.714.

---

## 5. Checklist de publicação

### GitHub Pages
1. [ ] Fazer as substituições da seção 1 (no mínimo `{{URL_BASE}}` e `{{WHATSAPP}}`).
2. [ ] Criar um repositório no GitHub (público, ou privado num plano que permita Pages).
3. [ ] Enviar o conteúdo da pasta com `.gitignore` (assim `_projeto/`, os originais e `assets/img/originais/` não sobem). Pelo site do GitHub: "Add file → Upload files", sem arrastar esses itens.
4. [ ] Settings → Pages → Source: *Deploy from a branch* → `main` / `/ (root)` → Save.
5. [ ] Abrir `https://usuario.github.io/repositorio/` e testar: menu mobile, botões de WhatsApp, formulários, banner de cookies e uma URL inexistente (deve abrir a 404).
6. [ ] Rodar o Lighthouse (Chrome DevTools, modo mobile) na home e numa página de serviço.

### Domínio próprio (recomendado)
1. [ ] Registrar o domínio (ex.: Registro.br).
2. [ ] Settings → Pages → Custom domain → informar `www.seudominio.com.br` (o GitHub cria o arquivo `CNAME`).
3. [ ] No DNS: CNAME de `www` → `usuario.github.io`; registros A do domínio raiz → 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153.
4. [ ] Marcar **Enforce HTTPS**.
5. [ ] **Trocar `{{URL_BASE}}` (ou a URL antiga do github.io) pela URL nova em:** canonical, `og:url`, `og:image`, `twitter:image`, JSON-LD (todos os `@id`, `url`, `logo` e `image`), `sitemap.xml`, `robots.txt` e `404.html`. Basta buscar e substituir a URL antiga por `https://www.seudominio.com.br`.
6. [ ] Com domínio próprio, o `/favicon.ico` passa a ficar na raiz do domínio, como o Google espera.

### Google Search Console
1. [ ] Adicionar propriedade: *Domínio* (verificação por DNS TXT, recomendado) ou *Prefixo de URL* (meta tag: descomentar `google-site-verification` no `<head>` de `index.html`).
2. [ ] Sitemaps → enviar `sitemap.xml`.
3. [ ] Inspeção de URL → "Solicitar indexação" nesta ordem: home, `/precos/`, as 5 páginas de serviço, `/auditoria-gratuita-de-anuncios/`, `/regras-de-publicidade-para-clinicas/`, `/sobre/`.
4. [ ] Conferir em "Melhorias" se aparecem Breadcrumbs e FAQ sem erros. Testar também em https://validator.schema.org e https://search.google.com/test/rich-results.
5. [ ] Depois de 2 a 4 semanas: relatório "Páginas" (indexação) e "Desempenho" (consultas).

### Medição
1. [ ] Criar o contêiner do GTM, colocar o `gtmId` em `main.js` e, dentro do GTM, configurar GA4 + Meta Pixel.
2. [ ] Eventos enviados ao `dataLayer` (crie acionadores de *Evento personalizado* no GTM):
   - `whatsapp_click` (parâmetro `link_location`: hero, rodape, botao_flutuante, cta_final, questionario_orcamento…)
   - `generate_lead` (parâmetro `form_name`: auditoria, ebook, contato)
   - `ebook_download`
3. [ ] Marcar `generate_lead` e `whatsapp_click` como conversões no GA4 e importar para o Google Ads.
4. [ ] O Consent Mode v2 começa como "negado". Os scripts só carregam depois de o visitante clicar em "Aceitar".

---

## 6. Pendências que dependem de você

| # | Item | Situação |
|---|---|---|
| 1 | Número do WhatsApp | ✅ Configurado: (48) 98838-7867 |
| 2 | Domínio / URL final | `{{URL_BASE}}` |
| 3 | **Dado "60 clientes"** | Em comentário `<!-- CONFIRMAR -->` na home e em /sobre. É média no 1º mês ou total atendido? **Não publicado** |
| 4 | Nome definitivo da marca | Usando o provisório "Arno Hoberg \| Tráfego Pago para Clínicas" |
| 5 | Tema e título do e-book + PDF | Página /ebook/ com título e tópicos provisórios; `{{EBOOK_PDF_URL}}` |
| 6 | Cases reais (CPC/CPL antes e depois, com autorização) | Modelo comentado na seção de resultados da home |
| 7 | Depoimentos reais (nome, clínica, foto, autorização) | Seção pronta e comentada na home |
| 8 | Endpoint de formulário | `{{FORM_ENDPOINT}}` (até lá, os formulários seguem pelo WhatsApp) |
| 9 | Razão social, CNPJ, e-mail, foro | Páginas de privacidade e termos |
| 10 | **Validação jurídica** do guia de regras, da política e dos termos | Obrigatória antes de publicar |
| 11 | IDs de GTM / GA4 / Pixel e código do Search Console | `main.js` e `<head>` |
| 12 | Preço do SEO | Coloquei "sob orçamento" (o briefing não definia). Confirme |
| 13 | Horário de suporte | /precos cita "suporte pelo WhatsApp em horário comercial". Confirme |
| 14 | Logo vetorial original | Vetorizei a partir do PNG (99,87% de fidelidade). Se existir o arquivo .svg/.ai original, envie |
| 15 | Instagram/LinkedIn | Para incluir `sameAs` no schema e links no rodapé |

---

## 7. Plano de 90 dias de SEO (sem blog)

**Dias 1–15 — Base técnica e indexação**
- Publicar com domínio próprio e HTTPS, configurar o Search Console e o GA4 e enviar o sitemap.
- Solicitar a indexação das páginas principais e validar os dados estruturados.
- Criar perfis consistentes (mesmo nome, foto, descrição e link): LinkedIn pessoal e de empresa, Instagram profissional e YouTube (opcional).

**Dias 16–45 — Páginas de apoio (cauda longa, alta intenção)**
- Criar 4 a 6 páginas de apoio, cada uma com 1 keyword e links para o serviço correspondente:
  - `/trafego-pago-para-dermatologistas/`
  - `/anuncios-para-harmonizacao-facial/`
  - `/quanto-investir-em-trafego-pago-para-clinica/` (só se o Search Console mostrar demanda separada de /precos/; senão, reforce /precos/)
  - `/landing-page-para-clinica-estetica/` (se "landing page" ganhar impressões próprias)
  - `/google-ads-ou-instagram-para-clinica/` (comparativo)
- Criar um glossário curto (CPL, CPC, CTR, Índice de Qualidade) dentro de /precos/ ou como página própria.

**Dias 46–75 — Autoridade e backlinks**
- Participar como convidado de podcasts/lives de gestão de clínicas e associações de estética, com link para o site.
- Escrever artigos convidados em portais de gestão de clínicas e de marketing médico, apontando para o guia de regras (a página mais "linkável").
- Pedir aos clientes satisfeitos um link "site desenvolvido/gerido por" no rodapé do site da clínica, com autorização.
- Cadastrar o site em diretórios de profissionais de marketing (perfis de parceiro do Google Ads/Meta, se elegível).
- **Google Business Profile:** como a consultoria é 100% online e sem atendimento presencial, o perfil só é permitido como *empresa de área de cobertura* que atende o cliente no local dele. Para serviço puramente remoto, as diretrizes do Google em geral **não** permitem o perfil. Não crie um endereço fictício. Para as clínicas clientes, que têm endereço, o perfil é essencial (isso faz parte do serviço de SEO).

**Dias 76–90 — Otimização com dados**
- No Search Console: páginas com muitas impressões e CTR baixo → reescrever title e description.
- Consultas na posição 8–20 → reforçar a página com uma seção ou pergunta de FAQ sobre aquela consulta.
- Atualizar a data de revisão do guia de regras e conferir se as normas mudaram.
- Publicar os primeiros cases e depoimentos autorizados (sinal forte de E-E-A-T).

**Quando incluir um blog:** quando você conseguir publicar **pelo menos 2 conteúdos úteis por mês, com consistência**, e quando o Search Console mostrar muitas consultas informacionais ("como…", "pode…", "quanto…") que não cabem nas páginas atuais. Antes disso, páginas de apoio bem feitas rendem mais que um blog parado.

---

## 8. Relatório de assets

### Encontrados na pasta
| Arquivo original | Dimensões | Observação |
|---|---|---|
| `logo.png` | 800×800, RGBA, fundo transparente, preto | Monograma "AH" no triângulo. Boa resolução, mas não é vetor |
| `FOTO SITE.jpg` | 1080×1080 | Estúdio, fundo branco, terno azul, sorrindo |
| `FOTO PERFIL 01.jpg` | 1500×1500 (1 MB) | Retrato colorido, fundo escuro |
| `FOTO HOTMART.jpg` | 1080×1920 | Vertical, blazer preto, fundo escuro |
| `FOTO CORRETOR.jpg` | 1080×1080 | Retrato P&B |

Os originais não foram alterados. As cópias intactas estão em `assets/img/originais/`.

### Gerados / otimizados
| Arquivo gerado (WebP + AVIF) | Origem | Usado em |
|---|---|---|
| `arno-hoberg-gestor-trafego-pago-400/776` | FOTO SITE (recorte 4:5) | **Home** (hero, com preload e `fetchpriority=high`) |
| `arno-hoberg-especialista-marketing-clinicas-480/864` | FOTO HOTMART (recorte 4:5) | **Home** (seção "Prazer, Arno Hoberg") |
| `arno-hoberg-consultor-trafego-pago-clinicas-480/960` | FOTO PERFIL 01 | **/sobre/** (hero) e schema Person |
| `arno-hoberg-retrato-400/800` | FOTO CORRETOR | **/auditoria-gratuita-de-anuncios/** e **/ebook/** |
| `arno-hoberg-avatar-96/192` | FOTO PERFIL 01 (recorte do rosto) | Caixa "Quem cuida da sua conta" nas **5 páginas de serviço** |
| `og-image.jpg` 1200×630 | Logo laranja + texto + FOTO HOTMART | OG/Twitter de todas as páginas |
| `logo-arno-hoberg.svg` | Vetorizado do logo.png | Referência (o header e o rodapé usam o SVG inline) |
| `logo-arno-hoberg-512.png` | Vetor | Logo do schema Organization |
| favicons (`.ico` 16/32/48, `.svg`, PNG 16/32/48/96, apple 180, 192, 512, maskable) | Vetor, símbolo branco sobre laranja #C2410C | `<head>` de todas as páginas e manifest |

Exemplo de economia: FOTO PERFIL 01 tinha 1.052 KB; a versão AVIF de 960 px tem 23 KB.

### Observações sobre o logo
- A resolução e a transparência estão boas. Por ser preto, ele não aparece em fundo escuro. Por isso o rodapé usa a versão branca e o favicon usa o símbolo branco sobre laranja, que fica legível em 16 px, em abas claras e escuras.
- O logo é só o símbolo, sem nome. No header ele aparece ao lado do texto "Arno Hoberg / Tráfego Pago para Clínicas".
- Sugestão: guardar o vetor oficial (SVG/AI) e definir uma versão horizontal (símbolo + nome) para materiais futuros.

### O que está faltando
- Fotos da rotina de trabalho (computador, reunião por vídeo) para variar as páginas de serviço. Fotos de clínicas clientes só com autorização.
- Fotos e logos de clínicas para os depoimentos (com autorização).
- Prints de resultados reais para os cases (anonimizados ou autorizados).

---

## 9. Confirmação
Todos os arquivos do site foram salvos em `D:\SITE TRAFEGO PAGO ESTÉTICA` (árvore na seção 2). Validação automática: 15 páginas + 404, 0 links internos quebrados, 0 assets ausentes, 0 imagens sem `alt`/`width`/`height`, 0 IDs duplicados, 1 H1 por página, sem saltos de heading. Teste de largura em 360 e 390 px: nenhuma rolagem horizontal.

---

## 10. Árvore de headings completa (gerada pelo validador)

```text
## /  | title 52 | desc 150 | palavras no <main> 1911
H1 Tráfego pago para clínicas de estética: mais pacientes interessados, menos verba desperdiçada
  H2 Por que tantas clínicas investem em anúncios e não veem a agenda encher?
  H2 Marketing digital para clínicas estéticas, do anúncio ao WhatsApp
    H3 Google Ads para clínicas
    H3 Meta Ads (Instagram e Facebook)
    H3 Sites e landing pages
    H3 Automação de WhatsApp
    H3 SEO para clínicas
    H3 TikTok Ads
  H2 Como funciona: o método em 4 etapas
    H3 Diagnóstico e auditoria
    H3 Campanhas enxutas
    H3 Otimização semanal
    H3 Escala com controle
  H2 Resultado típico nas contas que assumimos
  H2 Por que escolher uma agência de tráfego pago só para clínicas
    H3 Método próprio
    H3 Orçamento baixo, bem usado
    H3 Especialista no nicho
    H3 Sites feitos para vender
  H2 Como captar pacientes para clínica de estética com tráfego pago
    H3 Tráfego pago para dermatologistas e clínicas de harmonização
  H2 Quanto investir em tráfego pago para clínica?
    H3 Monte seu orçamento em 30 segundos
  H2 Prazer, Arno Hoberg
  H2 Anúncios dentro das regras do CFM, da Anvisa e das plataformas
  H2 Perguntas frequentes
    H3 Quanto custa o tráfego pago para clínica de estética?
    H3 Em quanto tempo aparecem os primeiros resultados?
    H3 Qual é melhor para clínica: Google Ads ou Instagram?
    H3 Vocês atendem clínicas de qualquer cidade?
    H3 Vocês garantem um número de pacientes?
    H3 Os anúncios respeitam as regras do CFM e das plataformas?
    H3 Preciso ter site para anunciar?
    H3 Como eu acompanho os resultados?
  H2 Vamos ver o que dá para melhorar na sua clínica?

## /google-ads-para-clinicas-esteticas/  | title 49 | desc 155 | palavras no <main> 1182
H1 Google Ads para clínica de estética: apareça para quem já está procurando você
  H2 Por que o Google Ads da sua clínica gasta muito e traz pouco
  H2 Como funciona a gestão de Google Ads para clínicas
    H3 Auditoria da conta
    H3 Pesquisa de palavras-chave
    H3 Estrutura enxuta
    H3 Otimização semanal
  H2 Campanhas de Google Ads pensadas para clínicas
    H3 Rede de Pesquisa com intenção alta
    H3 Palavras-chave negativas desde o primeiro dia
    H3 Recursos do anúncio e localização
    H3 Como reduzir o custo por clique da clínica no Google Ads
    H3 Políticas de saúde do Google
  H2 O que você recebe na gestão de Google Ads
  H2 O que costuma mudar nos primeiros meses
  H2 Combine com outros serviços
    H3 Meta Ads (Instagram e Facebook)
    H3 Sites e landing pages
    H3 Automação de WhatsApp
    H3 SEO para clínicas
  H2 Perguntas frequentes
    H3 Quanto investir em Google Ads para clínica de estética?
    H3 Posso anunciar “botox” no Google?
    H3 O Google Ads funciona para clínica pequena?
    H3 Quanto tempo leva para ver resultado no Google Ads?
    H3 A conta do Google Ads fica no nome de quem?
    H3 Como sei se os cliques viraram pacientes?
    H3 Vocês usam Performance Max?
  H2 Quer saber se esse serviço faz sentido para sua clínica?

## /meta-ads-para-clinicas-esteticas/  | title 56 | desc 154 | palavras no <main> 1248
H1 Meta Ads para clínica de estética: anúncios no Instagram que geram conversas, não só curtidas
  H2 Por que impulsionar posts não enche a agenda da clínica
  H2 Como funciona a gestão de Meta Ads para clínicas
    H3 Diagnóstico
    H3 Plano de criativos
    H3 Campanhas de mensagens
    H3 Testes e otimização
  H2 Anúncios no Instagram para clínica de estética que geram conversas
    H3 Objetivo certo: mensagens no WhatsApp
    H3 Criativos que educam, não que prometem
    H3 Públicos de acordo com as regras
    H3 Como reduzir o custo por lead da clínica estética no Meta Ads
    H3 Anúncios para harmonização facial e dermatologia
  H2 O que você recebe na gestão de Meta Ads
  H2 O que costuma mudar nos primeiros meses
  H2 Combine com outros serviços
    H3 Google Ads para clínicas
    H3 Sites e landing pages
    H3 Automação de WhatsApp
    H3 SEO para clínicas
  H2 Perguntas frequentes
    H3 Impulsionar post é a mesma coisa que fazer Meta Ads?
    H3 Posso usar fotos de antes e depois nos anúncios do Instagram?
    H3 Quanto investir em anúncios no Instagram para clínica?
    H3 Anúncios para harmonização facial são permitidos?
    H3 Quem produz os criativos dos anúncios?
    H3 Por que meus anúncios na Meta são reprovados?
    H3 O que é um bom custo por lead para clínica?
  H2 Quer saber se esse serviço faz sentido para sua clínica?

## /criacao-de-sites-para-clinicas-esteticas/  | title 55 | desc 152 | palavras no <main> 1153
H1 Criação de site para clínica de estética e landing pages que transformam visitas em agendamentos
  H2 Por que tantos sites de clínica não geram contatos
  H2 Como funciona a criação do site ou da landing page
    H3 Briefing
    H3 Estrutura e textos
    H3 Design e desenvolvimento
    H3 Publicação e ajustes
  H2 O que uma landing page para clínica estética precisa ter
    H3 Site institucional ou landing page?
    H3 Velocidade também é conversão
    H3 Site para dermatologista e clínica de harmonização facial
  H2 O que você recebe na criação do site
  H2 O que costuma melhorar com uma página bem feita
  H2 Combine com outros serviços
    H3 Google Ads para clínicas
    H3 Meta Ads (Instagram e Facebook)
    H3 Automação de WhatsApp
    H3 SEO para clínicas
  H2 Perguntas frequentes
    H3 Quanto custa um site para clínica de estética?
    H3 Qual a diferença entre site e landing page?
    H3 Em quanto tempo o site fica pronto?
    H3 O site vai aparecer no Google?
    H3 Posso colocar fotos de antes e depois no site?
    H3 O site fica no meu nome?
  H2 Quer saber se esse serviço faz sentido para sua clínica?

## /automacao-whatsapp-para-clinicas/  | title 60 | desc 153 | palavras no <main> 1118
H1 Automação de WhatsApp para clínica: responda em segundos e não perca nenhum interessado
  H2 Quanto custa um contato que ninguém respondeu?
  H2 Como funciona a automação de WhatsApp para clínicas
    H3 Mapeamento do atendimento
    H3 Desenho dos fluxos
    H3 Implementação e testes
    H3 Acompanhamento
  H2 Atendimento automático no WhatsApp para clínica de estética
    H3 Boas-vindas imediata, inclusive fora do horário
    H3 Triagem simples
    H3 Follow-up programado
    H3 Lembretes de avaliação
    H3 Por que o tempo de resposta importa tanto
    H3 Follow-up de leads: onde está o dinheiro esquecido
    H3 Automação com responsabilidade
  H2 O que você recebe na automação de WhatsApp
  H2 O que costuma melhorar com a automação
  H2 Combine com outros serviços
    H3 Google Ads para clínicas
    H3 Meta Ads (Instagram e Facebook)
    H3 Sites e landing pages
    H3 SEO para clínicas
  H2 Perguntas frequentes
    H3 A automação vai substituir minha recepcionista?
    H3 Funciona com o WhatsApp Business que eu já uso?
    H3 Quanto custa a automação de WhatsApp para clínica?
    H3 Posso enviar mensagens para quem não respondeu?
    H3 A automação pede dados de saúde do paciente?
    H3 Em quanto tempo a automação fica pronta?
  H2 Quer saber se esse serviço faz sentido para sua clínica?

## /seo-para-clinicas-esteticas/  | title 48 | desc 154 | palavras no <main> 1087
H1 SEO para clínica de estética: seja encontrada no Google sem depender só de anúncios
  H2 Por que a sua clínica não aparece no Google
  H2 Como funciona o SEO para clínicas
    H3 Diagnóstico
    H3 Plano de palavras-chave
    H3 Otimização
    H3 Acompanhamento
  H2 Os 4 pilares do SEO para clínicas de estética
    H3 1. SEO técnico
    H3 2. Páginas de procedimento
    H3 3. SEO local
    H3 4. Autoridade
    H3 Como fazer a clínica aparecer no Google sem pagar por clique
    H3 SEO e tráfego pago juntos
  H2 O que você recebe no serviço de SEO
  H2 O que costuma melhorar com SEO
  H2 Combine com outros serviços
    H3 Google Ads para clínicas
    H3 Meta Ads (Instagram e Facebook)
    H3 Sites e landing pages
    H3 Automação de WhatsApp
  H2 Perguntas frequentes
    H3 Quanto tempo o SEO leva para dar resultado?
    H3 Qual a diferença entre SEO e Google Ads?
    H3 O Perfil da Empresa no Google (Google Meu Negócio) faz parte do SEO?
    H3 Posso pedir avaliações para meus pacientes no Google?
    H3 Quanto custa SEO para clínica de estética?
    H3 Preciso ter um blog para fazer SEO?
  H2 Quer saber se esse serviço faz sentido para sua clínica?

## /precos/  | title 54 | desc 155 | palavras no <main> 875
H1 Quanto custa tráfego pago para clínica: preços claros, sem surpresas
  H2 Preço da gestão de tráfego por serviço
  H2 Quanto investir em tráfego pago para clínica
    H3 Quando vale investir mais que o mínimo
  H2 O que a gestão de tráfego inclui
    H3 Por que o contrato mínimo é de 3 meses
    H3 Como medir o retorno do investimento
  H2 Solicitar orçamento
  H2 Perguntas frequentes
    H3 Quanto custa um gestor de tráfego para clínica?
    H3 A verba dos anúncios está inclusa na gestão?
    H3 Qual a verba mínima para anunciar?
    H3 Por que o contrato mínimo é de 3 meses?
    H3 Quanto custa um site ou uma automação?
    H3 Existe taxa de setup?
  H2 Prefere conversar antes de decidir?

## /auditoria-gratuita-de-anuncios/  | title 60 | desc 150 | palavras no <main> 626
H1 Auditoria gratuita de anúncios para clínicas: descubra onde sua verba está vazando
  H2 Solicite sua auditoria gratuita
  H2 O que entra na análise da sua conta de anúncios
    H3 Google Ads
    H3 Meta Ads
    H3 Página e WhatsApp
  H2 Como funciona a auditoria gratuita
    H3 Você preenche o formulário
    H3 Combinamos o acesso
    H3 Análise detalhada
    H3 Apresentação por vídeo
  H2 Sinais de que sua conta precisa de uma auditoria
  H2 Perguntas frequentes
    H3 A auditoria é realmente gratuita?
    H3 Preciso dar acesso à minha conta?
    H3 E se eu ainda não anuncio?
    H3 Quanto tempo leva?
    H3 Por que meus anúncios não trazem pacientes?
  H2 Prefere pedir pelo WhatsApp?

## /ebook/  | title 53 | desc 153 | palavras no <main> 267
H1 E-book gratuito: guia prático de tráfego pago para clínicas de estética
  H2 Receba o e-book gratuitamente
  H2 O que você vai aprender
  H2 Para quem é este e-book
    H3 Clínicas que ainda não anunciam
    H3 Quem só impulsiona posts
    H3 Quem já investe e quer melhorar
  H2 Prefere tirar dúvidas direto comigo?

## /sobre/  | title 51 | desc 151 | palavras no <main> 386
H1 Arno Hoberg, gestor de tráfego pago para clínicas de estética
  H2 Por que escolhi trabalhar só com clínicas
    H3 Especialista em tráfego para clínicas estéticas
    H3 Consultor de marketing digital, não um painel de métricas
  H2 Como eu trabalho
    H3 Campanhas enxutas
    H3 Transparência
    H3 Ética em primeiro lugar
    H3 Comunicação direta
  H2 Meu método em 4 etapas
    H3 Diagnóstico e auditoria
    H3 Campanhas enxutas
    H3 Otimização semanal
    H3 Escala com controle
  H2 Vamos conversar sobre a sua clínica?

## /regras-de-publicidade-para-clinicas/  | title 53 | desc 156 | palavras no <main> 1714
H1 Regras de publicidade para clínicas de estética: guia prático para anunciar com segurança
  H2 Por que as regras de publicidade importam para clínicas
  H2 Publicidade médica: regras do CFM e do CRM
    H3 Resolução CFM nº 2.336/2023
    H3 Pontos de atenção na publicidade médica
    H3 Imagens de “antes e depois” na medicina
  H2 Outros conselhos profissionais (biomedicina, enfermagem, odontologia e mais)
    H3 Odontologia (CFO e CROs)
    H3 Biomedicina (CFBM e CRBMs)
    H3 Enfermagem (Cofen e Corens)
    H3 Fisioterapia, farmácia e esteticistas
  H2 Anvisa: propaganda de medicamentos e produtos para saúde
    H3 Toxina botulínica e medicamentos sob prescrição
    H3 Preenchedores e outros produtos para saúde
  H2 Código de Defesa do Consumidor e CONAR
  H2 Políticas do Google Ads para saúde e estética
  H2 Políticas do Meta Ads (Instagram e Facebook)
  H2 LGPD: dados de leads e de pacientes
  H2 Checklist antes de publicar um anúncio de clínica
  H2 Fontes oficiais para consulta
  H2 Perguntas frequentes
    H3 Clínica de estética pode postar antes e depois?
    H3 Pode anunciar botox no Instagram ou no Google?
    H3 Posso prometer resultado em um anúncio de clínica?
    H3 Quem é responsável pelo conteúdo do anúncio?
    H3 Preciso de consentimento para usar dados dos leads?
  H2 Quer campanhas que respeitam essas regras?

## /contato/  | title 53 | desc 150 | palavras no <main> 181
H1 Contato: fale com um gestor de tráfego especializado em clínicas
  H2 Prefere deixar uma mensagem?
  H2 O que acontece depois do seu contato
    H3 Primeira conversa
    H3 Diagnóstico
    H3 Proposta
    H3 Início
  H2 Pronto para conversar?

## /politica-de-privacidade/  | title 44 | desc 155 | palavras no <main> 396
H1 Política de Privacidade
  H2 1. Quem é o controlador dos dados
  H2 2. Quais dados coletamos
  H2 3. Para que usamos os dados e bases legais
  H2 4. Cookies
  H2 5. Compartilhamento
  H2 6. Transferência internacional
  H2 7. Por quanto tempo guardamos
  H2 8. Seus direitos
  H2 9. Segurança
  H2 10. Alterações

## /termos/  | title 54 | desc 155 | palavras no <main> 225
H1 Termos de Uso
  H2 1. Aceitação
  H2 2. Sobre o conteúdo
  H2 3. Sem garantia de resultados
  H2 4. Contratação de serviços
  H2 5. Propriedade intelectual
  H2 6. Links externos
  H2 7. Legislação e foro
  H2 8. Contato

## /obrigado/  | title 44 | desc 154 | palavras no <main> 178
H1 Obrigado! Recebemos seu pedido
  H2 Enquanto isso, conheça os serviços
    H3 Google Ads para clínicas
    H3 Meta Ads (Instagram e Facebook)
    H3 Sites e landing pages
    H3 Automação de WhatsApp
    H3 SEO para clínicas
```n