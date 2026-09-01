# `docs/legal/site` — as páginas públicas, prontas para o GitHub Pages

Escrito em 31/08/2026. O que está nesta pasta é o **site inteiro**: copiar o
conteúdo dela para a raiz de um repositório público e ligar o Pages já publica
as três páginas.

> ⚠️ **Não ligue o Pages no repositório do Zenith.** O código é privado, e
> GitHub Pages em repositório privado exige plano pago. Um repositório separado
> e público, só com estes arquivos, resolve e não expõe o código.

## O que tem aqui

| arquivo | o que é |
|---|---|
| `index.md` | a capa, com link para as três |
| `privacidade.md` | 🤖 **gerado** — não editar à mão |
| `termos.md` | 🤖 **gerado** — não editar à mão |
| `excluir-conta.md` | 🤖 **gerado** — não editar à mão |
| `_layouts/default.html` | o visual (fundo escuro e roxo do app), com o CSS dentro |
| `_config.yml` | o mínimo que o Jekyll do GitHub Pages precisa |
| `gerar.py` | refaz os três `.md` gerados a partir de `docs/legal/` |

🔴 **Os três marcados como gerados saem de `docs/legal/`.** Editar um deles aqui
é criar uma segunda versão do documento, e a próxima rodada de `gerar.py` apaga
a edição sem avisar. Mexeu no texto? Mexe em `docs/legal/` e roda:

```
python docs/legal/site/gerar.py
```

## Por que `.md` e não `.html`

O GitHub Pages roda Jekyll, que converte todo arquivo `.md` **que tenha front
matter** (o bloco entre `---` no topo) num `.html` de mesmo nome. Então
`privacidade.md` vira `privacidade.html`, que é exatamente o endereço que o app
abre.

⚠️ **Sem o front matter o arquivo é copiado cru e a página não existe.** É a
falha mais chata de diagnosticar, porque não aparece erro em lugar nenhum — só
um 404. O `gerar.py` põe o front matter; escrever um arquivo novo à mão exige
lembrar disso.

## Os endereços

Depois de ligar o Pages, as páginas ficam em:

```
https://<usuario>.github.io/<repositorio>/
https://<usuario>.github.io/<repositorio>/privacidade.html
https://<usuario>.github.io/<repositorio>/termos.html
https://<usuario>.github.io/<repositorio>/excluir-conta.html
```

🔴 **Esses três endereços aparecem em quatro lugares, e têm que ser iguais nos
quatro:**

1. `lib/core/constants/legal_links.dart` — é o que o app abre na tela *Sobre*;
2. a ficha do app no **Play Console** (política de privacidade);
3. a **tela de consentimento do Google Cloud** (a mesma do Google Sign-In);
4. o formulário de **Segurança dos dados** do Play Console (exclusão de conta).

O teste `test/links_legais_test.dart` cuida do primeiro. Os outros três são na
mão — e é por isso que estão listados aqui.
