# -*- coding: utf-8 -*-

from posixpath import split
import os    

def soma_inteiros_posicao_imparos.path.abspath("Lista1/Exercicio 1b/lista_inteiros.txt")():

    arquivo = 
    lista_inteiros = []

    with open(arquivo, 'r', encoding='utf-8') as txtfile:
        f = txtfile.read()
        txtfile.close()

        lista_inteiros = f.split()

    soma = 0

    # começa da posição 1 saltando de dois em dois
    for i in lista_inteiros[1::2]:
        soma = soma + int(i)

    return str(soma)
    

soma_inteiros_posicao_impar()