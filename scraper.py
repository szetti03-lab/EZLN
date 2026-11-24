# Auto-generated from the notebook. Env: PART (1-4), TEST_MODE (0/1). Output: results_partN.zip in the working directory.

import os
def display(x):
    print(x.to_string() if hasattr(x,'to_string') else x)


import urllib.request, subprocess, sys
try: urllib.request.urlopen('https://pypi.org', timeout=10)
except Exception as e: raise SystemExit('INTERNET OFF: enable Internet in Settings and re-run. Detail: ' + str(e))
print(subprocess.run([sys.executable,'-m','pip','install','trafilatura','ddgs','beautifulsoup4','pandas','pypdf'],capture_output=True,text=True).stdout[-200:])
import os, re, io, csv, json, time, hashlib, random, datetime, unicodedata, urllib.parse, urllib.robotparser
import requests, pandas as pd, trafilatura
from bs4 import BeautifulSoup
from pypdf import PdfReader
from ddgs import DDGS
OUT = os.environ.get('OUT_DIR', os.path.abspath('scrape_out'))
os.makedirs(OUT, exist_ok=True)
UA = {'User-Agent': 'Mozilla/5.0 (academic research, economics thesis; contact: your-email@example.com)'}  # put your email
T0 = time.time(); print('OUT =', OUT)

CAND_CSV='''marez,evento,anno_da,anno_a
16 de Febrero,nascita,1998,2003
1° de Enero,fine,2004,2013
Acalbaná,nascita,2003,2013
Bochil,fine,1999,2003
Comandanta Ramona,nascita,1998,2003
El Campesino,nascita,2003,2013
Ernesto Che Guevara (anni '90),fine,2004,2013
Huitiupán,fine,1999,2003
Independencia,fine,1999,2003
Ixtapa,nascita,1994,1998
Ixtapa,fine,1999,2003
Jitotol,nascita,1994,1998
Jitotol,fine,1999,2003
José María Morelos y Pavón,fine,1999,2003
La Dignidad,nascita,2003,2013
La Montaña,nascita,1998,2003
La Montaña,fine,2003,2013
Miguel Hidalgo y Costilla,fine,2004,2013
Nicolás Ruiz (concejo autónomo),nascita,1994,1998
Nicolás Ruiz (concejo autónomo),fine,1999,2003
Rubén Jaramillo,nascita,2003,2013
Sabanilla,fine,1999,2003
San José en Rebeldía,nascita,1998,2003
San José en Rebeldía,fine,2003,2013
San Juan Apóstol Cancuc,nascita,1994,1998
San Salvador,fine,1998,2003
Simojovel,fine,1999,2003
Zinacantán,fine,1999,2003
'''
CTL_CSV='''cve_mun_2020,municipio
001,Acacoyagua
002,Acala
003,Acapetahua
005,Amatán
006,Amatenango de la Frontera
008,Ángel Albino Corzo
009,Arriaga
010,Bejucal de Ocampo
011,Bella Vista
012,Berriozábal
015,Cacahoatán
016,Catazajá
017,Cintalapa
018,Coapilla
020,La Concordia
021,Copainalá
022,Chalchihuitán
023,Chamula
025,Chapultenango
027,Chiapa de Corzo
028,Chiapilla
029,Chicoasén
032,Escuintla
033,Francisco León
035,Frontera Hidalgo
036,La Grandeza
037,Huehuetán
040,Huixtla
042,Ixhuatán
043,Ixtacomitán
045,Ixtapangajoya
046,Jiquipilas
048,Juárez
051,Mapastepec
053,Mazapa de Madero
054,Mazatán
055,Metapa
056,Mitontic
060,Ocotepec
061,Ocozocoautla de Espinosa
062,Ostuacán
063,Osumacinta
067,Pantepec
068,Pichucalco
069,Pijijiapan
070,El Porvenir
071,Villa Comaltitlán
072,Pueblo Nuevo Solistahuacán
073,Rayón
074,Reforma
075,Las Rosas
079,San Fernando
080,Siltepec
083,Socoltenango
084,Solosuchiapa
085,Soyaló
086,Suchiapa
087,Suchiate
088,Sunuapa
089,Tapachula
090,Tapalapa
091,Tapilula
092,Tecpatán
093,Tenejapa
097,Tonalá
098,Totolapa
101,Tuxtla Gutiérrez
102,Tuxtla Chico
103,Tuzantán
104,Tzimol
105,Unión Juárez
106,Venustiano Carranza
107,Villa Corzo
108,Villaflores
110,San Lucas
115,Maravilla Tenejapa
117,Montecristo de Guerrero
118,San Andrés Duraznal
119,Santiago el Pinar
120,Capitán Luis Ángel Vidal
121,Rincón Chamula San Pedro
122,El Parral
123,Emiliano Zapata
124,Mezcalapa
125,Honduras de la Sierra
'''
SEEDS = ['https://chiapas.iiec.unam.mx/No9-PDF/ch9monjardin.pdf', 'https://otrosmundoschiapas.org/wp-content/uploads/1998/12/ESTAADOS.pdf', 'https://www.revistamexicanadesociologia.unam.mx/index.php/rms/article/download/60500/53331/171989', 'https://www.frayba.org.mx/sites/default/files/030612_desplazados_por_el_conflicto_armado_frayba.pdf', 'https://desinformemonos.org/la-larga-historia-de-violencia-paramilitar-e-impunidad-de-la-orcao/', 'https://chiapas.iiec.unam.mx/No8-PDF/ch8castro.pdf', 'https://revistas.unam.mx/index.php/antropologia/article/download/9967/pdf_459/30795', 'https://www.ejecentral.com.mx/ezln-da-a-conocer-la-creacion-de-nuevos-caracoles-y-crarez/', 'https://www.jornada.com.mx/2001/01/10/006n1pol.html', 'https://www.redalyc.org/journal/7238/723879811030/723879811030.pdf', 'https://journals.unam.mx/index.php/rmcpys/article/download/42421/38531/109056', 'https://chiapas.iiec.unam.mx/No8-PDF/ch8garcia-nava.pdf', 'https://core.ac.uk/download/478598403.pdf', 'https://chiapas-support.org/2012/12/22/more-than-40000-zapatistas-mobilize-in-chiapas/', 'https://www.elsaltodiario.com/ezln/fuego-zapatismo-opcion-paz-democracia-comunidades-1995-2014', 'https://www.frayba.org.mx/sites/default/files/040716_paramilitarizacion_en_la_zona_norte_de_chiapas_frayba.pdf', 'https://otrosmundoschiapas.org/wp-content/uploads/1998/04/LAS10CSEON.pdf', 'https://scielo.org.mx/pdf/liminar/v21n2/2007-8900-liminar-21-02-e987.pdf', 'https://otrosmundoschiapas.org/wp-content/uploads/1998/06/SENAI.pdf', 'https://www.sipaz.org/2005-2/?lang=en', 'https://frayba.org.mx/sites/default/files/Informes/Informe-Frayba-2023/Informe-Frayba-2023_Chiapas-un-desastre.pdf', 'https://core.ac.uk/download/35157137.pdf', 'https://www.truthdig.com/articles/paramilitary-resurgence-displaces-thousands-in-chiapas/', 'https://www.sipaz.org/in-focus-the-northern-region-a-powder-keg-of-violence/?lang=en', 'https://www.elsaltodiario.com/mapas/ofensiva-paramilitar-contra-la-autonomia-de-los-pueblos-organizados-en-chiapas', 'https://www.redalyc.org/pdf/745/74540109.pdf', 'https://redtdt.org.mx/wp-content/uploads/2023/06/AU_011_2023_BAEZLN_Moises_Chiapas.pdf', 'https://www.frayba.org.mx/sites/default/files/100217_informe_bolom_ajaw_final.pdf', 'https://ru.dgb.unam.mx/bitstream/20.500.14330/TES01000622656/3/0622656.pdf', 'https://chiapas-support.org/2019/08/18/ezln-creates-seven-new-caracols/', 'https://frayba.org.mx/el-presidente-de-la-republica-en-su-mananera-miente-y-encubre-la-violencia-en-chiapas', 'https://frayba.org.mx/sites/default/files/2024-10/241016_au_6deoctubre.pdf', 'https://enlacezapatista.ezln.org.mx/1994/12/19/creacion-de-municipios-autonomos/', 'https://frayba.org.mx/desplazamiento-riesgo-de-despojo-y-amenazas-a-bases-de-apoyo-del-ezln', 'https://ru.dgb.unam.mx/bitstream/20.500.14330/TES01000610950/3/0610950.pdf', 'https://mexiconewsdaily.com/news/zapatistas-to-extend-their-control', 'https://radiozapatista.org/wp-content/uploads/2025/12/informepreliminar2025.pdf', 'https://repositorio.xoc.uam.mx/jspui/bitstream/123456789/407/1/192142.pdf', 'https://www.elsaltodiario.com/ezln/cambios-autonomia-zapatista', 'https://www.centrodemedioslibres.org/wp-content/uploads/2017/08/Gobierno-Autonomo-I-1.pdf', 'https://theanarchistlibrary.org/library/jerome-baschet-the-reorganization-of-zapatista-autonomy', 'https://schoolsforchiapas.org/zapatista-teacher-dead/', 'https://www.jornada.com.mx/2004/09/19/morelia.html', 'https://www.elsaltodiario.com/mapas/narcoviolencia-colapsa-chiapas-entren-militares', 'https://www.jornada.com.mx/2004/09/19/realidad.html', 'https://yachana.org/reports/mex07/2007/07/caracol-morelia.html']
cand = pd.read_csv(io.StringIO(CAND_CSV)); cand = cand[~((cand.marez.isin(['La Dignidad', 'Rubén Jaramillo']) & (cand.evento == 'nascita')) | ((cand.marez == 'Sabanilla') & (cand.evento == 'fine')))]  # resolved by ENAH 2012 thesis (split of Sabanilla in 2003)
ctl = pd.read_csv(io.StringIO(CTL_CSV), dtype=str)
TEST_MODE = os.environ.get('TEST_MODE', '0') == '1'       # <- True for a quick test run (4 MAREZ, 5 controls)
PART = int(os.environ.get('PART', '1'))                # 1, 2 = candidate MAREZ (halves); 3, 4 = control municipalities (halves). Run each part as a separate Commit (~3-4 h each)
BUDGET_MIN = 45 if TEST_MODE else 240   # stop collecting after this many minutes (Kaggle limit is 12 h); extraction always runs
def left(frac): return (time.time() - T0) / 60 < BUDGET_MIN * frac
MAX_LINKS = 20 if TEST_MODE else 150     # link-following budget (channel D)
YEARS_PER_CAND = 3 if TEST_MODE else 5   # year-specific queries per candidate
# Alternative spellings / aliases to look for (edit freely): {'name in table': ['other spelling', ...]}
ALIASES = {'Ricardo Flores Magón': ['Flores Magón'], 'Acalbaná': ['Akabalná', 'Acalbana', 'Akabalna'], 'San Juan Apóstol Cancuc': ['Cancuc', "K'ankujk"],
           'Miguel Hidalgo y Costilla': ['Miguel Hidalgo'], 'José María Morelos y Pavón': ['Morelos'], 'Ernesto Che Guevara (anni \'90)': ['Ernesto Che Guevara'],
           'Independencia': ['La Independencia'], 'San José en Rebeldía': ['San José en Rebeldia'], 'El Campesino': ['Campesino']}
TEST_NAMES = ['Comandanta Ramona', 'San Salvador', 'Rubén Jaramillo', 'Huitiupán']   # test sample: MAREZ with a real, searchable name
if not TEST_MODE:
    h, hc = len(cand) // 2, len(ctl) // 2
    cand, ctl, SEEDS = {1: (cand.iloc[:h], ctl.iloc[:0], SEEDS), 2: (cand.iloc[h:], ctl.iloc[:0], []), 3: (cand.iloc[:0], ctl.iloc[:hc], []), 4: (cand.iloc[:0], ctl.iloc[hc:], [])}[PART]
if TEST_MODE: cand = cand[cand.marez.isin(TEST_NAMES)]; ctl = ctl.head(5); SEEDS = SEEDS[:5]
print('PART', PART, '|', len(cand), 'candidates;', len(ctl), 'controls;', len(SEEDS), 'seeds; TEST_MODE =', TEST_MODE)

ALL_SITES = ['jornada.com.mx','sipaz.org','frayba.org.mx','ciepac.org','enlacezapatista.ezln.org.mx','chiapas-support.org','desinformemonos.org','chiapasparalelo.com','radiozapatista.org']
SITES = ALL_SITES[:3] if TEST_MODE else ALL_SITES
# internal search of sites (WordPress style ?s=) - no search-engine rate limits
SITE_SEARCH = {'www.sipaz.org': 'https://www.sipaz.org/?s={q}', 'enlacezapatista.ezln.org.mx': 'https://enlacezapatista.ezln.org.mx/?s={q}',
               'radiozapatista.org': 'https://radiozapatista.org/?s={q}', 'desinformemonos.org': 'https://desinformemonos.org/?s={q}',
               'chiapasparalelo.com': 'https://chiapasparalelo.com/?s={q}'}
CRAWL_DOMAINS = ('sipaz.org','frayba.org.mx','ciepac.org','enlacezapatista.ezln.org.mx','radiozapatista.org','chiapasparalelo.com','desinformemonos.org')
LINK_KW = re.compile(r'zapatist|ezln|autonom|caracol|junta-de-buen|marez|municipio|chiapas', re.I)
BACKENDS = ['auto','bing','brave','yahoo']

LOG = OUT + '/search_log.csv'; PAGES = OUT + '/pages.jsonl'
LOG_FIELDS = ['ts','qid','query','url','outcome','via']
def log(**kw):
    row = {k: kw.get(k,'') for k in LOG_FIELDS}; row['ts'] = datetime.datetime.now().isoformat()
    new = not os.path.exists(LOG)
    with open(LOG,'a',newline='',encoding='utf-8-sig') as f:
        w = csv.DictWriter(f, fieldnames=LOG_FIELDS)
        if new: w.writeheader()
        w.writerow(row)

_robots = {}
def allowed(url):
    p = urllib.parse.urlparse(url); base = f'{p.scheme}://{p.netloc}'
    if base not in _robots:
        rp = urllib.robotparser.RobotFileParser()
        try:
            r = requests.get(base + '/robots.txt', headers=UA, timeout=15)
            rp.parse(r.text.splitlines()) if r.status_code == 200 else rp.parse([])
        except Exception: rp.parse([])
        _robots[base] = rp
    return _robots[base].can_fetch('*', url)

def pdf_text(content):
    try: return '\n'.join((pg.extract_text() or '') for pg in PdfReader(io.BytesIO(content)).pages)
    except Exception: return ''

def good_links(html, base):
    out = []
    try:
        for a in BeautifulSoup(html, 'html.parser').find_all('a', href=True):
            u = urllib.parse.urljoin(base, a['href']).split('#')[0]
            if u.startswith('http') and any(d in u for d in CRAWL_DOMAINS) and LINK_KW.search(u + ' ' + a.get_text(' ')) \
               and not re.search(r'/(tag|category|author|feed|wp-json|wp-content/themes)/|\?s=|/page/\d', u): out.append(u)
    except Exception: pass
    return list(dict.fromkeys(out))[:40]

def get_text(url):
    r = requests.get(url, headers=UA, timeout=30); r.raise_for_status()
    if 'pdf' in r.headers.get('content-type','').lower() or url.lower().endswith('.pdf'):
        return pdf_text(r.content), r.content, []
    return (trafilatura.extract(r.text, include_comments=False, favor_recall=True) or ''), r.content, good_links(r.text, url)

def wayback(url):
    try:
        j = requests.get('https://archive.org/wayback/available', params={'url': url}, headers=UA, timeout=30).json()
        s = j.get('archived_snapshots', {}).get('closest')
        if s and s.get('available'): return get_text(s['url']) + (s['url'],)
    except Exception: pass
    return None

seen = set()
if os.path.exists(PAGES):
    for l in open(PAGES, encoding='utf-8'): seen.add(json.loads(l)['url'])

def fetch(url, qid):
    if url in seen: return None
    text, content, links, via, outcome = '', b'', [], 'direct', 'ok'
    if allowed(url):
        try: text, content, links = get_text(url)
        except Exception as e: outcome = 'error: ' + str(e)[:80]
    else: outcome = 'blocked by robots.txt'
    if len(text) < 300:
        w = wayback(url)
        if w and len(w[0]) >= 300: text, content, links, via = w[0], w[1], w[2], 'wayback:' + w[3]; outcome += ' -> wayback ok'
        elif outcome == 'ok': outcome = 'ok (short text)'
    log(qid=qid, url=url, outcome=outcome, via=via)
    if len(text) < 300: return None
    rec = dict(url=url, qid=qid, via=via, ts=datetime.datetime.now().isoformat(), sha256=hashlib.sha256(content).hexdigest(), text=text, links=links)
    open(PAGES,'a',encoding='utf-8').write(json.dumps(rec, ensure_ascii=False) + '\n'); seen.add(url)
    time.sleep(random.uniform(2, 4)); return rec

def search(q, qid, n=8):
    """Merge results of several search backends (stop early when enough)."""
    urls = []
    for be in BACKENDS:
        for attempt in range(2):
            try:
                res = list(DDGS().text(q, max_results=n, backend=be)); urls += [x['href'] for x in res]; break
            except TypeError:
                try: res = list(DDGS().text(q, max_results=n)); urls += [x['href'] for x in res]; break
                except Exception: time.sleep(5)
            except Exception: time.sleep(5 * (attempt + 1))
        if len(set(urls)) >= n: break
    urls = list(dict.fromkeys(urls))
    log(qid=qid, query=q, outcome=f'{len(urls)} results', via='search')
    return urls

def site_search(name, qid):
    found = []
    for dom, tpl in SITE_SEARCH.items():
        u = tpl.format(q=urllib.parse.quote_plus(name))
        if not allowed(u): log(qid=qid, query=u, outcome='site-search blocked by robots', via='site-search'); continue
        try:
            r = requests.get(u, headers=UA, timeout=30); r.raise_for_status()
            ls = good_links(r.text, u); found += ls
            log(qid=qid, query=u, outcome=f'{len(ls)} results', via='site-search')
        except Exception as e: log(qid=qid, query=u, outcome='error: ' + str(e)[:60], via='site-search')
        time.sleep(random.uniform(2, 3))
    return list(dict.fromkeys(found))[:12]
print('helpers ready')

for u in SEEDS: fetch(u, 'seed|' + u)
print('seeds done; pages so far:', len(seen))

def names_of(r): return [r.marez] + ALIASES.get(r.marez, [])
for i, r in cand.iterrows():
    if not left(0.55): print('time budget: candidates stopped'); break
    for nm in names_of(r):
        a, b = int(r.anno_da), int(r.anno_a)
        years = list(range(a, b + 1)); step = max(1, len(years) // YEARS_PER_CAND); years = years[::step][:YEARS_PER_CAND]
        qs = [(f'"{nm}" municipio autónomo zapatista site:{s}', s) for s in SITES] + [
              (f'"{nm}" municipio autónomo zapatista', 'web'), (f'municipio autónomo {nm} EZLN MAREZ', 'web'), (f'MAREZ {nm} Chiapas creación fundación', 'web'),
              (f'MAREZ {nm} Chiapas desaparece disuelve integra', 'web')] + [(f'municipio autónomo {nm} zapatista {y}', f'year{y}') for y in years]
        qid = f'cand|{r.marez}|{r.evento}|'
        for q, s in qs:
            urls = search(q, qid + s); print(r.marez, '|', s, '|', len(urls), flush=True)
            for u in urls: fetch(u, qid + s)
        for u in site_search(nm, qid + 'site-search'): fetch(u, qid + 'site-search')
print('done B+C; pages:', len(seen))

recs = [json.loads(l) for l in open(PAGES, encoding='utf-8')]
todo = []
for rec in recs:
    for u in rec.get('links', []):
        if u not in seen and u not in todo: todo.append(u)
print(len(todo), 'candidate links;', 'budget', MAX_LINKS)
for u in todo[:MAX_LINKS]:
    if not left(0.65): break
    fetch(u, 'crawl|' + u)
print('done D; pages:', len(seen))

def queries_control(name):
    return [(f'{name} Chiapas conflicto agrario organización campesina', 'web'), (f'{name} Chiapas desplazados paramilitares', 'web'),
            (f'{name} Chiapas EZLN zapatistas', 'web'), (f'{name} Chiapas organización campesina OCEZ CIOAC ORCAO', 'web')]
for i, r in ctl.iterrows():
    if not left(0.92): print('time budget: controls stopped'); break
    qid = f'ctl|{r.cve_mun_2020}|{r.municipio}'
    for q, s in queries_control(r.municipio):
        urls = search(q, qid, n=6); print(r.municipio, '|', len(urls), flush=True)
        for u in urls: fetch(u, qid)
    for u in site_search(r.municipio + ' Chiapas', qid)[:6]: fetch(u, qid)
print('done controls; pages:', len(seen), '| minutes:', round((time.time() - T0) / 60))

def norm(s): return ''.join(c for c in unicodedata.normalize('NFKD', s.lower()) if not unicodedata.combining(c))
BIRTH = r'funda|creo\b|crearon|creacion|declar|constitu|nacio|inaugur|se instal|surgi|nuevo municipio'
END   = r'disol|desmantel|desapare|dejo de|se integr|fusion|se separ|extin|suspend|reorganiz|sustitu|reemplaz|se disgreg'
ZAP   = r'zapatist|ezln|marez|junta de buen gobierno|caracol|bases de apoyo'
OTHER = r'orcao|paz y justicia|ocez|\bmira\b|socama|cioac|mocri|cnpa|narco|cartel|cjng|sinaloa|guardia nacional|ejercito|policia|minera|mineria'
MONTHS = r'enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre'
YEAR = r'\b(19[9]\d|20[0-2]\d)\b'
def is_date_name(n): return bool(re.match(r'^\d', n.strip())) or bool(re.search(r'\b(' + MONTHS + r')\b', norm(n)))
def sentences(text): return [s.strip() for s in re.split(r'(?<=[.!?])\s+|\n+', text) if 25 < len(s.strip()) < 900]
def years_in(s): return sorted(set(int(a) for a in re.findall(YEAR, s)))
def url_year(u):
    m = re.search(r'/(19[9]\d|20[0-2]\d)/', u) or re.search(r'[/_-](19[9]\d|20[0-2]\d)[/_-]?', u); return int(m.group(1)) if m else None
def mtype(ns, key):
    for m in re.finditer(re.escape(key), ns):
        pre = ns[max(0, m.start() - 45):m.start()]
        if re.search(r'municipios? autonomos?( rebeldes?)?( zapatistas?)?( de| del)?\W*$|marez\W*(de |del )?\W*$', pre): return 'marez'
        if re.search(r'(comunidad|ejido|poblado|localidad|colonia|rancheria)( zapatista)?( de| del)?\W*$', pre): return 'community'
    return 'other'

def extract(recs):
    out = []
    for rec in recs:
        p = rec['qid'].split('|'); kind = p[0]
        if kind not in ('cand', 'ctl'): kind_name = None
        S = sentences(rec['text']); NS = [norm(s) for s in S]
        if kind == 'cand': names = [p[1]] + ALIASES.get(p[1], []); date_named = is_date_name(p[1])
        elif kind == 'ctl': names = [p[2]]; date_named = False
        else: continue
        for nm in names:
            key = norm(re.sub(r'\(.*?\)', '', nm)).strip()
            for i, ns in enumerate(NS):
                if key not in ns: continue
                mt = mtype(ns, key)
                if date_named and mt != 'marez': continue
                ys = years_in(S[i]); src = 'sentence'
                if not ys: ys = years_in(' '.join(S[max(0, i-1):i+2])); src = 'window+-1'
                if not ys:
                    uy = url_year(rec['url']); ys = [uy] if uy else []; src = 'url-year (publication)'
                if not ys: continue
                out.append(dict(kind=kind, name=p[1] if kind == 'cand' else p[2], matched_as=nm, mention_type=mt, years=';'.join(map(str, ys)), year_source=src,
                    birth_verb=bool(re.search(BIRTH, ns)), end_verb=bool(re.search(END, ns)), zapatista_in_sentence=bool(re.search(ZAP, ns)),
                    other_actors=';'.join(sorted(set(re.findall(OTHER, ns)))), sentence=S[i], url=rec['url'], via=rec.get('via', ''), sha256=rec['sha256'], qid=rec['qid']))
    return out

NAME = r"([A-ZÁÉÍÓÚÑ0-9][\wáéíóúñ°\.]*(?:\s+(?:de|del|la|las|los|y|[A-ZÁÉÍÓÚÑ0-9][\wáéíóúñ°\.]*)){0,3})"
GAZ = re.compile(r'(?i:municipios?\s+aut[oó]nomos?(?:\s+rebeldes?)?(?:\s+zapatistas?)?(?:\s*\(marez\))?(?:\s+(?:de|del))?)\s+["“«]?' + NAME)
STOP = {'Zapatista','Zapatistas','Rebelde','Rebeldes','En','El','La','Los','Las','Y','Chiapas','Autónomo','Autónomos','Cuyo','Que'}
def gazetteer(recs):
    rows = []
    for rec in recs:
        S = sentences(rec['text'])
        for i, s in enumerate(S):
            for m in GAZ.finditer(s):
                nm = m.group(1).strip(' .,;:')
                nm = re.sub(r'(\s+(de|del|la|las|los|y))+\W*$', '', nm)
                if not nm or nm.split()[0] in STOP or len(nm) < 3: continue
                ys = years_in(s) or years_in(' '.join(S[max(0, i-1):i+2])) or ([url_year(rec['url'])] if url_year(rec['url']) else [])
                rows.append(dict(marez_name=nm, years=';'.join(map(str, ys)), birth_verb=bool(re.search(BIRTH, norm(s))), end_verb=bool(re.search(END, norm(s))),
                                 sentence=s, url=rec['url'], via=rec.get('via', '')))
    return rows

recs = [json.loads(l) for l in open(PAGES, encoding='utf-8')]
ex = pd.DataFrame(extract(recs))
# noise filter: for candidates keep only MAREZ/community mentions, or 'other' mentions that also have Zapatista terms + a birth/end verb
if len(ex): ex = ex[(ex.kind != 'cand') | (ex.mention_type != 'other') | (ex.zapatista_in_sentence & (ex.birth_verb | ex.end_verb))]
ex.to_csv(OUT + '/candidate_sentences.csv', index=False, encoding='utf-8-sig')
gz = pd.DataFrame(gazetteer(recs)); gz.to_csv(OUT + '/gazetteer_mentions.csv', index=False, encoding='utf-8-sig')
if len(gz):
    known = {norm(x) for x in cand.marez}
    g = gz.groupby('marez_name').agg(mentions=('url','size'), pages=('url','nunique'), birth_sentences=('birth_verb','sum'), end_sentences=('end_verb','sum')).reset_index()
    g['known_candidate'] = g.marez_name.map(lambda x: norm(x) in known); g = g.sort_values('mentions', ascending=False); g.to_csv(OUT + '/gazetteer_summary.csv', index=False, encoding='utf-8-sig'); display(g.head(40))
print(len(recs), 'pages;', len(ex), 'candidate sentences;', len(gz), 'gazetteer mentions')
ex[ex.kind == 'cand'].head(20)

rows = []
for rec in recs:
    if not rec['qid'].startswith('ctl|'): continue
    _, cve, name = rec['qid'].split('|'); key = norm(name)
    for s in sentences(rec['text']):
        ns = norm(s)
        if key in ns: rows.append(dict(cve_mun_2020=cve, municipality=name, url=rec['url'], zapatista=bool(re.search(ZAP, ns)), other=';'.join(sorted(set(re.findall(OTHER, ns))))))
cov = pd.DataFrame(rows)
if len(cov):
    summ = cov.groupby(['cve_mun_2020','municipality']).agg(pages=('url','nunique'), sentences=('url','size'), zapatista_sentences=('zapatista','sum'), other_actor_sentences=('other', lambda x: (x != '').sum())).reset_index()
    cov.to_csv(OUT + '/control_sentences.csv', index=False, encoding='utf-8-sig'); summ.to_csv(OUT + '/control_coverage.csv', index=False, encoding='utf-8-sig'); display(summ)
import shutil
# slim zip: keep only relevant pages (name found, seed, or MAREZ gazetteer hit); the full cache pages.jsonl stays out of the zip
gaz_urls = set(gz.url) if len(gz) else set()
def relevant(rec):
    p = rec['qid'].split('|'); nt = norm(rec['text'])
    if p[0] == 'seed' or rec['url'] in gaz_urls: return True
    nm = p[1] if p[0] == 'cand' else p[2] if p[0] == 'ctl' else None
    return bool(nm) and norm(re.sub(r'\(.*?\)', '', nm)).strip() in nt
STAGE = OUT + '_zip'; shutil.rmtree(STAGE, ignore_errors=True); os.makedirs(STAGE)
for f in os.listdir(OUT):
    if f != 'pages.jsonl': shutil.copy(OUT + '/' + f, STAGE + '/' + f)
keep = [r for r in recs if relevant(r)]
with open(STAGE + '/pages_relevant.jsonl', 'w', encoding='utf-8') as fh:
    for r in keep: fh.write(json.dumps({k: v for k, v in r.items() if k != 'links'}, ensure_ascii=False) + '\n')
print(len(keep), 'relevant pages of', len(recs))
ZN = f'results_part{PART}' if not TEST_MODE else 'results'
shutil.make_archive(os.path.dirname(OUT) + '/' + ZN, 'zip', STAGE); print('zip ready:', os.path.dirname(OUT) + '/' + ZN + '.zip')
try:
    from google.colab import files; files.download('/content/' + ZN + '.zip')
except Exception: pass