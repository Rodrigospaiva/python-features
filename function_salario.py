# Cálculo do salário

horas = float(input("Horas trabalhadas: "))
taxa = float(input("Valor da hora: "))

if horas > 40:
    horas_exc = horas - 40
    taxa_exc = taxa * 1.5
    hora_extra = horas_exc * taxa_exc
    salario = horas * taxa + hora_extra
else:
    salario = horas * taxa

print("O salário será: R$ ", salario)