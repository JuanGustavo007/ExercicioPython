# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
# Valide a entrada e permita repetir a operação.


paisA = int(input("Por favor digite um valor para Pais A:  "))
paisB = int(input("Por favor digite um valor para Pais B: "))


while paisA < paisB and (paisA > 0 and paisB > 0):
    print(paisA)
    paisA += paisA * 0.03
    paisB += paisB * 0.015

if paisA > paisB:
    print("Maior")
    print(paisA)

