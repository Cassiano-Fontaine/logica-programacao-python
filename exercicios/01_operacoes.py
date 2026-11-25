# Exercício 1 — variáveis e operações matemáticas
# Troque numero_a e numero_b e execute o arquivo de novo.

numero_a = 13
numero_b = 4

soma = numero_a + numero_b
subtracao = numero_a - numero_b
multiplicacao = numero_a * numero_b

print("Número A:", numero_a)
print("Número B:", numero_b)
print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)

if numero_b == 0:
    print("Divisão: não dá para dividir por zero")
else:
    divisao = numero_a / numero_b
    divisao_inteira = numero_a // numero_b
    resto = numero_a % numero_b
    print("Divisão:", divisao)
    print("Divisão inteira:", divisao_inteira)
    print("Resto:", resto)
