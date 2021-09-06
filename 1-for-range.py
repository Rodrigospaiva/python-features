numero_digitado = int(input('Digite um número: '))

for  x in range(1, numero_digitado+1):

    if (x % numero_digitado) == 0:



        print('Os seguintes números são primos.', x)