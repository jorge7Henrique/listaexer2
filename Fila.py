from ListaLigada import ListaLigada

class Fila:
    def __init__(self):
        self.__fila = ListaLigada()

    def inserir(self, nome):
         self.__fila.adicionar_fim(nome)


    def remove(self):
            self.__fila.remover_comeco()

    def vazia(self):
        if self.__fila.tamanho() == 0:
            return True
        return False

    def __str__(self):
        return self.__fila.__str__()