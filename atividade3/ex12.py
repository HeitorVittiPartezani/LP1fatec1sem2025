temperatura = float(input("Digite a temperatura em Celsius: "))

if temperatura <= 15:
    print("Frio")
elif 16 <= temperatura <= 25:
    print("Agradável")
else:
    print("Quente")