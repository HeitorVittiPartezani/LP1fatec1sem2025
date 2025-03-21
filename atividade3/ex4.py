idade = int(input("Digite sua idade: "))

if idade < 12 or idade > 60:
    preco_ingresso = 15.00
else:
    preco_ingresso = 30.00

print(f"O preço do ingresso é R$ {preco_ingresso:.2f}")