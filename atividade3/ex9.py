salario = float(input("Digite seu salário atual: "))

if salario < 2000:
    bonus = salario * 0.20
elif 2000 <= salario <= 5000:
    bonus = salario * 0.10
else:
    bonus = salario * 0.05

salario_final = salario + bonus
print(f"Seu bônus é de R$ {bonus:.2f} e o salário final é R$ {salario_final:.2f}")