#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
entrada = str(input("Digite um texto: "))
vogais = ["a", "e", "i", "o",  "u"]
consoantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", 'p', "q", "r", "s", "t", "v", "x", "y", "w", "z"]
quantasVogais = []
quantasConsoantes = []

for i in entrada:
    if i in vogais:
        quantasVogais.append(i)
    elif i in consoantes:
        quantasConsoantes.append(i)

print(len(quantasVogais))
print(len(quantasConsoantes))