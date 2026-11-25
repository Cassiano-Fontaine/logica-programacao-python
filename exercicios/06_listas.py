# Exercício 6 — listas
# A primeira lista é de compras. A segunda é de números.

compras = ["arroz", "feijão", "leite"]
print("Lista inicial:", compras)

compras.append("pão")
print("Depois de adicionar pão:", compras)
print("Quantidade de itens:", len(compras))
print("Primeiro item:", compras[0])
print("Último item:", compras[-1])

print("Itens da lista:")
for item in compras:
    print("-", item)

numeros = [4, 9, 2, 15, 7]
maior = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero

print("Números:", numeros)
print("Maior número:", maior)
