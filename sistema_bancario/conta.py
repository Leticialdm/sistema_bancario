import json

def salvar_contas(contas):
    with open('contas.json', 'w') as file:
        json.dump(contas, file, default=lambda o: o.__dict__)

def carregar_contas():
    try:
        with open('contas.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

class Conta:
    def __init__(self, cliente, saldo=0):
        self.cliente = cliente
        self.saldo = saldo
        self.movimentos = []  

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.movimentos.append(f"Depósito: +{valor}")
            return True  
        return False 

    def saque(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            self.movimentos.append(f"Saque: -{valor}")
            return True  
        return False  

    def consultar_saldo(self):
        return self.saldo

    def consultar_extrato(self):
        return self.movimentos

class ContaCorrente(Conta):
    def __init__(self, cliente, saldo=0, limite=1000):
        super().__init__(cliente, saldo)
        self.limite = limite

class ContaEspecial(Conta):
    def __init__(self, cliente, saldo=0, limite=2000):
        super().__init__(cliente, saldo)
        self.limite = limite
