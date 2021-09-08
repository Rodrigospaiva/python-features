animal = input('Digite o nome do animal: ')

lista_animais = ['cachorro',
                 'gato',
                 'coelho',
                 'tartaruga']

if animal in lista_animais:
    print('Animal existente na lista.')
else:
    print('Animal não encontrado.')
    animal_add = input('Deseja adicioná-lo? (S ou N):\n')
    if animal_add == 's':
        lista_animais.append(animal)
        print('Novo animal adicionado.')
        print(lista_animais)
    else:
        print('Fim do programa.')





