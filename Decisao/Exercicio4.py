#Faça um Programa que verifique se uma letra digitada é vogal ou consoante

vogalDigitada = str(input("Digite um valor "))
vogais = ["a", "e", "i", "o",  "u"]
consoantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", 'p', "q", "r", "s", "t", "v", "x", "y", "w", "z"]

if vogais.__contains__(vogalDigitada):
    print("É uma vogal")
else:
    print("É uma consoante")
