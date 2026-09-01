# -*- coding: utf-8 -*-
"""Gera as páginas do GitHub Pages a partir dos documentos de `docs/legal/`.

    python docs/legal/site/gerar.py

Por que um gerador e não HTML escrito à mão: os documentos MUDAM (a seção 6 da
política já tem data marcada para mudar, no dia em que o Supabase sair do plano
Free). Com duas cópias — uma no repositório e outra no site — a segunda vira
mentira na primeira distração. Aqui existe uma fonte só, e o site é derivado.

O que ele faz, e só isso:

1. tira TODO bloco de citação (`> ...`) — no `docs/legal/` eles são recados
   internos para o Rogerio ("falta preencher", "recomendação: 16 anos"), nunca
   texto para o usuário;
2. põe o front matter que o Jekyll do GitHub Pages exige — sem ele o arquivo
   `.md` é copiado cru e NÃO vira `.html`, que é o erro mais chato de descobrir
   porque a página simplesmente não existe;
3. grava com o nome que o app espera. 🔴 Os nomes abaixo são os mesmos de
   `lib/core/constants/legal_links.dart` — mudar um lado sem o outro deixa o
   botão do app abrindo 404.
"""

import io
import os
import re

AQUI = os.path.dirname(os.path.abspath(__file__))
FONTE = os.path.dirname(AQUI)  # docs/legal

# (arquivo de origem, arquivo do site, título da aba, descrição)
PAGINAS = [
    ('politica_de_privacidade.md', 'privacidade.md', 'Política de Privacidade',
     'Como o Zenith coleta, usa e protege os seus dados.'),
    ('termos_de_uso.md', 'termos.md', 'Termos de Uso',
     'As regras de uso do aplicativo Zenith.'),
    ('exclusao_de_conta.md', 'excluir-conta.md', 'Excluir sua conta',
     'Como apagar sua conta do Zenith e todos os seus dados.'),
]


def limpar(texto):
    """Tira os blocos de citação e as linhas em branco que sobram deles."""
    linhas = [ln for ln in texto.split('\n') if not ln.lstrip().startswith('>')]
    saida = '\n'.join(linhas)
    saida = re.sub(r'\n{3,}', '\n\n', saida)
    # Um `---` logo depois de outro, ou no fim, é separador órfão de bloco
    # removido.
    saida = re.sub(r'\n---\n\n---\n', '\n---\n', saida)
    return saida.strip() + '\n'


def main():
    for origem, destino, titulo, descricao in PAGINAS:
        caminho = os.path.join(FONTE, origem)
        with io.open(caminho, encoding='utf-8') as f:
            corpo = limpar(f.read())

        frente = (
            '---\n'
            'layout: default\n'
            'title: "%s"\n'
            'description: "%s"\n'
            '---\n\n' % (titulo, descricao)
        )
        alvo = os.path.join(AQUI, destino)
        with io.open(alvo, 'w', encoding='utf-8') as f:
            f.write(frente + corpo)
        print('escrito: %s' % destino)


if __name__ == '__main__':
    main()
