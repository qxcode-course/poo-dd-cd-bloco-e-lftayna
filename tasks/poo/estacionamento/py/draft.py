from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, id : str, tipo: str):
        self.__id : str = id
        self.__tipo: str = tipo
        self.__horaEntrada: int = 0

    def getEntrada(self) -> int:
        return self.__horaEntrada

    def getTipo(self) -> str:
        return self.__tipo

    def getId(self) -> str:
        return self.__id

    def setEntrada(self, horaEntrada: int):
         self.__horaEntrada = horaEntrada 

    @abstractmethod

    def calcularvalor(self, horaSaida: int) -> float:
        pass

    def __str__(self) -> str:
        return f"{self.__id}:{self.__tipo}:{self.__horaEntrada}"

class Bike(Veiculo):
    def __init__(self, id: str):
        super().__init__(id, "Bike")

    def calcularvalor(self, horaSaida: int) -> None:
        tempo = horaSaida - self.getEntrada()
        return tempo * 0.015

class Moto(Veiculo):
    def __init__(self, id: str):
        super().__init__(id, "Moto")

    def calcularvalor(self, horaSaida: int) -> None:
        tempo = horaSaida - self.getEntrada()
        return tempo * 0.05

class Carro(Veiculo):
    def __init__(self, id: str):
        super().__init__(id, "Carro")

    def calcularvalor(self, horaSaida: int) -> None:
        tempo = horaSaida - self.getEntrada()
        valor = tempo * 0.10
        if valor < 5:
            valor = 5
        return valor

class Estacionamento:
    def __init__(self):
        self.__horaAtual : int = 0
        self.__veiculos : list[Veiculo] = []

    ##def procurarVeiculo(self, id: str) -> int:

    def estacionar(self, veiculo = Veiculo) -> None:
        veiculo.setEntrada(self.__horaAtual)
        self.__veiculos.append(veiculo)

    def pagar(self, id: str) -> None:
        for x in self.__veiculos:
            if x.getId() == id:
                entrada = x.getEntrada()
                saida = self.__horaAtual
                valor = x.calcularvalor(saida)
                print(f"{x.getTipo()} chegou {entrada} saiu {saida}. Pagar R$ {valor:.2f}")  
                return    

    def __str__(self) -> str:
        saida = ""
        for x in self.__veiculos:
            tipo = x.getTipo()
            id = x.getId()
            hora = x.getEntrada()

            tipo_mask = "_" * (10 - len(tipo)) + tipo
            id_mask = "_" * (10 - len(id)) + id

            saida += f"{tipo_mask} : {id_mask} : {hora}\n"
        saida += f"Hora atual: {self.__horaAtual}"
        return saida

    def passartempo(self, tempo: int) -> None:
        self.__horaAtual += tempo


def main():
    estacionamento = Estacionamento()
    while True:
        line : str = input()
        print("$" + line)
        args = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(estacionamento)
        elif args[0] == "tempo":
            tempo = int(args[1])
            estacionamento.passartempo(tempo)
        elif args[0] == "estacionar":
            tipo = args[1].lower()
            id = args[2] 
            if tipo == "bike":
                estacionamento.estacionar(Bike(id))
            if tipo == "moto":
                estacionamento.estacionar(Moto(id))
            if tipo == "carro":
                estacionamento.estacionar(Carro(id))
        elif args[0] == "pagar":
            id = args[1]
            estacionamento.pagar(id)
        else:
            print("comando invalido")



main()


        
    



