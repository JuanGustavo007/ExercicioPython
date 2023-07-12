"""
Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
"""
nota = float(input("Digite um valor: "))
notasPossiveis= [1,2,3,4,5,6,7,8,9,10]

while nota not in notasPossiveis:
    print("Valor invalido")
    nota = float(input("Digite um valor: "))

