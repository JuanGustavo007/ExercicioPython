"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações.
"""
nameUser = str(input("Digite um nome: "))
passwordUser = str(input("Digite sua senha: "))

while nameUser == passwordUser:
    print("Nome de usuário e senha são iguais, por favor os diferencie")
    nameUser = str(input("Digite um nome: "))
    passwordUser = str(input("Digite sua senha: "))
