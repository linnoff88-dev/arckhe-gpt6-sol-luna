#!/usr/bin/env python3
"""Build all static guide locales from one PT template and reviewed text catalogs."""
from pathlib import Path
import copy, html, json, re
ROOT=Path(__file__).resolve().parents[1]
BASE='https://linnoff88-dev.github.io/
SOURCE=json.loads((ROOT/'i18n/source/pt.json').read_text())
DATA=json.loads((ROOT/'data/research.json').read_text())
TEMPLATE=(ROOT/'i18n/source/pt.html').read_text()
ROUTES={'pt':'','en':'en/','es':'es/'}
LOCALES={'pt':'pt-BR','en':'en-US','es':'es-ES'}

def render(lang):
    targets=SOURCE if lang=='pt' else json.loads((ROOT/f'i18n/translations/{lang}.json').read_text())
    assert targets.keys()==SOURCE.keys(),f'{lang}: translation keys differ'
    assert all(isinstance(v,str) and v.strip() for v in targets.values()),f'{lang}: empty translations'
    translations={SOURCE[k]:targets[k] for k in SOURCE}
    def translate(value):
        if value not in translations: raise ValueError(f'Missing {lang} translation: {value}')
        return translations[value]
    def text_node(raw):
        value=html.unescape(raw.strip())
        if not value:return raw
        out=translate(value)
        if re.fullmatch(r'US\$ [\d.]+',out) and lang!='en':out=out.replace('.',',')
        return raw[:len(raw)-len(raw.lstrip())]+html.escape(out,quote=False)+raw[len(raw.rstrip()):]
    data=copy.deepcopy(DATA)
    for source in data['sources']:source['title']=translate(source['title'])
    for bench in data['benchmarks']:
        for field in ['metric','note']:bench[field]=translate(bench[field])
    chunks=re.split(r'(<script\b[^>]*>.*?</script>|<style\b[^>]*>.*?</style>|<[^>]+>)',TEMPLATE,flags=re.S)
    for i,chunk in enumerate(chunks):
        if chunk.startswith('<style'):continue
        if chunk.startswith('<script'):
            chunk=re.sub(r'const DATA=[^\n]+;',lambda _: 'const DATA='+json.dumps(data,ensure_ascii=False)+';',chunk,count=1)
            # Only replace display strings, preserving keys, IDs, URLs and executable logic.
            chunk=re.sub(r"'([^'\\]*(?:\\.[^'\\]*)*)'",lambda m:json.dumps(translations[m[1]],ensure_ascii=False) if m[1] in translations else m[0],chunk)
            for value in ['Estimativa mensal. ',' Diferença do cenário misto frente a só Sol: ','. Não inclui ferramentas.']:
                chunk=chunk.replace(value,translate(value))
            chunk=chunk.replace("'pt-BR'",repr(LOCALES[lang]))
            chunk=chunk.replace("'campo,valor\\n'", "'field,value\\n'") # stable machine-readable CSV schema
            chunks[i]=chunk;continue
        if chunk.startswith('<'):
            chunk=re.sub(r'(content|aria-label|alt)="([^"]*)"',lambda m:m[1]+'="'+html.escape(translations.get(html.unescape(m[2]),html.unescape(m[2])),quote=True)+'"',chunk)
            chunks[i]=chunk
        else:chunks[i]=text_node(chunk) if chunk.strip() not in ['__LANGUAGE_LINKS__','__LANGUAGE_META__'] else chunk
    result=''.join(chunks)
    prefix='../' if lang!='pt' else ''
    links=[]
    for target,route in ROUTES.items():
        href=prefix+route if prefix+route else './'
        links.append(f'<a data-language="{target}" href="{href}" hreflang="{LOCALES[target]}" lang="{LOCALES[target]}"'+(' aria-current="page"' if lang==target else '')+'>'+target.upper()+'</a>')
    meta=''.join(f'<link rel="alternate" hreflang="{LOCALES[k]}" href="{BASE+v}">' for k,v in ROUTES.items())
    meta+=f'<link rel="alternate" hreflang="x-default" href="{BASE}"><meta property="og:locale" content="{LOCALES[lang].replace("-","_")}"><meta property="og:url" content="{BASE+ROUTES[lang]}">'
    result=result.replace('__LANGUAGE_LINKS__',''.join(links)).replace('__LANGUAGE_META__',meta)
    result=result.replace('<html lang="pt-BR">',f'<html lang="{LOCALES[lang]}">')
    result=result.replace(f'rel="canonical" href="{BASE}"',f'rel="canonical" href="{BASE+ROUTES[lang]}"')
    if lang!='pt':result=result.replace('src="assets/','src="../assets/').replace('href="../data/','href="../../data/')
    output=ROOT/'guia'/ROUTES[lang]/'index.html';output.parent.mkdir(parents=True,exist_ok=True);output.write_text(result)
    print(f'{lang}: {output.relative_to(ROOT)} ({len(result.encode())} bytes)')

if __name__=='__main__':
    for lang in ROUTES:render(lang)
    sitemap='<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{BASE+route}</loc></url>' for route in ROUTES.values())+'</urlset>\n'
    (ROOT/'sitemap.xml').write_text(sitemap)
