# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
numeros = [1, 2, 3, 4, 5]
soma = 0

for i in numeros:
    soma += i
    mult = i * i
    if i == 5:
        media = soma / len(numeros)
        print(f"Média {media}")
