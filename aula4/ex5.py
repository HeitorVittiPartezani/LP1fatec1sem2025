try:
    # Solicita um número ao usuário, conforme as regras 
    n = int(input("Digite um número para calcular o fatorial: "))

    # Garante que o número é positivo 
    if n < 0:
        print("Erro: O número deve ser um inteiro não negativo (n >= 0).")
    else:
        # --- Cálculo com o laço for ---
        # No laço for, utiliza-se range() para iterar de 1 até n [cite: 6]
        fatorial_for = 1
        # O fatorial de 0 é 1 
        if n > 0:
            for i in range(1, n + 1):
                fatorial_for *= i
        
        # Exibe o resultado no formato esperado [cite: 5]
        print(f"Usando for: {n}! = {fatorial_for}")

        # --- Cálculo com o laço while ---
        # No laço while, são usadas variáveis auxiliares [cite: 6]
        fatorial_while = 1
        contador_while = 1
        
        if n > 0:
            while contador_while <= n:
                fatorial_while *= contador_while
                contador_while += 1
        
        # Exibe o resultado no formato esperado [cite: 5]
        print(f"Usando while: {n}! = {fatorial_while}")

except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")