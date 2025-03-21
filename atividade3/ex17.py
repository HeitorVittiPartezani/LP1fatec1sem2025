valor_saque = int(input("Digite o valor do saque (apenas múltiplos de 10): "))

if valor_saque % 10 != 0:
    print("Valor inválido. O saque deve ser múltiplo de 10.")
else:
    notas_100 = valor_saque // 100
    valor_saque %= 100
    notas_50 = valor_saque // 50
    valor_saque %= 50
    notas_20 = valor_saque // 20
    valor_saque %= 20
    notas_10 = valor_saque // 10

    print(f"Notas de R$ 100: {notas_100}")
    print(f"Notas de R$ 50: {notas_50}")
    print(f"Notas de R$ 20: {notas_20}")
    print(f"Notas de R$ 10: {notas_10}")