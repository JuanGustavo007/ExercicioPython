"""
Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
"""
valoresPares = []
valoresImpares = []
for i in range(20):
    nome = int(input("Digite um valor: "))
    if i % 2 == 0 :
        valoresPares.append(i)
    else:
        valoresImpares.append(i)

for i in valoresPares:
    print(f"Valor par {i}")

for i in valoresImpares:
    print(f"Valor impar {i}")