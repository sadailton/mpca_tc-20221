# -*- coding: utf-8 -*-

from posixpath import split

def carrega_lista(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as txtfile:
        f = txtfile.read()
        txtfile.close()

        return f.split()

def soma_inteiros_posicao_impar(lista_inteiros):

    soma = 0

    # começa da posição 1 saltando de dois em dois
    for i in lista_inteiros[1::2]:
        soma = soma + int(i)
    
    return soma


def main():

    lista_de_inteiros = carrega_lista('lista_inteiros.txt')

    soma = soma_inteiros_posicao_impar(lista_de_inteiros)
    print(soma)
    
    return True

if __name__ == '__main__':
    main()