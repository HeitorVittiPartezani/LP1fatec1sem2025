# tupla com 2 itens, nome do produto e preço do produto
produto = ("Arroz 5kg", 24.90)
nome = produto[0]  # nome do produto
preço = produto[1]  # preço do produto
# imprime o nome e preço do produto com 2 casas decimais
print(f'O produto {nome} custa R${preço:.2f}')
