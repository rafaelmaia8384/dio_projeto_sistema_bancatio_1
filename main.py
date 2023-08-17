menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Escolha uma opção: 
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor a ser depositado: "))
        if valor < 0:
            print("Valor inválido!")
            continue
        saldo += valor
        extrato += f"Depósito: {valor:.2f}\n"

    elif opcao == "s":
        valor = float(input("Digite o valor a ser sacado: "))
        if valor < 0:
            print("Valor inválido!")
            continue
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        if excedeu_saldo:
            print("Saldo insuficiente!")
        elif excedeu_limite:
            print("Limite excedido!")
        elif excedeu_saques:
            print("Limite de saques excedido!")
        else:
            saldo -= valor
            extrato += f"Saque: {valor:.2f}\n"
            numero_saques += 1

    elif opcao == "e":
        print("=" * 40)
        print("Nenhuma movimentação" if extrato == "" else extrato, end="")
        print(f"\nSaldo: {saldo:.2f}")
        print("=" * 40)

    elif opcao == "q":
        break

    else:
        print("Opção inválida!\n\n")
