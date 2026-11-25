# Lógica de Programação com Python

Repositório criado para reunir exercícios de lógica de programação desenvolvidos durante meus estudos na DIO.

## Sobre o projeto

O objetivo é praticar os fundamentos da programação com Python. Cada arquivo da pasta `exercicios` trata de um assunto e já traz valores de exemplo, então dá para executar e ver o resultado na hora.

Os exercícios foram escritos para este repositório. O material da formação entra aqui como referência de estudo.

## O que estes exercícios praticam

| Assunto | Onde aparece |
| --- | --- |
| Variáveis e operadores | `exercicios/01_operacoes.py` |
| Condicionais | `exercicios/02_par_impar.py` e `exercicios/05_comparacao.py` |
| Média e decisão | `exercicios/03_media_notas.py` |
| Repetições | `exercicios/04_tabuada.py` |
| Listas | `exercicios/06_listas.py` |
| Funções | `exercicios/07_funcoes.py` |

## Estrutura

```text
.
├── exercicios/
│   ├── 01_operacoes.py
│   ├── 02_par_impar.py
│   ├── 03_media_notas.py
│   ├── 04_tabuada.py
│   ├── 05_comparacao.py
│   ├── 06_listas.py
│   └── 07_funcoes.py
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── config.yml
│   │   ├── novo-exercicio.md
│   │   └── problema.md
│   └── pull_request_template.md
├── .gitignore
├── CONTRIBUTING.md
└── README.md
```

## Exercícios

| Arquivo | Assunto | O que o script faz |
| --- | --- | --- |
| `01_operacoes.py` | Variáveis | Soma, subtrai, multiplica e divide dois números |
| `02_par_impar.py` | Condicionais | Diz se o número é par ou ímpar |
| `03_media_notas.py` | Variáveis e condicional | Calcula a média de três notas e informa a situação |
| `04_tabuada.py` | Repetição | Mostra a tabuada de um número, do 1 ao 10 |
| `05_comparacao.py` | Condicionais | Compara dois números |
| `06_listas.py` | Listas | Monta uma lista de compras e acha o maior número de outra lista |
| `07_funcoes.py` | Funções | Reúne as ideias anteriores em funções reutilizáveis |

## Como executar

É preciso ter o Python 3 instalado. No terminal, na pasta do projeto:

```bash
python exercicios/01_operacoes.py
```

Para ver outro exercício, troque o nome do arquivo. Para testar outros números, abra o arquivo e mude os valores de exemplo.

## Exemplo

Trecho de `exercicios/05_comparacao.py`:

```python
if primeiro > segundo:
    print(primeiro, "é maior")
elif segundo > primeiro:
    print(segundo, "é maior")
else:
    print("Os dois números são iguais")
```

Com `primeiro = 15` e `segundo = 22`, o programa informa que 22 é maior.

## Fluxo no GitHub

- A branch `main` guarda a versão estável.
- A branch `dev` recebe o trabalho novo.
- Uma issue descreve a ideia ou a correção.
- Um pull request leva a mudança para revisão antes do merge.

O passo a passo para contribuir está no [CONTRIBUTING.md](CONTRIBUTING.md).

## Tecnologias utilizadas

- Python
- Git
- GitHub

## Referência

Projeto desenvolvido como parte dos estudos na DIO, utilizando como material de referência o repositório [estudos-logica-com-python](https://github.com/alinealien/estudos-logica-com-python), de alinealien.
