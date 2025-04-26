# Exercício 10: some os 3 maiores e os 3 menores números 
# e imprime os resultados
numeros = [10, 3, 5, 7, 2, 8, 12]
# ordena a lista em ordem crescente
numerosmenor = sorted(numeros)
# ordena a lista em ordem decrescente
numerosmaior = numerosmenor[::-1]
# variáveis para armazenar os resultados
resultadomenor = 0
resultadomaior = 0
# loop para somar os 3 primeiros e os 3 últimos números
for i in range(0,3):
    resultadomenor += numerosmenor[i]
    resultadomaior += numerosmaior[i]
# imprime os resultados
print(f'{resultadomenor} | {resultadomaior}')