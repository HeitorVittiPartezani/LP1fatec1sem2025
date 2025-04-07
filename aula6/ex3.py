codigo_cargo = int(input("Digite o código do cargo (1 a 5): ")) #

if codigo_cargo == 1:
    cargo = "Escriturário"
    salario_base = 2500.00
    beneficios = 300.00
    imposto = 0.08
elif codigo_cargo == 2:
    cargo = "Secretário"
    salario_base = 3200.00
    beneficios = 450.00
    imposto = 0.10
elif codigo_cargo == 3:
    cargo = "Caixa"
    salario_base = 3800.00
    beneficios = 600.00
    imposto = 0.12
elif codigo_cargo == 4:
    cargo = "Gerente"
    salario_base = 7500.00
    beneficios = 1000.00
    imposto = 0.15
elif codigo_cargo == 5:
    cargo = "Diretor"
    salario_base = 12000.00
    beneficios = 2000.00
    imposto = 0.20
else:
    print("Código de cargo inválido.")
    exit()

salario_liquido = salario_base + beneficios - (salario_base * imposto) #

print(f"Cargo: {cargo}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")