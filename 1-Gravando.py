import math

arquivo = open("./math-teste.txt", 'w')

for x in range(1, 10):
    arquivo.write( str(x) + '\televado á 2\t=\t' + str(pow(x, 2))+'\n' )

arquivo.close()