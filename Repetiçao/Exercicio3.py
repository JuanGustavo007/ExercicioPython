"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""

nome = str(input("Digite um nome: "))
idade = int(input("Digite uma idade: "))
salario = float(input("Digite um sálario: "))
sexo = str(input("Digite [f] - Feminino ou [M] - Masculino"))
estadoCivil = str(input("Digite o seu estado civil [s]- Solteiro [c] - Casado [v] - viuvo [d] - divorciado"))


if len(nome) > 3:
    print("Nome valido")
else:
    print("Nome invalido")

if idade in range(0, 150):
    print("Idade válida")
else:
    print("Idade invalida")

if salario > 0:
    print("Salario valido")
else:
    print("Salario invalido")

if sexo.lower() == "f" or sexo.lower() =="m" :
    print("Sexo valido")
else:
    print("Sexo invalido")

if estadoCivil.lower() == 's' or estadoCivil.lower() == 'c' or estadoCivil.lower() == 'v' or estadoCivil.lower() == 'd':
    print("Estado civil válido")
else:
    print("Sexo invalido")
