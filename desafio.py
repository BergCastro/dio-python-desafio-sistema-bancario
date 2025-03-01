import datetime

LIMITE_SAQUES = 3
SAQUE_MAXIMO = 500
SALDO_INICIAL = 0

def exibir_menu():
    menu = """
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [q]\tSair
    ======================================
    => """
    return input(menu)

def depositar(saldo, extrato):
    try:
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
    return saldo, extrato

def sacar(saldo, extrato, numero_saques):
    if numero_saques >= LIMITE_SAQUES:
        print("Limite de saques diários atingido.")
        return saldo, extrato, numero_saques
    try:
        valor = float(input("Informe o valor do saque: "))

        if valor <= 0:
            print("Valor inválido para saque.")
        elif valor > SAQUE_MAXIMO:
            print(f"O valor máximo por saque é de R$ {SAQUE_MAXIMO:.2f}")
        elif valor > saldo:
            print("Saldo insuficiente.")
        else:
            saldo -= valor
            extrato += f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")
        return saldo, extrato, numero_saques
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
        return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def main():
    saldo = SALDO_INICIAL
    extrato = ""
    numero_saques = 0

    while True:
        opcao = exibir_menu()

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques)
        elif opcao == "e":
            exibir_extrato(saldo, extrato)
        elif opcao == "q":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, selecione uma opção válida.")

if __name__ == "__main__":
    main()