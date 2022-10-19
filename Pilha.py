from ListaLigada import ListaLigada

class Pilha:
    def __init__(self):
        self.__pecas = ListaLigada()

    def insere(self, nome):
        self.__pecas.adiciona_comeco(nome)


    def remove(self):
        self.__pecas.remover_comeco()

    def vazia(self):
        if self.__pecas.tamanho() == 0:
            return True
        return False


    def __str__(self):
        return self.__pecas.__str__()