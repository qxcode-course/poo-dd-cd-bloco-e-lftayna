from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, valor : float, descricao: str):
        self.valor : float = valor
        self.descricao : str = descricao

    def resumo(self) -> str:
        return f"Pagamento de R$ {self.valor}:{self.descricao}"

    def validar_valor(self) -> None:
        if self.valor <= 0:
            raise ValueError("falhou: valor invalido")

    @abstractmethod

    def processar(self):
        pass

class CartaoCredito(Pagamento):
    def __init__(self, num: int, nome:str, limite: float, valor: float, descricao: str):
        self.num: int = num
        self.nome: str = nome
        self.limite: float = limite

    def resumo(self):
        return "Cartao de credito: " + super().resumo()

    def getlimite(self):
        return self.limite

    def processar(self):
        if self.valor > self.limite:
            print("pagamento recursado por limite insuficiente")
            return
        self.limite -= self.valor

class Pix(Pagamento):
    def __init__(self, valor: float, descricao: str, chave:str, banco:str):
        super().__init__(valor, descricao)
        self.__chave: str = chave
        self.__banco: str = banco

    def processar(self):
        print(f"Pix aprovado via banco {self.__banco}, chave {self.__chave}")

class Boleto(Pagamento):
    def __init__(self, valor: float, descricao: str, codigobarra: int, vencimento: str):
        super().__init__(valor, descricao)
        self.__codigobarras: int = codigobarra
        self.__vencimento: str = vencimento

    def processar(self):
        print("boleto gerado. Aguardando pagamento...")
        print(f"Codigo: {self.__codigobarras} | Vencimento: {self.__vencimento}")

    def processar_pagamento(pagamento: list [Pagamento]):
        for x in pagamentos:
            x.validar_valor()
            print(x.resumo())
            x.processar()
            if isinstance(x, CartaoCredito):
                print(x.getlimite())


 