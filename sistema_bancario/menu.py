from cliente import CadastroClientes
from agencia import CadastroAgencias
from conta import ContaCorrente, ContaEspecial, carregar_contas, salvar_contas
from movimento import Movimento

def menu_principal():
    cadastro_clientes = CadastroClientes()
    cadastro_agencias = CadastroAgencias()
    contas = carregar_contas()
    movimentos = Movimento()

    opcao = ''
    while opcao != '5':
        print("\n=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~ MENU ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=")
        print("\n\033[1mAtenção! Estas são as opções de funcionalidade deste programa:\033[0m")
        print("\n1. Gerenciar Clientes")
        print("2. Gerenciar Agências")
        print("3. Gerenciar Contas")
        print("4. Gerenciar Movimentação")
        print("5. Sair")

        opcao = input("\nPor favor, escolha uma opção (1, 2, 3, 4 ou 5): ")

        if opcao == '1':
            menu_clientes(cadastro_clientes)
        elif opcao == '2':
            menu_agencias(cadastro_agencias)
        elif opcao == '3':
            menu_contas(contas, cadastro_clientes)
        elif opcao == '4':
            menu_movimentacao(contas, cadastro_clientes, movimentos)
        elif opcao == '5':
            print("\033[1;91mSAINDO DO PROGRAMA... Obrigada(o) e volte sempre!\033[0m")
            salvar_contas(contas)
        else:
            print("\n\033[1;91mOpção inválida. Tente novamente escolhendo entre 1, 2, 3, 4 ou 5.\033[0m")

def menu_clientes(cadastro_clientes):
    opcao = ''
    while opcao != '5':
        print("\n=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~")
        print("\n\033[92mO Menu de Clientes foi selecionado com sucesso!\033[0m")
        print("\nEstas são as opções disponíveis para essa função:")
        print("1. Inserir Cliente")
        print("2. Listar Clientes")
        print("3. Excluir Cliente")
        print("4. Alterar Informações do Cliente")
        print("5. Voltar")

        opcao = input("\nPor favor, escolha uma das opções (1, 2, 3, 4 ou 5): ")

        if opcao == '1':
            cadastro_clientes.inserir_cliente()
        elif opcao == '2':
            clientes = cadastro_clientes.listar_clientes()
            if not clientes:
                print("\n\033[91mNenhum cliente cadastrado até o momento.\033[0m")
                print("\033[34mVoltando para o Menu de Clientes...\033[0m")
            else:
                print("\n___________________________")
                print("\033[1m    LISTA DE CLIENTES:\033[0m")
                for indice, cliente in enumerate(clientes):
                    print(f"\n{indice}. {cliente}")
                    print("__________________________")
        elif opcao == '3':
            cadastro_clientes.excluir_cliente()
        elif opcao == '4':
            cadastro_clientes.alterar_cliente()
        elif opcao == '5':
            print("\n\033[34mVoltando ao menu principal...\033[0m")
        else:
            print("\033[1;91mOpção inválida. Tente novamente.\033[0m")

def menu_agencias(cadastro_agencias):
    opcao = ''
    while opcao != '5':
        print("\n=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~")
        print("\n\033[92mO Menu de Agências foi selecionado com sucesso!\033[0m")
        print("\nEstas são as opções disponíveis para essa função:")
        print("1. Inserir Agência")
        print("2. Listar Agências")
        print("3. Excluir Agência")
        print("4. Alterar Informações de Agência")
        print("5. Voltar")

        opcao = input("\nPor favor, escolha uma das opções (1, 2, 3, 4 ou 5): ")

        if opcao == '1':
            cadastro_agencias.inserir_agencia()
        elif opcao == '2':
            agencias = cadastro_agencias.listar_agencias()
            if not agencias:
                print("\n\033[91mNenhuma agência cadastrada até o momento.\033[0m")
                print("\033[34mVoltando para o Menu de Agências...\033[0m")
            else:
                print("\n___________________________")
                print("\033[1m    LISTA DE AGÊNCIAS:\033[0m")
                for indice, agencia in enumerate(agencias):
                    print(f"{indice}. {agencia}")
                    print("__________________________")
        elif opcao == '3':
            cadastro_agencias.excluir_agencia()
        elif opcao == '4':
            cadastro_agencias.alterar_agencia()
        elif opcao == '5':
            print("\n\033[34mVoltando ao menu principal...\033[0m")
        else:
            print("\033[1;91mOpção inválida. Tente novamente.\033[0m")

def menu_contas(contas, cadastro_clientes):
    opcao = ''
    while opcao != '5':
        print("\n=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~")
        print("\n\033[92mO Menu de Contas foi selecionado com sucesso!\033[0m")
        print("\nEstas são as opções disponíveis para essa função:")
        print("1. Criar Conta Corrente")
        print("2. Criar Conta Especial")
        print("3. Consultar Saldo")
        print("4. Consultar Extrato")
        print("5. Voltar")

        opcao = input("\nPor favor, escolha uma das opções (1, 2, 3, 4 ou 5): ")

        if opcao == '1':
            print("\n___________________________")
            print("\033[1m Cadastrar Conta Corrente\033[0m")
            cpf = input("\n-Digite o CPF do cliente: ")
            cliente = cadastro_clientes.buscar_cliente(cpf)
            if cliente:
                nova_conta = ContaCorrente(cliente)  # ou ContaEspecial(cliente)
                contas.append(nova_conta)
                print("\033[92m\nConta corrente criada com sucesso para o cliente:", cliente.nome, "\033[0m")
                print("\033[34mVoltando para o Menu de Contas...\033[0m")
            else:
                print("\033[91m\nCliente não encontrado. Não foi possível criar a conta corrente.\033[0m")
                print("\033[34mVoltando para o Menu de Contas...\033[0m")

        elif opcao == '2':
            print("\n___________________________")
            print("\033[1m  Cadastrar Conta Especial\033[0m")
            cpf = input("\n-Digite o CPF do cliente: ")
            cliente = cadastro_clientes.buscar_cliente(cpf)
            if cliente:
                nova_conta = ContaEspecial(cliente)  # ou ContaCorrente(cliente)
                contas.append(nova_conta)
                print("\033[92m\nConta especial criada com sucesso para o cliente:", cliente.nome, "\033[0m")
                print("\033[34mVoltando para o Menu de Contas...\033[0m")
            else:
                print("\033[91m\nCliente não encontrado. Não foi possível criar a conta especial.\033[0m")
                print("\033[34mVoltando para o Menu de Contas...\033[0m")

        elif opcao == '3':
            print("\n___________________________")
            print("\033[1m Consultar Saldo\033[0m")
            cpf = input("\n-Digite o CPF do cliente: ")
            cliente = cadastro_clientes.buscar_cliente(cpf)
            if cliente:
                conta_encontrada = False
                for conta in contas:
                    if isinstance(conta, (ContaCorrente, ContaEspecial)) and conta.cliente == cliente:
                        print("\nSaldo da conta:", conta.consultar_saldo())
                        conta_encontrada = True
                        break
                if not conta_encontrada:
                    print("\nConta não encontrada para o cliente informado.")
                    print("\033[34mVoltando para o Menu de Contas...\033[0m")
            else:
                print("\nCliente não encontrado.")
                print("\033[34mVoltando para o Menu de Contas...\033[0m")

        elif opcao == '4':
            print("\n___________________________")
            print("\033[1m Consultar Extrato\033[0m")
            cpf = input("\n-Digite o CPF do cliente: ")
            cliente = cadastro_clientes.buscar_cliente(cpf)
            if cliente:
                conta_encontrada = False
                for conta in contas:
                    if isinstance(conta, (ContaCorrente, ContaEspecial)) and conta.cliente == cliente:
                        extrato = conta.consultar_extrato()
                        if extrato:
                            print("\nExtrato da conta:")
                            for movimento in extrato:
                                print(movimento)
                        else:
                            print("\033[91m\nNenhum movimento registrado nesta conta.\033[0m")
                            print("\033[34mVoltando para o Menu de Contas...\033[0m")
                        conta_encontrada = True
                        break
                if not conta_encontrada:
                    print("\033[91m\nConta não encontrada para o cliente informado.\033[0m")
                    print("\033[34mVoltando para o Menu de Contas...\033[0m")
            else:
                print("\033[91m\nCliente não encontrado.\033[0m")
                print("\033[34mVoltando para o Menu de Contas...\033[0m")

        elif opcao == '5':
            print("\n\033[34mVoltando ao menu principal...\033[0m")
            break

        else:
            print("\033[1;91mOpção inválida. Tente novamente.\033[0m")

def menu_movimentacao(contas, cadastro_clientes, movimentos):
    opcao = ''
    while opcao != '3':
        print("\n=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~")
        print("\n\033[92mMenu de Movimentação foi selecionado com sucesso!\033[0m")
        print("\nOpções disponíveis:")
        print("1. Depósito")
        print("2. Saque")
        print("3. Voltar")

        opcao = input("\nPor favor, escolha uma das opções (1, 2 ou 3): ")

        if opcao == '1':
            cpf = input("\nDigite o CPF do cliente: ")
            cliente = cadastro_clientes.buscar_cliente(cpf)
            if cliente:
                valor_deposito = float(input("\nDigite o valor do depósito: "))
                for conta in contas:
                    if isinstance(conta, (ContaCorrente, ContaEspecial)) and conta.cliente == cliente:
                        if conta.deposito(valor_deposito):
                            movimentos.adicionar_movimento(cliente.cpf, f"Depósito: +{valor_deposito}", valor_deposito)
                            print("\nDepósito realizado com sucesso.")
                        else:
                            print("\nDepósito não pôde ser realizado.")
                        break
                else:
                    print("\nConta não encontrada para o cliente informado.")

            else:
                print("\nCliente não encontrado.")

        elif opcao == '2':
            cpf = input("\nDigite o CPF do cliente: ")
            cliente = cadastro_clientes.buscar_cliente(cpf)
            if cliente:
                valor_saque = float(input("\nDigite o valor do saque: "))
                for conta in contas:
                    if isinstance(conta, (ContaCorrente, ContaEspecial)) and conta.cliente == cliente:
                        if conta.saque(valor_saque):
                            movimentos.adicionar_movimento(cliente.cpf, f"Saque: -{valor_saque}", valor_saque)
                            print("\nSaque realizado com sucesso.")
                        else:
                            print("\nSaque não pôde ser realizado.")
                        break
                else:
                    print("\n\033[92m______________________________\033[0m")
                    print("\033[92mMovimentação realizada com sucesso!\033[0m") #ERRADO
                    print("\033[34mVoltando para o Menu de Movimentação...\033[0m")
            else:
                print("\nCliente não encontrado.")

        elif opcao == '3':
            print("\nSaindo do menu de movimentação.")
            break
        else:
            print("\nOpção inválida. Por favor, escolha 1, 2 ou 3.")

if __name__ == "__main__":
    menu_principal()
