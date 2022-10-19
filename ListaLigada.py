from Celula import Celula
class ListaLigada:

    def __init__(self):
        self.__primeira = None
        self.__total_de_elementos = 0

    def adiciona_comeco(self, elemento):
        nova_celula = Celula(self.__primeira, elemento)
        self.__primeira = nova_celula

        if self.__total_de_elementos == 0:
            self.__ultima = self.__primeira

        self.__total_de_elementos += 1

    def adicionar_fim(self, elemento):
        if self.__total_de_elementos == 0:
            self.adiciona_comeco(elemento)
        else:
            nova_celula = Celula(None, elemento)
            self.__ultima.proxima = nova_celula
            self.__ultima = nova_celula
            self.__total_de_elementos += 1

    def adiciona_posicao(self, posicao, elemento):
        if posicao == 0:
            self.adiciona_comeco(elemento)
        elif posicao == self.__total_de_elementos:
            self.adicionar_fim(posicao-1)
        else:
            anterior = self.pegar(posicao-1)

            nova = Celula(anterior.proxima, elemento)
            anterior.proxima = nova

            self.__total_de_elementos += 1


    def pegar(self, posicao):

        if posicao < 0 or posicao >= self.__total_de_elementos:
            raise Exception("Posição Inválida")

        atual = self.__primeira

        for _ in range(0, posicao):
            atual = atual.proxima
        return atual


    def remover_comeco(self):
        self.__primeira = self.__primeira.proxima

        self.__total_de_elementos -= 1



    def tamanho(self):
        return self.__total_de_elementos

    def contem(self, elemento):
        atual = self.__primeira

        while atual is not None:
            if atual.elemento == elemento:
                return True
            atual = atual.proxima
        return False

    def remover_posicao(self, posicao):
        if posicao == 0:




    def __str__(self):

        if self.__total_de_elementos == 0:
            return '[]'

        string_final = '['
        atual = self.__primeira

        for i in range(0, self.__total_de_elementos-1):
            string_final = string_final + atual.elemento
            string_final = string_final + ', '
            atual = atual.proxima

        string_final = string_final + atual.elemento
        string_final = string_final + ']'
        return string_final

