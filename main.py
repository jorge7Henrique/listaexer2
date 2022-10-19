# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Pilha import Pilha
from Fila import Fila

def teste_pilha():
    print("Teste")

    fila = Fila()

    fila.inserir("Gustavo")
    fila.inserir("Jorge")
    fila.inserir("Peixoto")
    fila.inserir("Ítalo")
    print(fila)

    fila.remove()
    print(fila)
    fila.remove()
    print(fila)
    fila.remove()
    print(fila)
    fila.remove()
    print(fila)


    print(fila.vazia())


if __name__ == '__main__':
    teste_pilha()
