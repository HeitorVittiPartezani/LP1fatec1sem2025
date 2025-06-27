# Solicita um número ao usuário
try:
    numero = int(input("Digite um número inteiro: "))
    soma_pares = 0

    # Itera de 1 até o número informado
    for i in range(1, numero + 1):
        # Verifica se o número é par
        if i % 2 == 0:
            soma_pares += i

    print(f"A soma de todos os números pares de 1 até {numero} é: {soma_pares}")

except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")