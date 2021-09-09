conjunto1 = { 1, 2, 3, 4, 5 }
conjunto2 = { 1, 2, 6, 7, 8, 9, 10 }
print('Conjunto 1: ', conjunto1)
print('Conjunto 2: ', conjunto2, '\n')

conjunto_uniao = conjunto1.union(conjunto2)
print('União: ', conjunto_uniao)

conjunto_interceccao = conjunto1.intersection(conjunto2)
print('Intercecção: ', conjunto_interceccao)

conjunto_diferenca = conjunto1.difference(conjunto2)
print('Diferença: ', conjunto_diferenca)

conjunto_diferenca_simetrica = conjunto1.symmetric_difference(conjunto2)
print('Diferença simétrica: ', conjunto_diferenca_simetrica)

conjunto_a = {1, 2, 3, 4}
conjunto_b = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

conjunto_sub = conjunto_a.issubset(conjunto_b)
print('A é subconjunto de B: ', conjunto_sub)

conjunto_sup = conjunto_a.issuperset(conjunto_b)
print('A é subconjunto de B: ', conjunto_sup)


