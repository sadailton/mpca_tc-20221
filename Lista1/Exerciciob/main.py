from posixpath import split
import os

def soma_inteiros_posicao_impar():

    arquivo = os.path.abspath("Lista1/Exerciciob/lista_inteiros.txt")
    lista_inteiros = []

    with open(arquivo, 'r', encoding='utf-8') as txtfile:
        f = txtfile.read()
        txtfile.close()

        lista_inteiros = f.split()

    soma = 0

    # começa da posição 2 saltando de três em três
    for i in lista_inteiros[2::3]:
        soma = soma + int(i)

    return str(soma)
    

soma_inteiros_posicao_impar()