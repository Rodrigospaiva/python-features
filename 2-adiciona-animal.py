# APPEND adiciona no final da pilha.
lista_animais = ['cachorro', 'gato', 'coelho', 'tartaruga']
print(lista_animais)

animal_add = input('\nDeseja adicionar um animal? (S ou N):\n')
if animal_add == 's':
    animal = input('Qual?\n')
    lista_animais.append(animal)

    print('\nAnimal adicionado.')
    print('Nova lista: ', lista_animais, '\n')

    print('Fim do programa.')




