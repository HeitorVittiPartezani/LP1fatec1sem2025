# lista de compras do joao
joao = ['arroz', 'feijão', 'macarrão', 'leite']
# lista de compras da maria
maria = ['leite', 'café', 'açúcar', 'arroz']
# lista para armazenar os itens que somente maria comprou
somente_maria = []
# loop para verificar se os itens de maria estao em joao
for i in range(0,len(maria)):
    # se o item de maria nao estiver em joao, adiciona na lista somente_maria
    if maria[i] not in joao:
        somente_maria.append(maria[i])
# imprime a lista de itens que somente maria comprou
print(f'Maria comprou {somente_maria}, e joão não')