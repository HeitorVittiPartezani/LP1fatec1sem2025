idade = int(input("Digite a idade da pessoa: "))
gestante = input("É gestante? (S/N): ").upper()
deficiente = input("É deficiente? (S/N): ").upper()

if deficiente == "S" or idade >= 60:
    prioridade = "Máxima"
elif gestante == "S":
    prioridade = "Média"
else:
    prioridade = "Normal"

print(f"A prioridade de atendimento é: {prioridade}")