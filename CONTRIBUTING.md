# Como contribuir

Este repositório reúne exercícios curtos de lógica com Python. Se quiser acrescentar um exercício ou corrigir alguma coisa, o caminho é este.

## Antes de começar

- Olhe as issues abertas para não repetir uma ideia que já está em andamento.
- Código novo de exercício fica na pasta `exercicios`.
- Escreva de um jeito que outra pessoa, ainda no começo, consiga ler e explicar.
- Rode o arquivo com Python antes de abrir o pull request.

## Passo a passo

1. Abra uma issue contando qual exercício você quer adicionar, ou qual problema encontrou.
2. Se o repositório não for seu, faça um fork.
3. Clone o projeto e entre na pasta dele.
4. Atualize a branch `dev` e crie a sua branch a partir dela:

```bash
git checkout dev
git pull origin dev
git checkout -b exercicio/nome-curto
```

5. Crie o arquivo em `exercicios`, com o próximo número da sequência. Exemplo: `08_nome_curto.py`.
6. Coloque valores de exemplo no próprio arquivo, para ele rodar sem pedir dados.
7. Execute e confira a saída:

```bash
python exercicios/08_nome_curto.py
```

8. Faça o commit e abra um pull request para a branch `dev`.
9. Na descrição, cite a issue. Exemplo: `Fecha #12`.
10. Quando a `dev` estiver revisada, as mudanças seguem para a `main` por outro pull request.

## O que cabe neste projeto

- Um assunto por arquivo: variáveis, condicionais, repetições, listas ou funções.
- Mensagens de `print` em português, simples e diretas.
- Nomes de variáveis que digam o que guardam (`nota_1`, `compras`, `media`).
- Um comentário curto no topo dizendo o que o exercício pratica e o que a pessoa pode trocar.

## O que fica de fora

- Código copiado de outro repositório.
- Arquivos gerados pelo Python, como `__pycache__/` e `.pyc`. O `.gitignore` já cuida disso.
- Dependências externas. Os exercícios usam só o que já vem com o Python.

## Mensagem de commit

Uma frase curta, em português, dizendo o que entrou.

Exemplos:

- `Adiciona exercício de média ponderada`
- `Corrige a divisão por zero no exercício de funções`

## Pull request

Conte o que mudou e como você testou. O modelo em `.github/pull_request_template.md` já traz esses campos.
