def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato


def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= limite_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def cadastrar_cliente(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("Usuário já cadastrado!")
        return
    
    nome = input("Informe o nome: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro – bairro – cidade/sigla estado): ")
    usuarios.append({"cpf": cpf, "nome": nome, "data_nascimento": data_nascimento, "endereco": endereco})
    print("Usuário cadastrado com sucesso!")


def cadastrar_conta_bancaria(usuarios, contas, numero_conta):
    cpf = input("Informe o CPF do usuário: ")
    usuario = next((u for u in usuarios if u['cpf'] == cpf), None)
    if usuario:
        contas.append({"agencia": "0001", "numero_conta": numero_conta, "usuario": usuario})
        print("Conta criada com sucesso!")
        return numero_conta + 1
    else:
        print("Usuário não encontrado! Cadastre o usuário primeiro.")
        return numero_conta


def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []
    numero_conta = 1

    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo Usuário
    [nc] Nova Conta
    [q] Sair
    => """

    while True:
        opcao = input(menu).strip().lower()
        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = deposito(saldo, valor, extrato)
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "nu":
            cadastrar_cliente(usuarios)
        elif opcao == "nc":
            numero_conta = cadastrar_conta_bancaria(usuarios, contas, numero_conta)
        elif opcao == "q":
            break
        else:
            print("Operação inválida, tente novamente!")


if __name__ == "__main__":
    main()