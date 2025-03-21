valor_compra = float(input("Digite o valor da compra: "))

if valor_compra > 100:
    frete = 0
    print("Frete grátis!")
else:
    frete = 15
    print(f"O valor do frete é R$ {frete:.2f}")

valor_total = valor_compra + frete
print(f"O valor total da compra é R$ {valor_total:.2f}")