from abc import ABC, abstractmethod

class Animal(abc, ABC):
    def __init__(self, nome: str):
        self.__nome: str = nome

    def apresentar_nome(self):
        print(f"Eu sou um(a) {self.__name}")

class Leao(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def fazer_som(self):
        print(f"roar")
    
    def mover(self):
        print("andando")

class Elefante(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def fazer_som(self):
        print("afruuuuu")
    
    def mover(self):
        print("pisando")

class Cobra(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def fazer_som(self):
        print("pspspspsps")
    
    def mover(self):
        print("rastejando")

