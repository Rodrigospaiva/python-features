numero_digitado = int(input('Digite um número: '))

arquivo = open('./Teste.txt', "w")
#Parâmetros => ("caminho", "permissão")
# A permissão 'w' reescreve o conteúdo, para adicionar use o 'a'

for i in range(1, numero_digitado):
    arquivo.write(str(i))
    arquivo.flush() #grava após cada iteração.

arquivo.close()

