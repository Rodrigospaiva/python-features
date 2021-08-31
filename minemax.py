def imprime_min_max(lista_numeros):
    maximo = max(lista_numeros)
    minimo = min(lista_numeros)

    print("O número máximo da lista é: " + str(maximo))
    print("O número mínimo da lista é: " + str(minimo))

numeros = [10, 15, 28, 4, 17, 26, 1, 3, 39]

imprime_min_max(numeros)