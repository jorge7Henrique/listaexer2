class Celula:
    def __init__(self, proxima, celula):
        self.__proxima = proxima
        self.__elemento = celula


    @property
    def proxima(self):
        return self.__proxima

    @proxima.setter
    def proxima(self, proxima):
        self.__proxima = proxima

    @property
    def elemento(self):
        return self.__elemento

    def __str__(self):
        return self.__elemento
