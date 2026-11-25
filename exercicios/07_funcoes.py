# Exercício 7 — funções
# As ideias dos exercícios anteriores, agora em funções que devolvem um resultado.


def dividir(a, b):
    if b == 0:
        return None
    return a / b


def par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    return "ímpar"


def calcular_media(notas):
    if len(notas) == 0:
        return None

    soma = 0
    for nota in notas:
        soma = soma + nota

    return soma / len(notas)


def situacao(media):
    if media >= 7:
        return "aprovado"
    return "em recuperação"


def tabuada(numero):
    linhas = []
    for multiplicador in range(1, 11):
        resultado = numero * multiplicador
        linha = str(numero) + " x " + str(multiplicador) + " = " + str(resultado)
        linhas.append(linha)
    return linhas


def comparar(primeiro, segundo):
    if primeiro > segundo:
        return "o primeiro é maior"
    if segundo > primeiro:
        return "o segundo é maior"
    return "os números são iguais"


def maior_numero(numeros):
    if len(numeros) == 0:
        return None

    maior = numeros[0]
    for numero in numeros:
        if numero > maior:
            maior = numero
    return maior


print("--- Divisão ---")
print("10 / 2 =", dividir(10, 2))

divisao_zero = dividir(10, 0)
if divisao_zero is None:
    print("10 / 0 = não dá para dividir por zero")
else:
    print("10 / 0 =", divisao_zero)

print("--- Par ou ímpar ---")
for numero in [10, 17]:
    print(numero, "é", par_ou_impar(numero))

print("--- Média ---")
notas_altas = [8, 7, 6]
media_alta = calcular_media(notas_altas)
print("Notas:", notas_altas)
print("Média:", media_alta)
print("Situação:", situacao(media_alta))

notas_baixas = [5, 6, 4]
media_baixa = calcular_media(notas_baixas)
print("Notas:", notas_baixas)
print("Média:", media_baixa)
print("Situação:", situacao(media_baixa))

media_vazia = calcular_media([])
if media_vazia is None:
    print("Lista vazia: sem notas para calcular")
else:
    print("Lista vazia:", media_vazia)

print("--- Tabuada do 3 ---")
for linha in tabuada(3):
    print(linha)

print("--- Comparação ---")
print("15 e 22:", comparar(15, 22))
print("8 e 8:", comparar(8, 8))
print("10 e 3:", comparar(10, 3))

print("--- Maior número ---")
print("Maior de [4, 9, 2, 15, 7]:", maior_numero([4, 9, 2, 15, 7]))

lista_vazia = maior_numero([])
if lista_vazia is None:
    print("Maior de uma lista vazia: não há números")
else:
    print("Maior de uma lista vazia:", lista_vazia)
