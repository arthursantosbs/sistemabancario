menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


    
while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        valor = float(input("Digite o valor  do deposito:"))

        if valor < 0:
            print("valores negativos não são permitidos")
            continue
        else:
            saldo += valor
            extrato += f"R$ {valor:.2F} depositado \n"

    elif opcao == "s":
        print("saque")
        if LIMITE_SAQUES == numero_saques:
            print("Limite de saque diário atingido!")
            continue

        valor = float(input("Digite o valor do saque: "))

        if valor < 0 :
            print("valores negativos não são permitidos")
            continue
        elif valor > 500:
            print("valor acima de 500 não é permitido")
        elif saldo > valor:
            print("saldo indisponivel!")    
        else:
            saldo -= valor
            numero_saques += 1
            extrato += f"R${valor:.2f} Scadado"    

    elif opcao == "e":
        print('Extrato')
        print(extrato)
        print(f'Saldo da conta foi esse R$ {saldo:.2f}')
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")


