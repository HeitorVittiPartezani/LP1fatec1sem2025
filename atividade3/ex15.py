idade = int(input("Digite a idade da pessoa: "))
cartao_estudante = input("Possui cartão estudante? (S/N): ").upper()

if idade < 6 or idade > 65:
    tarifa = "Grátis"
elif cartao_estudante == "S":
    tarifa = "50% de desconto"
else:
    tarifa = "Tarifa normal"

print(f"A tarifa de ônibus para esta pessoa é: {tarifa}")