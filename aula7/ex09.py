# Exercício 9: imprime o nome e preço dos produtos em um carrinho
# utilizando um dicionário e 2 métodos diferentes de loop
compras = {
 "Sabonete": 2.50,
 "Shampoo": 15.00,
 "Condicionador": 16.50
}
# loop para imprimir os produtos do carrinho
for i in compras:
    # imprime o nome e preço do produto com 2 casas decimais
    print(f'{i}: R${compras[i]:.2f}')
print()
print('Metódo 2')
print()
# Metódo 2
for item,preço in compras.items():
    # imprime o nome e preço do produto com 2 casas decimais
    print(f'{item}: R${preço:.2f}')
    
# Neste exercício, estamos utilizando um dicionário para armazenar as informações do carrinho de compras.
# O dicionário tem como chave o nome do produto e como valor o preço do produto.
# No primeiro loop, estamos acessando o valor do dicionário com a chave i.
# No segundo loop, estamos acessando o valor do dicionário com o método items(), que retorna uma lista de tuplas com o nome e o preço do produto.