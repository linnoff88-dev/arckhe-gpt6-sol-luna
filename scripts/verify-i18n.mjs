import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';
import assert from 'node:assert/strict';
const root=path.resolve(import.meta.dirname,'..');
const read=p=>fs.readFileSync(path.join(root,p),'utf8');
const source=JSON.parse(read('i18n/source/pt.json'));
const data=JSON.parse(read('data/research.json'));
const base='https://linnoff88-dev.github.io/arckhe-/guia/';
let originalEstimate;
for(const [lang,route,locale] of [['pt','','pt-BR'],['en','en/','en-US'],['es','es/','es-ES']]){
 const html=read(`guia/${route}index.html`);
 const script=html.match(/<script>([\s\S]*?)<\/script>/)[1];
 new vm.Script(script);
 assert(html.includes(`<html lang="${locale}">`));
 assert(html.includes(`rel="canonical" href="${base+route}"`));
 assert.equal((html.match(/data-language=/g)||[]).length,3);
 assert.equal((html.match(/rel="alternate"/g)||[]).length,4);
 assert.equal((html.match(/<a\b[^>]*aria-current="page"/g)||[]).length,1);
 assert(!/__LANGUAGE_|\{\{[A-Z_]+\}\}/.test(html));
 const localized=JSON.parse(script.match(/const DATA=([^\n]+);/)[1]);
 assert.deepEqual(localized.models,data.models);
 assert.deepEqual(localized.previous,data.previous);
 assert.equal(localized.version,data.version);
 assert.deepEqual(localized.sources.map(s=>[s.id,s.url]),data.sources.map(s=>[s.id,s.url]));
 assert.deepEqual(localized.benchmarks.map(b=>[b.id,b.title,b.rows,b.source]),data.benchmarks.map(b=>[b.id,b.title,b.rows,b.source]));
 const estimate=script.match(/function estimate\(m,s\)\{[^\n]+/)[0];
 if(!originalEstimate)originalEstimate=estimate;
 assert.equal(estimate,originalEstimate,'Cost logic changed by locale');
 const ids=[...html.matchAll(/\bid="([^"]+)"/g)].map(m=>m[1]);
 assert.equal(ids.length,new Set(ids).size);
 for(const [,url] of html.matchAll(/(?:href|src)="([^"]+)"/g)){
  if(/^https?:/.test(url))continue;
  if(url.startsWith('#')){assert(ids.includes(url.slice(1)));continue}
  let target=path.resolve(root,'guia',route,url);if(url.endsWith('/'))target=path.join(target,'index.html');
  assert(fs.existsSync(target),`${lang}: broken local link ${url}`);
 }
 if(lang!=='pt'){
  const translations=JSON.parse(read(`i18n/translations/${lang}.json`));
  assert.deepEqual(Object.keys(translations).sort(),Object.keys(source).sort());
  assert(Object.values(translations).every(v=>typeof v==='string'&&v.trim()));
 }
}
console.log('PASS i18n: 3 locales, complete catalogs, metadata, routes/assets, identical benchmark numbers and cost logic.');
