# GPT-6 Sol & Luna â€” ObservatÃ³rio INEMA

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="48" />
  <p><strong>Arckhé AI</strong></p>
</div>


Pesquisa do lanÃ§amento de 22/09/2026, comparaÃ§Ãµes e planejamento de integraÃ§Ã£o.

**[Abrir guia e simulador](https://inematds.github.io/gpt6-sol-luna/guia/)**

**Idiomas:** [PortuguÃªs](https://inematds.github.io/gpt6-sol-luna/guia/) Â· [English](https://inematds.github.io/gpt6-sol-luna/guia/en/) Â· [EspaÃ±ol](https://inematds.github.io/gpt6-sol-luna/guia/es/)

![Capa GPT-6 Sol e Luna](capa/capa.png)

## Entregas

- AnÃ¡lise em portuguÃªs, inglÃªs e espanhol com 11 referÃªncias oficiais e recomendaÃ§Ãµes INEMA identificadas.
- GrÃ¡fico de preÃ§os e trÃªs avaliaÃ§Ãµes selecionÃ¡veis, com esforÃ§o e metodologia.
- Calculadora de texto: entrada comum, leitura/gravaÃ§Ã£o de cache, contexto longo, modalidade e roteamento/revisÃ£o.
- Gerador local de JSON para Responses; nÃ£o envia requisiÃ§Ãµes.
- Plano para atendimento, busca, bots, conteÃºdo, WebMCP e mÃ­dia.
- Dados editÃ¡veis em `data/research.json` e exportaÃ§Ãµes CSV.

## Executar

```sh
python3 -m http.server 8080
# http://localhost:8080/guia/
node scripts/verify.mjs
```

HTML/CSS/JavaScript sem build ou dependÃªncias de runtime. Fontes Google tÃªm fallback local. Nenhuma chave de API Ã© necessÃ¡ria. O conteÃºdo de `data/research.json` tambÃ©m estÃ¡ embutido no HTML para funcionar sem fetch; o verificador acusa divergÃªncias.

## Limites

Os benchmarks sÃ£o publicados pela OpenAI, nÃ£o reproduzidos neste projeto. O simulador estima custo de tokens; nÃ£o mede qualidade nem latÃªncia, nem inclui ferramentas e mÃ­dia. Exemplos de API foram revisados contra documentaÃ§Ã£o, mas nÃ£o executados com uma chave. Nenhuma integraÃ§Ã£o de produÃ§Ã£o foi ativada.

Capa gerada na ferramenta de imagem embutida do Codex, com pedido de GPT Image 2.5; o retorno e os metadados nÃ£o expÃµem a subversÃ£o. NÃ£o Ã© possÃ­vel certificar 2.5. Prompt e proveniÃªncia em [docs/imagem.md](docs/imagem.md).

VersÃ£o: **1.1.1**. Pesquisa consultada em **2026-09-22**.

## ManutenÃ§Ã£o multilÃ­ngue

Fonte editorial: `i18n/source/pt.html`; textos e traduÃ§Ãµes revisadas em `i18n/source/pt.json` e `i18n/translations/{en,es}.json`. Chaves sÃ£o hashes do texto original; textos novos exigem traduÃ§Ã£o explÃ­cita. NÃ£o editar as pÃ¡ginas geradas diretamente.

```sh
python3 scripts/build-i18n.py
node scripts/verify.mjs
```

O gerador compartilha estrutura, lÃ³gica e imagens. Traduz conteÃºdo, acessibilidade, metadados, notas dos grÃ¡ficos, validaÃ§Ãµes e exemplos. MantÃ©m os IDs de modelos, endpoints, chaves JSON e valores de benchmark. A troca de idioma preserva a seÃ§Ã£o e os campos do simulador na mesma aba. A URL determina o idioma; nÃ£o hÃ¡ redirecionamento automÃ¡tico.

As exportaÃ§Ãµes de dados usam identificadores estÃ¡veis; o README e os documentos tÃ©cnicos do repositÃ³rio permanecem em portuguÃªs. A traduÃ§Ã£o nÃ£o atualiza a pesquisa original de 22/09/2026. Nenhuma API de traduÃ§Ã£o foi chamada: custo de API de traduÃ§Ã£o US$ 0; consumo do agente nÃ£o medido.

---

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="32" />
  <p><strong>Arckhé AI</strong></p>
</div>