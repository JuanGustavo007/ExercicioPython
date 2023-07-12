#Faça um Programa que leia 4 notas, mostre as notas e a média na tela
notas = []
media = 0
for i in range(4):
    nota = int(input("Digite uma nota: "))
    notas.append(nota)

if len(notas) == 4:
    for i in notas:
        media += i / len(notas)
    print(media)