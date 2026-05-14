---
marp: true
theme: default
paginate: true
style: |
  /* ── RESET & BASE ── */
  * { box-sizing: border-box; margin: 0; padding: 0; }

  section {
    font-family: 'Trebuchet MS', sans-serif;
    background: #0A0E1A;
    color: #E2E8F0;
    padding: 0;
    width: 1280px;
    height: 720px;
    position: relative;
    overflow: hidden;
  }

  /* ── GRID OVERLAY (decorative) ── */
  section::before {
    content: '';
    position: absolute;
    inset: 0;
    background-image:
      linear-gradient(rgba(0,212,255,0.04) 1px, transparent 1px),
      linear-gradient(90deg, rgba(0,212,255,0.04) 1px, transparent 1px);
    background-size: 128px 72px;
    pointer-events: none;
    z-index: 0;
  }

  section > * { position: relative; z-index: 1; }

  /* ── HEADER BAR (all content slides) ── */
  section.content header {
    display: none;
  }
  section .slide-header {
    background: #060B14;
    border-bottom: 3px solid #00D4FF;
    padding: 10px 40px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 62px;
    flex-shrink: 0;
  }
  section .slide-header .title {
    font-size: 22px;
    font-weight: 700;
    color: #FFFFFF;
    letter-spacing: 0.5px;
  }
  section .slide-header .subtitle {
    font-size: 12px;
    color: #94A3B8;
  }

  /* ── BODY ── */
  section .body {
    padding: 22px 40px;
    height: calc(100% - 62px);
    display: flex;
    flex-direction: column;
    gap: 14px;
  }

  /* ── CARDS ── */
  .card {
    background: #111827;
    border: 1px solid #1E3A5F;
    border-left: 5px solid #00D4FF;
    padding: 14px 18px;
    border-radius: 2px;
  }
  .card.green  { border-left-color: #00FF88; }
  .card.red    { border-left-color: #FF3B5C; }
  .card.muted  { border-left-color: #64748B; }
  .card.amber  { border-left-color: #FFB800; }
  .card.top    { border-left: 1px solid #1E3A5F; border-top: 4px solid #00D4FF; }
  .card.top.green { border-top-color: #00FF88; }
  .card.top.muted { border-top-color: #64748B; }

  .card-title {
    font-size: 15px;
    font-weight: 700;
    color: #00D4FF;
    margin-bottom: 6px;
  }
  .card-title.green  { color: #00FF88; }
  .card-title.red    { color: #FF3B5C; }
  .card-title.muted  { color: #94A3B8; }
  .card-title.amber  { color: #FFB800; }
  .card-title.mono   { font-family: 'Consolas', monospace; font-size: 13px; letter-spacing: 2px; }

  .card p, .card li { font-size: 13px; color: #E2E8F0; line-height: 1.5; }
  .card .detail     { font-size: 12px; color: #94A3B8; margin-top: 6px; }

  /* ── GRID LAYOUTS ── */
  .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
  .grid-3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 14px; }

  /* ── STAT BLOCKS ── */
  .stat {
    background: #1E2A3A;
    border: 1px solid #1E3A5F;
    padding: 14px;
    text-align: center;
    border-radius: 2px;
  }
  .stat .val  { font-family: 'Consolas', monospace; font-size: 26px; font-weight: 700; color: #00D4FF; }
  .stat .val.green { color: #00FF88; }
  .stat .val.muted { color: #94A3B8; }
  .stat .lbl  { font-size: 11px; color: #94A3B8; margin-top: 4px; }

  /* ── TABLE ── */
  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 12.5px;
  }
  thead tr { background: #0D2137; }
  thead th { color: #FFFFFF; font-weight: 700; padding: 8px 12px; text-align: left; border-bottom: 2px solid #00D4FF; }
  tbody tr:nth-child(odd)  td { background: #111827; }
  tbody tr:nth-child(even) td { background: #1E2A3A; }
  tbody td { padding: 7px 12px; border-bottom: 1px solid #1E3A5F; color: #E2E8F0; }
  tbody td.mono  { font-family: 'Consolas', monospace; color: #00D4FF; font-size: 12px; }
  tbody td.green { font-family: 'Consolas', monospace; color: #00FF88; font-size: 12px; }

  /* ── QUOTE BLOCK ── */
  blockquote {
    background: #1E2A3A;
    border: 1px solid #1E3A5F;
    border-left: 5px solid #00D4FF;
    padding: 14px 18px;
    border-radius: 2px;
    margin: 0;
  }
  blockquote p { font-size: 13.5px; color: #E2E8F0; font-style: italic; line-height: 1.55; }
  blockquote p strong { color: #00D4FF; font-style: normal; font-size: 22px; }

  /* ── BADGE ── */
  .badge {
    display: inline-block;
    padding: 3px 10px;
    font-family: 'Consolas', monospace;
    font-size: 11px;
    font-weight: 700;
    border-radius: 2px;
    background: #00FF88;
    color: #000;
  }
  .badge.red   { background: #FF3B5C; }
  .badge.amber { background: #FFB800; }
  .badge.muted { background: #475569; color: #fff; }

  /* ── CODE / MONO ── */
  code {
    font-family: 'Consolas', monospace;
    color: #00D4FF;
    background: transparent;
    font-size: 1em;
  }

  /* ── PAGINATION ── */
  section::after {
    content: attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total);
    position: absolute;
    bottom: 14px;
    right: 28px;
    font-size: 11px;
    color: #1E3A5F;
    font-family: 'Consolas', monospace;
    z-index: 10;
  }

  /* ── NOTE STRIP ── */
  .note {
    background: #1A1000;
    border: 1px solid #3A2800;
    padding: 8px 14px;
    border-radius: 2px;
    font-size: 11px;
    color: #FFB800;
    font-style: italic;
  }

  /* ── COVER SLIDE ── */
  section.cover::before {
    background-image:
      linear-gradient(rgba(0,212,255,0.06) 1px, transparent 1px),
      linear-gradient(90deg, rgba(0,212,255,0.06) 1px, transparent 1px);
    background-size: 128px 72px;
  }
  section.cover {
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 0 80px;
    border-left: 7px solid #00D4FF;
  }
  section.cover .inst {
    font-family: 'Consolas', monospace;
    font-size: 11px;
    color: #00D4FF;
    letter-spacing: 4px;
    text-transform: uppercase;
    margin-bottom: 36px;
  }
  section.cover h1 {
    font-size: 54px;
    font-weight: 700;
    color: #FFFFFF;
    line-height: 1.1;
    margin-bottom: 0;
    border: none;
  }
  section.cover h1 span { color: #00D4FF; }
  section.cover .dataset {
    font-size: 18px;
    color: #94A3B8;
    margin-top: 14px;
    margin-bottom: 40px;
    padding-top: 14px;
    border-top: 1px solid #1E3A5F;
    width: 560px;
  }
  section.cover .author-card {
    background: #111827;
    border: 1px solid #1E3A5F;
    border-left: 5px solid #00FF88;
    padding: 16px 22px;
    width: 580px;
    border-radius: 2px;
  }
  section.cover .author-card .name { font-size: 18px; font-weight: 700; color: #FFFFFF; }
  section.cover .author-card .meta { font-size: 12px; color: #94A3B8; margin-top: 6px; line-height: 1.6; }

  section.cover .btc-deco {
    position: absolute;
    right: 80px;
    top: 50%;
    transform: translateY(-50%);
    font-size: 180px;
    color: #F7931A;
    opacity: 0.12;
    font-weight: 900;
    line-height: 1;
    z-index: 0;
    user-select: none;
  }

  /* ── INDEX SLIDE ── */
  section.index-slide .body {
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 12px;
  }
  .index-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
  }
  .index-item {
    background: #111827;
    border: 1px solid #1E3A5F;
    border-left: 5px solid #00D4FF;
    padding: 14px 18px;
    border-radius: 2px;
  }
  .index-item.green { border-left-color: #00FF88; }
  .index-item.red   { border-left-color: #FF3B5C; }
  .index-item .num  { font-family: 'Consolas', monospace; font-size: 24px; font-weight: 700; color: #00D4FF; }
  .index-item.green .num { color: #00FF88; }
  .index-item.red   .num { color: #FF3B5C; }
  .index-item .lbl  { font-size: 14px; color: #E2E8F0; margin-top: 6px; }

  /* ── MODELO CARD (clasificadores) ── */
  .model-card {
    background: #111827;
    border: 1px solid #1E3A5F;
    border-top: 5px solid #00D4FF;
    padding: 16px;
    border-radius: 2px;
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  .model-card.green { border-top-color: #00FF88; }
  .model-card.muted { border-top-color: #64748B; }
  .model-badge {
    display: inline-block;
    font-family: 'Consolas', monospace;
    font-size: 11px;
    font-weight: 700;
    padding: 3px 10px;
    background: #00D4FF;
    color: #000;
    border-radius: 2px;
    align-self: flex-start;
  }
  .model-badge.green { background: #00FF88; }
  .model-badge.muted { background: #475569; color: #fff; }
  .model-card h3 { font-size: 16px; font-weight: 700; color: #FFFFFF; margin: 0; }
  .model-card .concept-lbl {
    font-family: 'Consolas', monospace; font-size: 10px; letter-spacing: 2px;
    color: #00D4FF; text-transform: uppercase;
  }
  .model-card.green .concept-lbl { color: #00FF88; }
  .model-card.muted .concept-lbl { color: #94A3B8; }
  .model-card p { font-size: 12px; color: #E2E8F0; line-height: 1.45; }
  .model-card .param { font-size: 11px; color: #94A3B8; font-style: italic; }

  /* ── CONCLUSION CARD ── */
  .concl-card {
    background: #111827;
    border: 1px solid #1E3A5F;
    border-left: 5px solid #00D4FF;
    padding: 14px 18px;
    border-radius: 2px;
    display: flex;
    align-items: flex-start;
    gap: 14px;
  }
  .concl-card.green { border-left-color: #00FF88; }
  .concl-card.muted { border-left-color: #64748B; }
  .concl-content { flex: 1; }
  .concl-content h3 { font-size: 17px; font-weight: 700; margin-bottom: 4px; color: #00D4FF; }
  .concl-card.green .concl-content h3 { color: #00FF88; }
  .concl-card.muted .concl-content h3 { color: #94A3B8; }
  .concl-content .verdict { font-size: 13px; font-weight: 700; color: #FFFFFF; margin-bottom: 5px; }
  .concl-content .detail  { font-size: 12px; color: #94A3B8; line-height: 1.5; }

  /* ── METRIC CARDS ── */
  .metric-card {
    background: #111827;
    border: 1px solid #1E3A5F;
    border-left: 5px solid #00D4FF;
    padding: 12px 16px;
    border-radius: 2px;
  }
  .metric-card.green  { border-left-color: #00FF88; }
  .metric-card.muted  { border-left-color: #64748B; }
  .metric-card.amber  { border-left-color: #FFB800; }
  .metric-card.red    { border-left-color: #FF3B5C; }
  .metric-card h3 { font-family: 'Consolas', monospace; font-size: 14px; color: #00D4FF; margin-bottom: 5px; }
  .metric-card.green h3 { color: #00FF88; }
  .metric-card.muted h3 { color: #94A3B8; }
  .metric-card.amber h3 { color: #FFB800; }
  .metric-card.red   h3 { color: #FF3B5C; }
  .metric-card p { font-size: 12px; color: #E2E8F0; line-height: 1.4; }

  /* ── BAR CHART (CSS-only) ── */
  .chart-wrap { background: #111827; border: 1px solid #1E3A5F; padding: 16px; border-radius: 2px; }
  .chart-legend { display: flex; gap: 20px; margin-bottom: 14px; }
  .chart-legend .item { display: flex; align-items: center; gap: 6px; font-size: 12px; color: #94A3B8; }
  .chart-legend .dot { width: 12px; height: 12px; border-radius: 2px; flex-shrink: 0; }
  .chart-groups { display: flex; gap: 20px; align-items: flex-end; height: 240px; padding: 0 10px; }
  .metric-group { flex: 1; display: flex; flex-direction: column; align-items: center; gap: 4px; height: 100%; }
  .bars { display: flex; gap: 4px; align-items: flex-end; height: 210px; }
  .bar-wrap { display: flex; flex-direction: column; align-items: center; gap: 2px; }
  .bar { width: 26px; border-radius: 2px 2px 0 0; position: relative; }
  .bar span { position: absolute; top: -18px; left: 50%; transform: translateX(-50%); font-family: 'Consolas', monospace; font-size: 9px; color: #E2E8F0; white-space: nowrap; }
  .bar.nb  { background: #00D4FF; }
  .bar.lr  { background: #00FF88; }
  .bar.svm { background: #64748B; }
  .metric-label { font-size: 11px; color: #94A3B8; text-align: center; }

  /* ── THANK YOU ── */
  section.thankyou {
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 0 80px;
    border-left: 7px solid #00D4FF;
  }
  section.thankyou h1 {
    font-size: 72px; font-weight: 700; color: #FFFFFF; margin: 0; border: none; line-height: 1;
  }
  section.thankyou h2 {
    font-size: 28px; color: #00D4FF; font-weight: 400; margin-top: 10px; border: none;
  }
  section.thankyou hr {
    border: none; border-top: 1px solid #1E3A5F; width: 480px; margin: 28px 0; margin-left: 0;
  }
  section.thankyou .refs { font-size: 12px; color: #94A3B8; line-height: 2; }
  section.thankyou .refs strong { color: #E2E8F0; }
  section.thankyou .shield-deco {
    position: absolute; right: 100px; top: 50%; transform: translateY(-50%);
    font-size: 200px; opacity: 0.07; color: #00D4FF; user-select: none; z-index: 0;
  }

  /* ── SMOTE VISUAL ── */
  .smote-bar { height: 28px; border-radius: 2px; display: flex; overflow: hidden; margin: 8px 0; }
  .smote-bar .seg-white { background: #1E3A5F; flex: 98.62; display: flex; align-items: center; padding-left: 10px; font-size: 11px; color: #94A3B8; }
  .smote-bar .seg-ransom { background: #FF3B5C; flex: 1.38; display: flex; align-items: center; justify-content: center; }

  /* global heading overrides */
  h1, h2, h3 { border: none; padding: 0; margin: 0; }
---

<!-- _class: cover -->

<div class="inst">Instituto Politécnico Nacional · CIC </div>

# Clasificadores basados en Redes Neuronales Artificiales</span>

<div class="dataset">Bitcoin Heist Ransomware Address Dataset</div>

<div class="author-card">
  <div class="name">Ing. Marco Antonio Reséndiz Díaz</div>
  <div class="meta">
    Maestría en Ciencia y Tecnología en IA y Ciencia de Datos<br>
    Dra. Yenny Villuendas · Aprendizaje Automático · Mayo 2026
  </div>
</div>

<div class="btc-deco">₿</div>

---

<!-- _class: index-slide -->

<div class="slide-header">
  <span class="title">Índice</span>
  <span class="subtitle">Redes Neuronales Artificiales</span>
</div>

<div class="body">
<div class="index-grid">
  <div class="index-item">
    <div class="num">01</div>
    <div class="lbl">Introducción</div>
  </div>
  <div class="index-item">
    <div class="num">04</div>
    <div class="lbl">Desempeño de clasificadores</div>
  </div>
  <div class="index-item">
    <div class="num">02</div>
    <div class="lbl">Descripción del conjunto de datos</div>
  </div>
  <div class="index-item green">
    <div class="num">05</div>
    <div class="lbl">Resultados</div>
  </div>
  <div class="index-item">
    <div class="num">03</div>
    <div class="lbl">Tratamiento de los datos</div>
  </div>
  <div class="index-item red">
    <div class="num">06</div>
    <div class="lbl">Conclusiones</div>
  </div>
</div>
</div>

---

<div class="slide-header">
  <span class="title">01 · Introducción</span>
  <span class="subtitle">¿Qué es el Ransomware?</span>
</div>

<div class="body">

<blockquote>
<p><strong>"</strong> Malware que retiene datos o dispositivos confidenciales de una víctima, amenazando con mantenerlos bloqueados a menos que se pague un rescate. <em>— IBM</em></p>
</blockquote>

<div class="grid-2">
  <div class="card">
    <div class="card-title">Ransomware Payment</div>
    <p>Pago realizado a ciberdelincuentes para obtener una clave de cifrado y recuperar el acceso a los datos secuestrados.</p>
  </div>
  <div class="card red">
    <div class="card-title red">⚠ Advertencia crítica</div>
    <p>El pago <strong>NO siempre</strong> garantiza la liberación de los datos o dispositivos afectados.</p>
  </div>
</div>

</div>

---

<div class="slide-header">
  <span class="title">02 · Conjunto de Datos</span>
  <span class="subtitle">Bitcoin Heist Ransomware Address — UCI ML Repository</span>
</div>

<div class="body">

<div class="card" style="border-left: 5px solid #00D4FF; margin-bottom: 4px;">
  <p>Diseñado como un <strong>grafo de características</strong> para detectar patrones de transacciones de Bitcoin asociadas a ransomware.</p>
</div>

| Feature | Tipo | Descripción |
|---|---|---|
| `address` | String | Dirección de Bitcoin |
| `year / day` | Integer | Fecha de la transacción |
| `length` | Integer | Repeticiones del proceso de mezcla |
| `weight` | Float | Grado de fusión de monedas |
| `count` | Integer | Número de transacciones de fusión |
| `looped` | Integer | Transacciones que dividen, mueven y fusionan monedas |
| `neighbors` | Integer | Vecinos en el grafo de transacciones |
| `income` | Integer | Monto en Satoshi |
| `label` | String | Familia ransomware o *"white"* |

</div>

---

<div class="slide-header">
  <span class="title">02 · Features Clave</span>
  <span class="subtitle">Anatomía de las transacciones sospechosas</span>
</div>

<div class="body">

<div class="card">
  <div class="card-title mono">LENGTH</div>
  <p>Cuantifica la cantidad de veces que se repite el proceso de mezcla de Bitcoin para ocultar el origen de las monedas.</p>
</div>

<div class="card green">
  <div class="card-title green mono">WEIGHT</div>
  <p>Mide la <strong>fusión de monedas</strong>: cuando múltiples direcciones de entrada se concentran en una sola salida (coin consolidation).</p>
</div>

<div class="card red">
  <div class="card-title red mono">LOOPED</div>
  <p>Detecta transacciones que <strong>(1)</strong> dividen monedas, <strong>(2)</strong> las mueven por diferentes caminos en la red y <strong>(3)</strong> las fusionan en una sola cuenta.</p>
</div>

<div class="note">Nota: Los registros con label <em>ransomware</em> son confirmados; los <em>white</em> pueden o no estar relacionados.</div>

</div>

---

<div class="slide-header">
  <span class="title">03 · Tratamiento de los Datos</span>
  <span class="subtitle">Preprocesamiento y filtrado</span>
</div>

<div class="body">

<div class="grid-3">
  <div class="stat">
    <div class="val">2,916,697</div>
    <div class="lbl">Registros totales filtrados</div>
  </div>
  <div class="stat">
    <div class="val green">0.3 BTC</div>
    <div class="lbl">Umbral mínimo de transferencia</div>
  </div>
  <div class="stat">
    <div class="val muted">2009–2018</div>
    <div class="lbl">Periodo de análisis</div>
  </div>
</div>

<div class="grid-2">
  <div class="card">
    <div class="card-title">Binarización del Target</div>
    <table>
      <thead><tr><th>Label original</th><th>Target</th></tr></thead>
      <tbody>
        <tr><td class="green">"white"</td><td>0 — posiblemente no ransomware</td></tr>
        <tr><td class="mono">Familia ransomware</td><td>1 — confirmado ransomware</td></tr>
      </tbody>
    </table>
  </div>
  <div class="card green">
    <div class="card-title green">SMOTE — Balanceo</div>
    <p><strong style="color:#FF3B5C;">Desbalance severo:</strong> 98.62% clase 0 vs 1.38% clase 1</p>
    <div class="smote-bar">
      <div class="seg-white">98.62% white</div>
      <div class="seg-ransom"></div>
    </div>
  </div>
</div>

</div>

---

<div class="slide-header">
  <span class="title">03 · Orange Workflow</span>
  <span class="subtitle">Orange</span>
</div>

<div class="body">

  <figure>
    <img src="IMG/rna_orange_workflow.png" width="800"/>
  </figure>

</div>

---

<div class="slide-header">
  <span class="title">04 · Validación</span>
  <span class="subtitle">Validación cruzada estratificada</span>
</div>

<div class="body">

<div class="card" style="margin-bottom: 4px;">
  <p>Combina <strong>k-fold cross validation</strong> con <strong>estratificación</strong> para garantizar representatividad de clases en cada subconjunto. Crítico dado el severo desbalance del dataset.</p>
</div>

<div class="grid-3">
  <div class="card top">
    <div class="card-title mono">K-FOLD</div>
    <p>Divide los datos en k subconjuntos. Entrena con k−1 folds y valida con el restante, rotando hasta cubrir todos.</p>
  </div>
  <div class="card top green">
    <div class="card-title green mono">ESTRATIFICACIÓN</div>
    <p>Garantiza que cada fold mantenga la misma proporción de clases. Esencial para datasets desbalanceados.</p>
  </div>
  <div class="card top muted">
    <div class="card-title muted mono">CONFIGURACIÓN</div>
    <p><strong>3 folds</strong> para acelerar el entrenamiento. Cada modelo se evalúa en las 3 particiones y se promedia el desempeño.</p>
  </div>
</div>

</div>

---

<div class="slide-header">
  <span class="title">04 · Clasificadores</span>
  <span class="subtitle">Tres modelos basados en Redes Neurnales Artificiales</span>
</div>

<div class="body">

<div class="grid-3" style="flex: 1;">
  <div class="model-card">
    <h3>RN1_Relu_Adam</h3>
    <div class="concept-lbl">Configuración</div>
    <p>
      - Neuronas: 100
      - Activación: ReLU
      - Solver: Adam
      - Regularization: 0.001
      - Max iteraciones: 200
    </p>
  </div>
  <div class="model-card green">
    <h3>RN2_tanh_L_BFGS_B</h3>
    <div class="concept-lbl">Configuración</div>
    <p>
      - Neuronas: 100
      - Activación: tanh
      - Solver: L-BFGS-B
      - Regularization: 0.001
      - Max iteraciones: 200
    </p>
  </div>
  <div class="model-card muted">
    <h3>RN3_Logistic_SGD</h3>
    <div class="concept-lbl">Configuración</div>
    <p>
      - Neuronas: 100
      - Activación: Logistic
      - Solver: SGD
      - Regularization: 0.001
      - Max iteraciones: 200
    </p>
  </div>
</div>

<div class="note">
Donde:

- Neuronas: Indica que la capa oculta de la red neuronal contiene k neuronas
- Activación: Define la función de activación utilizada por las neuronas para transformar la información recibida
- Solver: Es el algoritmo encargado de optimizar los pesos de la red durante el entrenamiento.
- Regularization: Ayuda a reducir el sobreajuste penalizando pesos excesivamente grandes.
- Max Iteraciones: Número máximo de iteraciones permitidas durante el entrenamiento de la red neuronal

</div>

</div>

---

<div class="slide-header">
  <span class="title">05 · Medidas de Desempeño</span>
  <span class="subtitle">Métricas de evaluación</span>
</div>

<div class="body">

<div class="grid-2">
  <div class="metric-card">
    <h3>Recall</h3>
    <p>Habilidad de encontrar <strong>todas las muestras positivas</strong>. Mide cuántos ransomwares reales detectamos sobre el total real.</p>
  </div>
  <div class="metric-card green">
    <h3>Precision</h3>
    <p>Habilidad de <strong>no etiquetar positivos como negativos</strong>. Mide la pureza de las alertas generadas.</p>
  </div>
  <div class="metric-card muted">
    <h3>Accuracy</h3>
    <p>Proporción de <strong>predicciones correctas</strong> sobre el total de predicciones realizadas.</p>
  </div>
  <div class="metric-card amber">
    <h3>F1 Score</h3>
    <p><strong>Media armónica</strong> entre Precision y Recall. Equilibra ambas métricas en un solo valor representativo.</p>
  </div>
</div>

<div class="metric-card red">
  <h3>AUC-ROC</h3>
  <p>Área bajo la curva ROC. Mide la capacidad de <strong>distinguir entre clases a diferentes umbrales</strong> de decisión.</p>
</div>

</div>

---

<div class="slide-header">
  <span class="title">05 · Resultados</span>
  <span class="subtitle">Comparación de métricas entre clasificadores</span>
</div>

<div class="body">

| Modelo            | Train    | AUC   | CA    | F1    | Prec  | Recall |
| ----------------- | -------- | ----- | ----- | ----- | ----- | ------ |
| RN1_Relu_Adam     | 1111.953 | 0.884 | 0.811 | 0.808 | 0.825 | 0.811  |
| RN2_tanh_L_BFGS_B | 2386.158 | 0.768 | 0.687 | 0.686 | 0.691 | 0.687  |
| RN3_Logistic_SGD  | 140.143  | 0.477 | 0.500 | 0.335 | 0.527 | 0.500  |

</div>


---

<div class="slide-header">
  <span class="title">05 · ROC Analysis</span>
  <span class="subtitle">ROC Analysis</span>
</div>

<div class="body">

  <figure>
    <img src="IMG/roc_analysis_RNA.png" width="800"/>
  </figure>

</div>




---

<div class="slide-header">
  <span class="title">05 · Matrices de Confusión</span>
  <span class="subtitle">Distribucion de predicciones por modelo</span>
</div>

<div class="body">

<div class="grid-3" style="flex:1; align-items:start;">

  <div class="card" style="border-left-color:#00D4FF;">
    <div class="card-title">RN1_Relu_Adam</div>
    <table style="margin-top:8px;">
      <thead><tr><th></th><th style="text-align:center;color:#94A3B8;font-size:11px;">Pred Neg</th><th style="text-align:center;color:#94A3B8;font-size:11px;">Pred Pos</th></tr></thead>
      <tbody>
        <tr><td style="color:#94A3B8;font-size:11px;">Real Neg</td>
            <td style="text-align:center;background:#001A0D;color:#00FF88;font-size:16px;font-weight:700;font-family:Consolas;">1724197</td>
            <td style="text-align:center;background:#1A0000;color:#FF3B5C;font-size:16px;font-weight:700;font-family:Consolas;">159948</td></tr>
        <tr><td style="color:#94A3B8;font-size:11px;">Real Pos</td>
            <td style="text-align:center;background:#1A0000;color:#FF3B5C;font-size:16px;font-weight:700;font-family:Consolas;">553928</td>
            <td style="text-align:center;background:#001A0D;color:#00FF88;font-size:16px;font-weight:700;font-family:Consolas;">1330217</td></tr>
      </tbody>
    </table>
  </div>

  <div class="card" style="border-left-color:#64748B;">
    <div class="card-title muted">RN2_tanh_L_BFGS_B</div>
    <table style="margin-top:8px;">
      <thead><tr><th></th><th style="text-align:center;color:#94A3B8;font-size:11px;">Pred Neg</th><th style="text-align:center;color:#94A3B8;font-size:11px;">Pred Pos</th></tr></thead>
      <tbody>
        <tr><td style="color:#94A3B8;font-size:11px;">Real Neg</td>
            <td style="text-align:center;background:#001A0D;color:#00FF88;font-size:16px;font-weight:700;font-family:Consolas;">1416788</td>
            <td style="text-align:center;background:#2A0000;color:#FF3B5C;font-size:16px;font-weight:700;font-family:Consolas;">467357</td></tr>
        <tr><td style="color:#94A3B8;font-size:11px;">Real Pos</td>
            <td style="text-align:center;background:#2A0000;color:#FF3B5C;font-size:16px;font-weight:700;font-family:Consolas;">710745</td>
            <td style="text-align:center;background:#001A0D;color:#00FF88;font-size:16px;font-weight:700;font-family:Consolas;">1173400</td></tr>
      </tbody>
    </table>
  </div>

  <div class="card" style="border-left-color:#00FF88;">
    <div class="card-title green">RN3_Logistic_SGD</div>
    <table style="margin-top:8px;">
      <thead><tr><th></th><th style="text-align:center;color:#94A3B8;font-size:11px;">Pred Neg</th><th style="text-align:center;color:#94A3B8;font-size:11px;">Pred Pos</th></tr></thead>
      <tbody>
        <tr><td style="color:#94A3B8;font-size:11px;">Real Neg</td>
            <td style="text-align:center;background:#001A0D;color:#00FF88;font-size:16px;font-weight:700;font-family:Consolas;">1881048</td>
            <td style="text-align:center;background:#1D0000;color:#FF3B5C;font-size:16px;font-weight:700;font-family:Consolas;">3097</td></tr>
        <tr><td style="color:#94A3B8;font-size:11px;">Real Pos</td>
            <td style="text-align:center;background:#1D0000;color:#FF3B5C;font-size:16px;font-weight:700;font-family:Consolas;">1880299</td>
            <td style="text-align:center;background:#001A0D;color:#00FF88;font-size:16px;font-weight:700;font-family:Consolas;">3846</td></tr>
      </tbody>
    </table>
  </div>
</div>

</div>

---

<div class="slide-header">
  <span class="title">06 · Conclusiones</span>
  <span class="subtitle">Análisis comparativo de los tres clasificadores</span>
</div>

<div class="body">
      <div class="verdict">
      - La configuración RN1 basada en ReLU y Adam obtuvo el mejor desempeño global, alcanzando un AUC de 0.884 y una exactitud de 81.1%, evidenciando una mayor capacidad de discriminación y generalización respecto al resto de configuraciones evaluadas.
      - RN2 presentó un desempeño intermedio, mientras que RN3 mostró resultados cercanos al azar, indicando dificultades de convergencia asociadas al uso de la función logística y el optimizador SGD.
      </div>
      <div class="verdict">
      - RN2 presentó un desempeño intermedio, mientras que RN3 mostró resultados cercanos al azar, indicando dificultades de convergencia asociadas al uso de la función logística y el optimizador SGD.
      </div>
</div>

---

<!-- _class: thankyou -->

<div class="shield-deco">🛡</div>

# Gracias

## por su atención

<hr>

<div class="refs">
  <strong>Referencias</strong><br>
  IBM Think: ibm.com/mx-es/think/topics/ransomware<br>
  UCI ML Repository: Bitcoin Heist Ransomware Address Dataset
</div>