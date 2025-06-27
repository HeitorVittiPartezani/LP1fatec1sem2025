try:
    valor_saque = int(input("Digite o valor que deseja sacar: R$ "))
    valor_restante = valor_saque
    notas = [100, 50, 20, 10, 5, 2, 1]

    print(f"\nPara sacar R$ {valor_saque}, você receberá:")

    for nota in notas:
        # Calcula a quantidade de notas necessárias
        quantidade_notas = valor_restante // nota
        
        # Se a quantidade for maior que zero, exibe o resultado
        if quantidade_notas > 0:
            if nota > 1:
                print(f"- {quantidade_notas} nota(s) de R$ {nota}")
            else:
                print(f"- {quantidade_notas} moeda(s) de R$ {nota}")
        
        # Atualiza o valor restante
        valor_restante %= nota

except ValueError:
    print("Entrada inválida. Por favor, digite um valor inteiro.")