# Faça um Programa que peça as quatro notas de 10 alunos,
# calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0

medias = []
for i in range(10):
    nota_aluno_1 = float(input("Digite uma nota: "))
    nota_aluno_2 = float(input("Digite a segunda nota: "))
    nota_aluno_3 = float(input("Digite a terceira nota:  "))
    nota_aluno_4 = float(input("Digite a quarta nota:  "))
    media = (nota_aluno_1 + nota_aluno_2 + nota_aluno_3 + nota_aluno_4) / 4
    medias.append(media)

for i in medias:
    if i > 7:
        print(i)