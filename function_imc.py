def calculo_imc(peso, altura):
    return round((float(peso) / float(altura)**2), 2)

altura = input("Digite sua altura: ")
peso = input("Digite seu peso: ")

print("O IMC é: ", calculo_imc(peso, altura))
