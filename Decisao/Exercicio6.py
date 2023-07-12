#Faça um Programa que leia três números e mostre o maior deles.
numero1 = int(input("Digite o primeiro valor: "))
numero2 = int(input("Digite o segundo valor: "))
numero3 = int(input("Digite o terceiro valor: "))


if numero1 > numero2 and numero1 > numero3:
    print(f"{numero1} é o maior valor")
elif numero2 > numero3 and numero2 >numero1:
    print(f"{numero2} é o maior valor")
elif numero3 > numero2 and numero3 > numero1:
    print(f"{numero3} é o maior valor")
else:
    print("Valores iguais")