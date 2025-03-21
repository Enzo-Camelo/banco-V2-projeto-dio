from datetime import date, time, datetime



def menu():
    menu = """
Qual operação deseja realizar?

[d] Depositar
[s] Sacar
[e] Extrato
[nc] Nova conta
[nu] Novo usuário
[q] Sair

=> """
    return input(menu)



def depositar(saldo, valor, extrato, TRANSACOES, /):
    if TRANSACOES < 10:

        if valor > 0:
            datatime = datetime.now()
            hora = datatime.strftime("%H:%M:%S")
            data = datatime.strftime("%d/%m/%Y")

            saldo += valor
            TRANSACOES += 1
            extrato += f"Transação realizada às {hora} do dia {data}\n"
            extrato += f"Depósito: R$ {valor:.2f}\n\n"
            print("\nDepósito realizado com sucesso!")
        else:
            print("\nA operação falhou! O valor informado é inválido.")

    else:
            print("\nVocê atingiu o limite de transações permitidas hoje. Por favor volte amanhã.")

    return saldo, extrato, TRANSACOES


        
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques, transacoes):

    if transacoes < 10:
        
        if saldo > 0:

            if numero_saques < limite_saques:

                if valor <= saldo:

                    if valor > 0:

                        if valor <= limite:
                            datatime = datetime.now()
                            hora = datatime.strftime("%H:%M:%S")
                            data = datatime.strftime("%d/%m/%Y")

                            saldo -= valor
                            transacoes += 1
                            extrato += f"Transação realizada às {hora} do dia {data}\n"
                            extrato += f"Saque: R$ {valor:.2f}\n\n"
                            numero_saques += 1
                            print("\nSaque realizado com sucesso!")
                        else:
                            print("\nOperação falhou! O valor excede o limite de R$ 500.00.")

                    else:
                        print("\nOperação falhou! Não é possível sacar um valor negativo.")

                else:
                    print("\nSaldo insuficiente.")
                
            else:
                print("\nVocê excedeu o limite de saques.")

        else:
            print("\nVocê deve realizar um depósito antes de sacar um valor.")
    
    else:
        print("\nVocê atingiu o limite de transações permitidas hoje. Por favor volte amanhã.")

    return saldo, extrato, numero_saques, transacoes

        

def exibir_extrato(saldo, /, *, extrato):
    print("================== EXTRATO ==================")
    if extrato == "":
        print("Nenhuma movimentação foi realizada na conta ainda.")
    else:
        print(extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=============================================")



def criar_usuario(usuarios):
    cpf = input("\nInforme o CPF (apenas números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nUsuário já cadastrado.")
        return
    
    nome = input("\nInforme o nome completo: ")
    data_nascimento = input("\nInforme a data de nascimento (dd/mm/aaaa): ")
    endereco = input("\nInforme o endereço com este modelo:\n(Rua, número - bairro - cidade/sigla estado):\n")

    usuarios.append({"nome" : nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\nUsuário cadastrado com sucesso!")



def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None



def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("\nInforme o CPF do usuário que deseja vincular a conta (apenas números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    else:
        print("\nUsuário não encontrado.")
        

    
def base():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    TRANSACOES = 0

    saldo = 0 
    limite = 500 
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("\nInforme o valor do depósito: "))

            saldo, extrato, TRANSACOES = depositar(saldo, valor, extrato, TRANSACOES)

        elif opcao == "s":
            valor = float(input("\nInforme o valor do saque: "))

            saldo, extrato, numero_saques, TRANSACOES = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
                transacoes=TRANSACOES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "q":
            print("\nObrigado por escolher nosso banco!\nVolte sempre!")
            break

        else:
            print("\nOpção inválida.\nPor favor escolha uma das opções do menu.")



base()