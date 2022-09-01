# -*- coding: utf-8 -*-

from posixpath import split
import os

def carrega_lista(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as txtfile:
        f = txtfile.read()
        txtfile.close()

        return f.split()

def soma_inteiros_posicao_impar(lista_inteiros):

    soma = 0

    # começa da posição 1 saltando de dois em dois
    for i in lista_inteiros[2::3]:
        soma = soma + int(i)
    
    return soma


def main():

    lista_de_inteiros = carrega_lista(os.path.abspath("Lista1/Exercicio 1b/lista_inteiros.txt"))

    soma = soma_inteiros_posicao_impar(lista_de_inteiros)
    print(soma)
    
    return True

if __name__ == '__main__':
    main()