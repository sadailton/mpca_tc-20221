from posixpath import split
import os
#from utils import rf

programa = """
def soma_inteiros_posicao_impar():

    arquivo = os.path.abspath("Lista1/Exercicio 1b/lista_inteiros.txt")
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
    """
programa = """
def soma(a, b):
    print('Adailton')

soma
"""
def compara_lista():
    
    arquivo = os.path.abspath("Lista1/Exerciciob/main.py")
    lista = []
    with open(arquivo) as file_obj:
        f = file_obj.read()
        

    # for linha in programa:
    #     lista.append(eval(linha))

    d = {'a': 2, 'b': 2}
    
    obj = compile(f,arquivo,mode='exec')

    print(exec(obj, ))

    isinstance()
compara_lista()
