# dicionário com os valores romanos e seus correspondentes em numeros inteiros
romanos = {
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1,
}
# Entrada do usuario
n = input = int(input('Insirea um número para ser convertido em algarismos romanos: '))
resposta = ''

# loop para percorrer o dicionário e verificar se o valor atual é menor ou igual ao input do usuário
for key,item in romanos.items():
    # verifica se o valor atual do dicionário é menor ou igual ao input do usuário
    while item <= n:
        # subtrai o valor atual do input do usuário
        n -= item  
        # concatena o valor atual na resposta
        resposta += key  

# imprime a resposta
print(f'{input} em algarismos romanos é igual a: {resposta}')