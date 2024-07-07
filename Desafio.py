DEPOSITOS_FEITOS = []
SAQUES_FEITOS = []
LimiteSaque = 3
saldo = sum(DEPOSITOS_FEITOS)


def Depositar():
    global DEPOSITOS_FEITOS, saldo
    try:
        deposito = float(input("Digite a quantia a ser depositado\n"))
    except:
        print("Digite um número válido.")
        Depositar()

    DEPOSITOS_FEITOS.append(deposito)
    saldo = sum(DEPOSITOS_FEITOS)

    escolha = input(
        "\nVocê deseja fazer outro depósito?\n[1] Sim\n[2] Não\n\n")
    if (escolha == "1"):
        Depositar()
    elif (escolha == "2"):
        print("\nRetornando ao menu...\n")
        Menu()


def Sacar():
    global LimiteSaque
    global saldo

    try:
        Saque = float(input(
            "\nDigite a quantidade em R$ que você deseja sacar:\n(OBS: Limite por saque é de R$500.00)\n\n"))
    except:
        print("Valor inválido. Digite um número.\n\n")
        Sacar()

    if (LimiteSaque == 0):
        print("\nVocê já realizou o máximo de saques diários.\nVolte amanhã para ter mais 3 saques diários.\n\n")
        Menu()

    if (Saque > saldo) and (LimiteSaque != 0):
        escolha = input(
            "\nSaldo insuficiente.\n\nVocê deseja retornar ao Menu?\n[1] Sim.\n[2] Não\n")
        if (escolha == "1"):
            Menu()

    elif (Saque > 500) and (LimiteSaque != 0):
        print("Tentativa de saque ultrapassa o limite de R$500,00. Retornando ao Menu.")
        Menu()

    else:
        saldo -= Saque
        SAQUES_FEITOS.append(Saque)
        LimiteSaque -= 1
        escolha = input(
            "\nSaque realizado com sucesso!\n\nVocê deseja realizar outro saque?\n[1] Sim\n[2] Não\n")
        if escolha == "1":
            Sacar()
        else:
            print("\n\nRetornando ao Menu\n")
            Menu()


def Extrato():
    global saldo
    n1 = 1
    n2 = 1
    if not DEPOSITOS_FEITOS and not SAQUES_FEITOS:
        print("\n\nNão foram realizadas movimentações recentes.")
    else:
        print("\nExtrato:")
        for deposito in DEPOSITOS_FEITOS:
            print(f"{n1}° Depósito: R$ {deposito:.2f}")
            n1 += 1
        for saque in SAQUES_FEITOS:
            print(f"{n2}° Saque: R$ {saque:.2f}")
            n2 += 1
    print(f"Saldo total da conta: R${saldo:.2f}")


def Menu():
    print("\nMenu:")
    print("[1] Depositar")
    print("[2] Sacar")
    print("[3] Extrato")
    print("[4] Sair")

    escolha = input("\nEscolha uma opção: ")

    if escolha == "1":
        Depositar()
    elif escolha == "2":
        Sacar()
    elif escolha == "3":
        Extrato()
    elif escolha == "4":
        print("Saindo...")
    else:
        print("Opção inválida!")
        Menu()


Menu()
