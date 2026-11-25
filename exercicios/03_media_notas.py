# Exercício 3 — média de três notas
# Média igual ou maior que 7: aprovado.
# Abaixo de 7: em recuperação.

nota_1 = 8
nota_2 = 7
nota_3 = 9

quantidade = 3
soma = nota_1 + nota_2 + nota_3
media = soma / quantidade

print("Notas:", nota_1, nota_2, nota_3)
print("Soma:", soma)
print("Média:", media)

if media >= 7:
    print("Situação: aprovado")
else:
    print("Situação: em recuperação")
