# Exercício 6: imprime o nome e preço dos produtos em um carrinho
# utilizando uma tupla de tuplas e um loop for
carrinho = (
 ("Arroz", 24.90),
 ("Feijão", 8.50),
 ("Leite", 4.80),
)
# loop para imprimir os produtos do carrinho
for i in range(0,len(carrinho)):
    # desempacota a tupla em variáveis separadas
    nome = carrinho[i][0]
    preço = carrinho[i][1]
    # imprime o produto e seu preço com 2 casas decimais
    print(f'Produto: {nome} | Preço: {preço:.2f}')