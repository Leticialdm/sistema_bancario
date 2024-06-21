import json
from conta import Conta
from conta import carregar_contas, salvar_contas

class Movimento:
    def __init__(self):
        self.movimentos = [] 
        
    def salvar_dados(self):
        with open('movimentos.json', 'w') as file:
            json.dump(self.movimentos, file)

    def ler_dados(self):
        try:
            with open('movimentos.json', 'r') as file:
                self.movimentos = json.load(file)
        except FileNotFoundError:
            pass

    def adicionar_movimento(self, cliente_id, descricao, valor):
        movimento = {
            'cliente_id': cliente_id,
            'descricao': descricao,
            'valor': valor
        }
        self.movimentos.append(movimento)
        self.salvar_dados()


    def adicionar_conta(self, conta):
        if conta.cliente.cpf not in self.contas:
            self.contas[conta.cliente.cpf] = conta
            print("\n\033[92mConta adicionada com sucesso!\033[0m")
        else:
            print("\n\033[91mUma conta para este CPF já existe.\033[0m")

    def buscar_conta(self, cpf):
        if cpf in self.contas:
            return self.contas[cpf]
        else:
            print("\n\033[91mNenhuma conta encontrada.\033[0m")
            print("\033[34mVoltando para o Menu Principal...\033[0m")
            return None

    def realizar_operacao(self):
        print("\n=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~")
        print("\n\033[92mO Menu de Movimentação foi selecionado com sucesso!\033[0m")
        cpf = input("\n-Para começar, digite o CPF do cliente: ")
        conta = self.buscar_conta(cpf)

        if conta:
            while True:
                print("\nEstas são as opções disponíveis para essa função:")
                print("1. Depositar")
                print("2. Sacar")
                print("3. Ver Saldo Anterior")
                print("4. Ver Saldo Atual")
                print("5. Voltar")

                opcao = input("\nPor favor, escolha uma das opções (1, 2, 3, 4 ou 5): ")

                if opcao == '1':
                    print("\n___________________________")
                    print("\033[1m Realizar Depósito\033[0m")
                    valor = float(input("\n-Digite o valor a ser depositado: R$ "))
                    conta.deposito(valor)
                elif opcao == '2':
                    print("\n___________________________")
                    print("\033[1m Realizar Saque\033[0m")
                    valor = float(input("\n-Digite o valor a ser sacado: "))
                    conta.saque(valor)
                elif opcao == '3':
                    print("\n___________________________")
                    print("\033[1m Consultar Saldo Anterior\033[0m")
                    print(f"\n-Saldo Anterior: {conta.saldo_anterior()}")
                elif opcao == '4':
                    print("\n___________________________")
                    print("\033[1m Consultar Saldo Atual\033[0m")
                    print(f"\n-Saldo Atual: {conta.saldo_atual()}")
                elif opcao == '5':
                    print("\n\033[34mVoltando ao menu principal...\033[0m")
                    break
                else:
                    print("\033[1;91mOpção inválida. Tente novamente.\033[0m")
