import json

class Agencia:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def __str__(self):
        return f"Nome: {self.nome}, Endereço: {self.endereco}"

class CadastroAgencias:
    def __init__(self):
        self.agencias = []
        self.arquivo_agencias = 'agencias.json'
        self.ler_dados()

    def inserir_agencia(self):
        print("\n___________________________")
        print("\033[1m      Inserir Agências\033[0m")
        nome = input("\n-Digite o nome da agência: ")
        endereco = input("\n-Digite o endereço da agência: ")
        print("\n\033[92m______________________________\033[0m")
        print("\033[92mAgência registrada com sucesso!\033[0m")
        print("\033[34mVoltando para o Menu de Agências...\033[0m")
        agencia = Agencia(nome, endereco)
        self.agencias.append(agencia)
        self.salvar_dados()

    def listar_agencias(self):
        return self.agencias

    def excluir_agencia(self):
        if not self.agencias:
            print("\n\033[91mNenhuma agência cadastrado até o momento.\033[0m")
            print("\033[34mVoltando para o Menu de Agências...\033[0m")
            return

        print("\n___________________________")
        print("\033[1m    LISTA DE AGÊNCIAS:\033[0m")
        for indice, agencia in enumerate(self.agencias):
            print(f"{indice}. {agencia}")

        indice = int(input("\n-Digite o índice da agência a ser excluída: "))
        if 0 <= indice < len(self.agencias):
            del self.agencias[indice]
            self.salvar_dados()
            print("\n\033[92m______________________________\033[0m")
            print("\033[92mAgência excluída com sucesso!\033[0m")
            print("\033[34mVoltando para o Menu de Agências...\033[0m")
        else:
            print("\n\033[1;91mÍndice inválido\033[0m")
            print("\033[34mVoltando para o Menu de Agências...\033[0m")

    def alterar_agencia(self):
        if not self.agencias:
            print("\n\033[91mNenhuma agência cadastrada até o momento.\033[0m")
            print("\033[34mVoltando para o Menu de Agências...\033[0m")
            return

        print("\n___________________________")
        print("\033[1m    LISTA DE AGÊNCIAS:\033[0m")
        for indice, agencia in enumerate(self.agencias):
            print(f"{indice}. {agencia}")

        indice = int(input("\nDigite o índice da agência a ser alterada: "))
        if 0 <= indice < len(self.agencias):
            agencia = self.agencias[indice]
            print("\nOpções de alteração:")
            print("1. Alterar Nome")
            print("2. Alterar Endereço")

            opcao = input("\nPor favor, escolha uma das opções (1 ou 2): ")

            if opcao == '1':
                novo_nome = input("\nDigite o novo nome da agência: ")
                agencia.nome = novo_nome
                print("\n\033[92mNome da agência alterado com sucesso!\033[0m")
            elif opcao == '2':
                novo_endereco = input("\nDigite o novo endereço da agência: ")
                agencia.endereco = novo_endereco
                print("\n\033[92mEndereço da agência alterado com sucesso!\033[0m")
            else:
                print("\n\033[1;91mOpção inválida. Tente novamente.\033[0m")
                print("\033[34mVoltando para o Menu de Agências...\033[0m")

            self.salvar_dados()
            print("\033[34mVoltando para o Menu de Agências...\033[0m")
        else:
            print("\n\033[1;91mÍndice inválido\033[0m")
            print("\033[34mVoltando para o Menu de Agências...\033[0m")

    def salvar_dados(self):
        with open(self.arquivo_agencias, 'w') as file:
            json.dump([vars(agencia) for agencia in self.agencias], file)

    def ler_dados(self):
        try:
            with open(self.arquivo_agencias, 'r') as file:
                data = json.load(file)
                self.agencias = [Agencia(**agencia) for agencia in data]
        except FileNotFoundError:
            pass
