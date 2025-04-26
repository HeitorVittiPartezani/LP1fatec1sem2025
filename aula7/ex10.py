# Exercício 10: some os 4 maiores e os 4 menores números 
# e imprime os resultados
numeros = [1, 3, 5, 7, 9]
# ordena a lista em ordem crescente
numerosmenor = sorted(numeros)
# ordena a lista em ordem decrescente
numerosmaior = numerosmenor[::-1]
# variáveis para armazenar os resultados
resultadomenor = 0
resultadomaior = 0
# loop para somar os 4 primeiros e os 4 últimos números
for i in range(0,4):
    resultadomenor += numerosmenor[i]
    resultadomaior += numerosmaior[i]
# imprime os resultados
print(f'{resultadomenor} | {resultadomaior}')