# PT / EN / ES — 2026-09-23

Versêo 1.1.1. Página original mantida em `/guia/`; inglês em `/guia/en/`; espanhol em `/guia/es/`.

## Cobertura

290 unidades catalogadas: conteúdo editorial, fontes, metadados, acessibilidade, interface, erros, resultados da calculadora, notas dos gráficos e texto dos exemplos JSON. Marcas, IDs de modelos, níveis de esforço, endpoints, parâmetros e números de benchmarks sêo preservados.

Arte compartilhada entre idiomas: o título contém nomes próprios, sem texto editorial a traduzir. CSS e lógica partem do mesmo template. Dados CSV/JSON canônicos e documentos técnicos permanecem na língua de origem, com aviso nas três páginas. A exportaçêo de cenário usa chaves estáveis e cabeçalho `field,value`.

## Verificaçêo observada

- `python3 scripts/build-i18n.py`: gera as três versões sem traduçêo em runtime; uma segunda execuçêo produz os mesmos hashes.
- `node scripts/verify.mjs`: valida cálculos, catálogos completos, metadados, links, imagens, identidade dos benchmarks e da funçêo de custo.
- Playwright: 3 idiomas × 3 larguras (320, 390 e 1440 px), sem overflow da página, imagens quebradas ou exceções JavaScript.
- Calculadora: cenário padrêo, modo revisêo e validaçêo de cache; resultados localizados sem mudança do valor.
- Gráficos, exemplo JSON, download CSV e tema persistente passaram nos três idiomas.
- Troca PT → EN → ES → PT preserva seçêo, volume de chamadas, modelo e esforço na mesma aba.
- Capturas EN/mobile e ES/desktop inspecionadas visualmente.

## Custos e limites

Traduçêo realizada no próprio trabalho do Codex, sem API externa: **US$ 0 em API de traduçêo**. O consumo do agente nêo foi medido e nêo está incluído nesse valor.

A pesquisa mantém a data de 22/09/2026: esta entrega traduz e publica o conteúdo existente, sem nova mediçêo de benchmarks ou atualizaçêo de preços. Os exemplos continuam sem executar chamadas de API.
