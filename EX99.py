
def maior (*num):
    cont= maior = 0
    print('')
    print('Valores')
    print('')
    for valor in num:
        print(f'{valor}', end=' ', flush = True)
        
        if cont ==0:
            maior = valor
        else:
            if valor > maior:
                maior= valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print('')
    print(f'O maior valor informado foi {maior}.')
    print('')


maior (2, 4, 10, 15, 23, 105, 2)
