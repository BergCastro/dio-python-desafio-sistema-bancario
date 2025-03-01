import datetime
import textwrap

LIMITE_SAQUES = 3
SAQUE_MAXIMO = 500
SALDO_INICIAL = 0
AGENCIA = "0001"

usuarios = []
contas = []
numero_conta = 1


def menu():
    menu = """\n
    ================ MENU ================
    [c]\tCriar Usuário
    [cc]\tCriar Conta Corrente
    [lc]\tListar Contas
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    """Realiza um depósito na conta (positional-only arguments)."""
    if valor > 0:
        saldo += valor
        extrato += f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - Depósito: R$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato


def extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


def criar_usuario():
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input(
        "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): "
    )

    usuarios.append(
        {"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco}
    )

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta_corrente():
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf)

    if usuario:
        global numero_conta
        conta = {
            "agencia": AGENCIA,
            "numero_conta": numero_conta,
            "usuario": usuario,
        }
        contas.append(conta)
        numero_conta += 1
        print("\n=== Conta criada com sucesso! ===")
    else:
        print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas():
    if not contas:
        print("Não há contas cadastradas.")
        return

    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    saldo = SALDO_INICIAL
    limite = SAQUE_MAXIMO
    extrato_bancario = ""
    numero_saques = 0

    while True:
        opcao = menu()

        if opcao == "c":
            criar_usuario()
        elif opcao == "cc":
            criar_conta_corrente()
        elif opcao == "lc":
            listar_contas()
        elif opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato_bancario = depositar(saldo, valor, extrato_bancario)
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato_bancario = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato_bancario,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        elif opcao == "e":
            extrato(saldo, extrato=extrato_bancario)
        elif opcao == "q":
            print("Saindo...")
            break
        else:
            print(
                "Operação inválida, por favor selecione novamente a operação desejada."
            )


if __name__ == "__main__":
    main()