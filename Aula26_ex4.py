from random import randint
from time import sleep



def sortear(lista):
    print( 'sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n=randint(1,10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.4)
        print('pronto!')


def somapar(lista):
    soma=0
    for valor in lista:
        if valor % 2==0:
            soma+=valor
    print(f'somando os valores pares de {lista}, temos {soma}')


    numeros=list()
    sortear(numeros)
    somapar(numeros) 