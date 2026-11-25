# Exercício 4 — repetição
# Mostra a tabuada do 1 ao 10. Troque a variável numero para ver outra.

numero = 7

print("Tabuada do", numero)

for multiplicador in range(1, 11):
    resultado = numero * multiplicador
    print(numero, "x", multiplicador, "=", resultado)
