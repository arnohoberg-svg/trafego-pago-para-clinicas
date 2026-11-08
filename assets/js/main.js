/* Arno Hoberg | Tráfego Pago para Clínicas — JS mínimo (carregado com defer) */
(function () {
  'use strict';

  /* ============ CONFIGURAÇÃO (preencha antes de publicar) ============ */
  var CONFIG = {
    whatsapp: '5548988387867',         // (48) 98838-7867 — só números, com DDI e DDD
    formEndpoint: '{{FORM_ENDPOINT}}',  // ex.: https://formspree.io/f/xxxxxx (aceita POST JSON)
    ebookUrl: '{{EBOOK_PDF_URL}}',      // link do PDF do e-book (após definir o tema)
    gtmId: '',                          // ex.: 'GTM-XXXXXXX'  (recomendado: GA4 e Meta Pixel via GTM)
    ga4Id: '',                          // ex.: 'G-XXXXXXXXXX' (use só se NÃO usar GTM)
    metaPixelId: ''                     // ex.: '123456789012345' (use só se NÃO usar GTM)
  };
  var CONSENT_KEY = 'ah_consent_v1';

  window.dataLayer = window.dataLayer || [];
  function track(event, params) {
    var data = { event: event };
    for (var k in params) { if (Object.prototype.hasOwnProperty.call(params, k)) data[k] = params[k]; }
    window.dataLayer.push(data);
    if (typeof window.fbq === 'function') {
      var map = { whatsapp_click: 'Contact', generate_lead: 'Lead', ebook_download: 'Lead' };
      if (map[event]) window.fbq('track', map[event]);
    }
  }
  function isSet(v) { return v && v.indexOf('{{') === -1; }

  /* ============ Menu responsivo ============ */
  var toggle = document.querySelector('.menu-toggle');
  var nav = document.getElementById('site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', String(!open));
      nav.classList.toggle('is-open', !open);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('is-open')) {
        toggle.setAttribute('aria-expanded', 'false'); nav.classList.remove('is-open'); toggle.focus();
      }
    });
  }
  Array.prototype.forEach.call(document.querySelectorAll('.nav-sub-toggle'), function (btn) {
    var sub = document.getElementById(btn.getAttribute('aria-controls'));
    btn.addEventListener('click', function () {
      var open = btn.getAttribute('aria-expanded') === 'true';
      btn.setAttribute('aria-expanded', String(!open));
      sub.hidden = open;
      sub.classList.toggle('is-open', !open);
    });
  });

  /* ============ Consentimento de cookies (LGPD) ============ */
  function getConsent() { try { return localStorage.getItem(CONSENT_KEY); } catch (e) { return null; } }
  function setConsent(v) { try { localStorage.setItem(CONSENT_KEY, v); } catch (e) {} }
  function loadScript(src) { var s = document.createElement('script'); s.async = true; s.src = src; document.head.appendChild(s); }

  function loadTrackers() {
    if (window.__trackersLoaded) return; window.__trackersLoaded = true;
    // Consent Mode v2: atualiza para concedido
    window.gtag = window.gtag || function () { window.dataLayer.push(arguments); };
    window.gtag('consent', 'update', { ad_storage: 'granted', analytics_storage: 'granted', ad_user_data: 'granted', ad_personalization: 'granted' });
    if (CONFIG.gtmId) {
      window.dataLayer.push({ 'gtm.start': Date.now(), event: 'gtm.js' });
      loadScript('https://www.googletagmanager.com/gtm.js?id=' + CONFIG.gtmId);
      return;
    }
    if (CONFIG.ga4Id) {
      loadScript('https://www.googletagmanager.com/gtag/js?id=' + CONFIG.ga4Id);
      window.gtag('js', new Date()); window.gtag('config', CONFIG.ga4Id);
    }
    if (CONFIG.metaPixelId) {
      /* Meta Pixel (código oficial resumido) */
      !function (f, b, e, v, n, t, s) { if (f.fbq) return; n = f.fbq = function () { n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments); }; if (!f._fbq) f._fbq = n; n.push = n; n.loaded = !0; n.version = '2.0'; n.queue = []; t = b.createElement(e); t.async = !0; t.src = v; s = b.getElementsByTagName(e)[0]; s.parentNode.insertBefore(t, s); }(window, document, 'script', 'https://connect.facebook.net/en_US/fbevents.js');
      window.fbq('init', CONFIG.metaPixelId); window.fbq('track', 'PageView');
    }
  }

  var banner = document.getElementById('cookie-banner');
  function showBanner() { if (banner) banner.hidden = false; }
  function hideBanner() { if (banner) banner.hidden = true; }
  var consent = getConsent();
  if (consent === 'granted') loadTrackers();
  else if (!consent) {
    // mostra o banner depois do primeiro paint para não competir com o LCP
    window.addEventListener('load', function () { setTimeout(showBanner, 600); });
  }
  document.addEventListener('click', function (e) {
    var t = e.target.closest('[data-consent]');
    if (!t) return;
    var v = t.getAttribute('data-consent');
    if (v === 'accept') { setConsent('granted'); hideBanner(); loadTrackers(); }
    else if (v === 'reject') { setConsent('denied'); hideBanner(); }
    else if (v === 'open') { showBanner(); var first = banner && banner.querySelector('button'); if (first) first.focus(); }
  });

  /* ============ Rastreamento de cliques no WhatsApp ============ */
  document.addEventListener('click', function (e) {
    var a = e.target.closest('a[href*="wa.me/"]');
    if (a) track('whatsapp_click', { link_location: a.getAttribute('data-loc') || 'conteudo', page_path: location.pathname });
  });

  function waUrl(text) { return 'https://wa.me/' + CONFIG.whatsapp + '?text=' + encodeURIComponent(text); }

  /* ============ Mini-questionário de orçamento → WhatsApp ============ */
  Array.prototype.forEach.call(document.querySelectorAll('form[data-quote]'), function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var services = Array.prototype.map.call(form.querySelectorAll('input[name="servico"]:checked'), function (i) { return i.value; });
      var msg = form.querySelector('.form-msg');
      if (!services.length) {
        msg.textContent = 'Selecione pelo menos um serviço para montar o orçamento.';
        msg.className = 'form-msg is-error'; form.querySelector('input[name="servico"]').focus(); return;
      }
      var esp = form.querySelector('[name="especialidade"]');
      var verba = form.querySelector('[name="verba"]');
      var text = 'Olá! Vim pelo site e gostaria de um orçamento.\n\n' +
        'Serviços que procuro:\n' + services.map(function (s) { return '• ' + s; }).join('\n') +
        (esp && esp.value ? '\n\nEspecialidade da clínica: ' + esp.value : '') +
        (verba && verba.value ? '\nInvestimento atual em anúncios: ' + verba.value : '');
      msg.textContent = 'Abrindo o WhatsApp com sua mensagem pronta…'; msg.className = 'form-msg is-ok';
      track('whatsapp_click', { link_location: 'questionario_orcamento', servicos: services.join('|') });
      window.open(waUrl(text), '_blank', 'noopener');
    });
  });

  /* ============ Formulários de captura (auditoria, e-book, contato) ============ */
  function validPhone(v) { var d = v.replace(/\D/g, ''); return d.length >= 10 && d.length <= 13; }
  function setError(field, text) {
    var err = document.getElementById(field.id + '-erro');
    field.setAttribute('aria-invalid', text ? 'true' : 'false');
    if (err) err.textContent = text || '';
  }
  Array.prototype.forEach.call(document.querySelectorAll('form[data-lead]'), function (form) {
    var tel = form.querySelector('input[type="tel"]');
    if (tel) tel.addEventListener('input', function () {
      var d = tel.value.replace(/\D/g, '').slice(0, 11);
      if (d.length > 6) tel.value = '(' + d.slice(0, 2) + ') ' + d.slice(2, d.length - 4) + '-' + d.slice(-4);
      else if (d.length > 2) tel.value = '(' + d.slice(0, 2) + ') ' + d.slice(2);
      else tel.value = d;
    });
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var msg = form.querySelector('.form-msg');
      var ok = true, firstBad = null;
      Array.prototype.forEach.call(form.querySelectorAll('[required]'), function (f) {
        var bad = '';
        if (f.type === 'checkbox' && !f.checked) bad = 'É preciso aceitar para continuar.';
        else if (f.type !== 'checkbox' && !f.value.trim()) bad = 'Preencha este campo.';
        else if (f.type === 'tel' && !validPhone(f.value)) bad = 'Informe um WhatsApp válido com DDD.';
        setError(f, bad);
        if (bad) { ok = false; if (!firstBad) firstBad = f; }
      });
      if (!ok) { msg.textContent = 'Revise os campos destacados.'; msg.className = 'form-msg is-error'; firstBad.focus(); return; }
      if (form.querySelector('.hp input') && form.querySelector('.hp input').value) return; // anti-spam

      var data = {};
      Array.prototype.forEach.call(form.elements, function (el) {
        if (!el.name || el.type === 'submit') return;
        data[el.name] = el.type === 'checkbox' ? el.checked : el.value.trim();
      });
      data.origem = form.getAttribute('data-lead');
      data.pagina = location.href;
      data.consentimento_em = new Date().toISOString();

      var origem = data.origem;
      var done = function () {
        track('generate_lead', { form_name: origem });
        if (origem === 'ebook') track('ebook_download', { form_name: origem });
        var base = form.getAttribute('data-thanks') || '../obrigado/';
        window.location.href = base + '?origem=' + encodeURIComponent(origem);
      };
      var fallbackWa = function () {
        // Sem endpoint configurado (ou falha no envio): segue pelo WhatsApp com os dados preenchidos
        var intro = {
          auditoria: 'Olá! Estava no site e gostaria de uma auditoria gratuita.',
          ebook: 'Olá! Vim pelo site, gostaria de entender mais sobre o seu processo. Também quero receber o e-book gratuito.'
        };
        var text = (intro[origem] || 'Olá! Vim pelo site, gostaria de entender mais sobre o seu processo.') + '\n\n' +
          '• Nome: ' + (data.nome || '') + '\n• Clínica: ' + (data.clinica || '') + '\n• Especialidade: ' + (data.especialidade || '') +
          (data.plataforma ? '\n• Anuncia hoje em: ' + data.plataforma : '') + (data.mensagem ? '\n• Mensagem: ' + data.mensagem : '');
        track('generate_lead', { form_name: origem, metodo: 'whatsapp' });
        msg.textContent = 'Abrindo o WhatsApp para concluir seu pedido…'; msg.className = 'form-msg is-ok';
        window.location.href = waUrl(text);
      };

      if (!isSet(CONFIG.formEndpoint)) { fallbackWa(); return; }
      var btn = form.querySelector('[type="submit"]');
      btn.disabled = true; msg.textContent = 'Enviando…'; msg.className = 'form-msg';
      fetch(CONFIG.formEndpoint, { method: 'POST', headers: { 'Content-Type': 'application/json', Accept: 'application/json' }, body: JSON.stringify(data) })
        .then(function (r) { if (!r.ok) throw new Error(r.status); done(); })
        .catch(function () { btn.disabled = false; fallbackWa(); });
    });
  });

  /* ============ Página de agradecimento ============ */
  var thanks = document.querySelector('[data-thanks-page]');
  if (thanks) {
    var origem = new URLSearchParams(location.search).get('origem');
    var box = document.getElementById('ebook-download');
    if (origem === 'ebook' && box) {
      box.hidden = false;
      var link = box.querySelector('a');
      if (isSet(CONFIG.ebookUrl)) link.href = CONFIG.ebookUrl;
      link.addEventListener('click', function () { track('ebook_download', { metodo: 'link' }); });
    }
  }
})();
