"""
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
"""

nota1 = float(input("Digite a primeira nota do aluno:  "))
nota2 = float(input("Digite a segunda nota do aluno: "))
if ((nota1 + nota2) / 2.00) >= 7.00:
    print(((nota1 + nota2) / 2.00))
    print("Aluno aprovado")
else:
    print("Aluno reprovado")
