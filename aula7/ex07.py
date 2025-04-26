# Exercício 7: imprime o preço do leite e do feijão com 2 casas decimais
# utilizando uma tabela (dicionário) e strings de formatação
tabela = {
 "Arroz": 24.90,
 "Feijão": 8.50,
 "Leite": 4.80,
 "Açúcar": 3.90
}

# imprime o preço do leite e do feijão com 2 casas decimais
# utilizando strings de formatação
print(f'Opreço do leite é R${tabela["Leite"]:.2f} e o preço do feijão éR${tabela["Feijão"]:.2f}')
