salario_bruto = float(input("Digite o salário bruto: "))

if salario_bruto <= 1900:
    aliquota = 0
    imposto = 0
elif 1900 < salario_bruto <= 2800:
    aliquota = 0.075
    imposto = salario_bruto * aliquota
elif 2800 < salario_bruto <= 3700:
    aliquota = 0.15
    imposto = salario_bruto * aliquota
elif 3700 < salario_bruto <= 4600:
    aliquota = 0.225
    imposto = salario_bruto * aliquota
else:
    aliquota = 0.275
    imposto = salario_bruto * aliquota

print(f"Salário bruto: R$ {salario_bruto:.2f}")
print(f"Alíquota do IR: {aliquota * 100:.1f}%")
print(f"Imposto de Renda: R$ {imposto:.2f}")