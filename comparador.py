# Relacionar variáveis em Template Strings: %s

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

if a > b and a > c:
    print('\nO maior número é: %s' %a)
elif b > a and b >c:
    print('\nO maior número é: %s' %b)
else:
    print('\nO maior número é: %s' %c)

print('\nFim do programa.')
