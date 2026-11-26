# GPT-6 Sol & Luna ê¢â¬â ObservatêÂ³rio ARCKHê

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="48" />
  <p><strong>Arckhé AI</strong></p>
</div>


Pesquisa do lanêÂ§amento de 22/09/2026, comparaêÂ§êÂµes e planejamento de integraêÂ§êÂ£o.

**[Abrir guia e simulador](https://linnoff88-dev.github.io/

**Idiomas:** [PortuguêÂªs](https://linnoff88-dev.github.io/ êÂ· [English](https://linnoff88-dev.github.io/ êÂ· [EspaêÂ±ol](https://linnoff88-dev.github.io/

![Capa GPT-6 Sol e Luna](capa/capa.png)

## Entregas

- AnêÂ¡lise em portuguêÂªs, inglêÂªs e espanhol com 11 referêÂªncias oficiais e recomendaêÂ§êÂµes ARCKHê identificadas.
- GrêÂ¡fico de preêÂ§os e trêÂªs avaliaêÂ§êÂµes selecionêÂ¡veis, com esforêÂ§o e metodologia.
- Calculadora de texto: entrada comum, leitura/gravaêÂ§êÂ£o de cache, contexto longo, modalidade e roteamento/revisêÂ£o.
- Gerador local de JSON para Responses; nêÂ£o envia requisiêÂ§êÂµes.
- Plano para atendimento, busca, bots, conteêÂºdo, WebMCP e mêÂ­dia.
- Dados editêÂ¡veis em `data/research.json` e exportaêÂ§êÂµes CSV.

## Executar

```sh
python3 -m http.server 8080
# http://localhost:8080/guia/
node scripts/verify.mjs
```

HTML/CSS/JavaScript sem build ou dependêÂªncias de runtime. Fontes Google têÂªm fallback local. Nenhuma chave de API êÂ© necessêÂ¡ria. O conteêÂºdo de `data/research.json` tambêÂ©m estêÂ¡ embutido no HTML para funcionar sem fetch; o verificador acusa divergêÂªncias.

## Limites

Os benchmarks sêÂ£o publicados pela OpenAI, nêÂ£o reproduzidos neste projeto. O simulador estima custo de tokens; nêÂ£o mede qualidade nem latêÂªncia, nem inclui ferramentas e mêÂ­dia. Exemplos de API foram revisados contra documentaêÂ§êÂ£o, mas nêÂ£o executados com uma chave. Nenhuma integraêÂ§êÂ£o de produêÂ§êÂ£o foi ativada.

Capa gerada na ferramenta de imagem embutida do Codex, com pedido de GPT Image 2.5; o retorno e os metadados nêÂ£o expêÂµem a subversêÂ£o. NêÂ£o êÂ© possêÂ­vel certificar 2.5. Prompt e proveniêÂªncia em [docs/imagem.md](docs/imagem.md).

VersêÂ£o: **1.1.1**. Pesquisa consultada em **2026-09-22**.

## ManutenêÂ§êÂ£o multilêÂ­ngue

Fonte editorial: `i18n/source/pt.html`; textos e traduêÂ§êÂµes revisadas em `i18n/source/pt.json` e `i18n/translations/{en,es}.json`. Chaves sêÂ£o hashes do texto original; textos novos exigem traduêÂ§êÂ£o explêÂ­cita. NêÂ£o editar as pêÂ¡ginas geradas diretamente.

```sh
python3 scripts/build-i18n.py
node scripts/verify.mjs
```

O gerador compartilha estrutura, lêÂ³gica e imagens. Traduz conteêÂºdo, acessibilidade, metadados, notas dos grêÂ¡ficos, validaêÂ§êÂµes e exemplos. MantêÂ©m os IDs de modelos, endpoints, chaves JSON e valores de benchmark. A troca de idioma preserva a seêÂ§êÂ£o e os campos do simulador na mesma aba. A URL determina o idioma; nêÂ£o hêÂ¡ redirecionamento automêÂ¡tico.

As exportaêÂ§êÂµes de dados usam identificadores estêÂ¡veis; o README e os documentos têÂ©cnicos do repositêÂ³rio permanecem em portuguêÂªs. A traduêÂ§êÂ£o nêÂ£o atualiza a pesquisa original de 22/09/2026. Nenhuma API de traduêÂ§êÂ£o foi chamada: custo de API de traduêÂ§êÂ£o US$ 0; consumo do agente nêÂ£o medido.

---

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="32" />
  <p><strong>Arckhé AI</strong></p>
</div>