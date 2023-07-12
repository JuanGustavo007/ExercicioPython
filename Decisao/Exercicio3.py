#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

texto = str(input("Digite [M] para Masculino ou [F] para feminino"))
print(type(texto))
if texto.upper() == "M":
    print("Masculino")
elif texto.upper() == "F":
    print("Feminino")
else:
    print("Sexo invalido")

