salario_bruto = float(input("Digite o salário bruto: ")) #

if salario_bruto <= 2112.00:
    imposto = 0.00
    parcela_deduzir = 0.00
elif 2112.01 <= salario_bruto <= 2826.65:
    imposto = 0.075
    parcela_deduzir = 158.40
elif 2826.66 <= salario_bruto <= 3751.05:
    imposto = 0.15
    parcela_deduzir = 370.40
elif 3751.06 <= salario_bruto <= 4664.68:
    imposto = 0.225
    parcela_deduzir = 651.73
else:
    imposto = 0.275
    parcela_deduzir = 884.96

imposto_a_pagar = (salario_bruto * imposto) - parcela_deduzir

if imposto == 0.00:
    print("Não há imposto a pagar.")
else:
    print(f"O imposto a pagar é: R$ {imposto_a_pagar:.2f}") #