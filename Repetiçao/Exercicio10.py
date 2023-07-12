# Faça um #Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
# Imprima a idade e a altura na ordem inversa a ordem lida.
idades = []
alturas = []

for i in range(5):
    idade = int(input("Digite a sua idade: "))
    altura = float(input("Digite a sua altura"))
    idades.append(idade)
    alturas.append(altura)

idades.reverse()
alturas.reverse()
print(idades)
print(alturas)
