def operacoes(num_1, num_2):
    soma = round((num_1 + num_2),2)
    subtracao = round((num_1 - num_2),2)
    multiplicacao = round((num_1 * num_2),2)
    divisao =round((num_1 / num_2),2)

    print("Soma: " + str(soma))
    print("Subtração: " + str(subtracao))
    print("Multiplicação: " + str(multiplicacao))
    print("Divisão: " + str(divisao))

numero_1 = int(input("Informe o primeiro número: "))
numero_2 = int(input("Informe o segundo número: "))

operacoes(numero_1, numero_2)