# lista de compras do joao
joao = ['arroz', 'feijão', 'macarrão', 'leite']
# lista de compras da maria
maria = ['leite', 'café', 'açúcar', 'arroz']
# lista para armazenar os itens em comum
em_comum = []
# loop para verificar se os itens de joao estao em maria
for i in range(0,len(joao)):
    # se o item de joao estiver em maria, adiciona na lista em_comum
    if joao[i] in maria:
        em_comum.append(joao[i])
# imprime a lista de itens em comum
print(em_comum)