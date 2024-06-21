import uuid
import json


class Cliente:
    def __init__(self, nome, cpf):
        self.id = str(uuid.uuid4())
        self.nome = nome
        self.cpf = cpf

    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}"


class CadastroClientes:
    def __init__(self):
        self.clientes = []
        self.arquivo_clientes = 'clientes.json'
        self.ler_dados()
    
    def buscar_cliente(self, cpf):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente
        return None 

    def inserir_cliente(self):
        print("\n___________________________")
        print("\033[1m      Inserir Cliente\033[0m")
        nome = input("\n-Digite o nome do cliente: ")
        cpf = input("\n-Agora, digite o cpf do cliente: ")
        print("\n\033[92m______________________________\033[0m")
        print("\033[92mCliente registrado com sucesso!\033[0m")
        print("\033[34mVoltando para o Menu de Clientes...\033[0m")
        cliente = Cliente(nome, cpf)
        self.clientes.append(cliente)
        self.salvar_dados()

    def listar_clientes(self):
        return self.clientes

    def excluir_cliente(self):
        if not self.clientes:
            print("\n\033[91mNenhum cliente cadastrado até o momento.\033[0m")
            print("\033[34mVoltando para o Menu de Clientes...\033[0m")
            return

        print("\n___________________________")
        print("\033[1m    LISTA DE CLIENTES:\033[0m")
        for indice, cliente in enumerate(self.clientes):
            print(f"{indice}. {cliente}")

        indice = int(input("\n-Digite o índice do cliente a ser excluído: "))
        if 0 <= indice < len(self.clientes):
            del self.clientes[indice]
            self.salvar_dados()
            print("\n\033[92m______________________________\033[0m")
            print("\033[92mCliente excluído com sucesso!\033[0m")
            print("\033[34mVoltando para o Menu de Clientes...\033[0m")
        else:
            print("\n\033[1;91mÍndice inválido\033[0m")
            print("\033[34mVoltando para o Menu de Clientes...\033[0m")

    def salvar_dados(self):
        with open(self.arquivo_clientes, 'w') as file:
            json.dump([vars(cliente) for cliente in self.clientes], file)

    def ler_dados(self):
        try:
            with open(self.arquivo_clientes, 'r') as file:
                data = json.load(file)
                print("Data lida do arquivo:", data)
                self.clientes = [Cliente(**cliente) for cliente in data]
        except FileNotFoundError:
            print("Arquivo de clientes não encontrado.")
        except json.JSONDecodeError as e:
            print("Erro ao decodificar JSON:", e)


    def alterar_cliente(self):
        cpf = input("\n-Digite o CPF do cliente a ser alterado: ")
        cliente = self.buscar_cliente(cpf)

        if cliente:
            print(f"\nCliente encontrado: {cliente.nome}, CPF: {cliente.cpf}")
            novo_nome = input("\n-Digite o novo nome (ou deixe em branco para manter o atual): ")
            novo_cpf = input("\n-Digite o novo CPF (ou deixe em branco para manter o atual): ")

            if novo_nome:
                cliente.nome = novo_nome
            if novo_cpf:
                cliente.cpf = novo_cpf

            print("\n\033[92m______________________________\033[0m")
            print("\033[92mDados do cliente alterados com sucesso!\033[0m")
            print("\033[34mVoltando para o Menu de Clientes...\033[0m")
            self.salvar_dados()
        else:
            print("\n\033[91mCliente não encontrado.\033[0m")
            print("\033[34mVoltando para o Menu de Clientes...\033[0m")


class Movimento:
    def __init__(self):
        self.movimentos = []
        self.arquivo_movimentos = 'movimentos.json'
        self.ler_dados()

    def adicionar_movimento(self, cliente_id, descricao, valor):
        movimento = {
            'cliente_id': cliente_id,
            'descricao': descricao,
            'valor': valor
        }
        self.movimentos.append(movimento)
        self.salvar_dados()

    def salvar_dados(self):
        with open(self.arquivo_movimentos, 'w') as file:
            json.dump(self.movimentos, file)

    def ler_dados(self):
        try:
            with open(self.arquivo_movimentos, 'r') as file:
                self.movimentos = json.load(file)
        except FileNotFoundError:
            pass