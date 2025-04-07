n = int(input('Digite um numero para calcular seu fatorial: '))
resultado = 1
for i in range(1, n+1):
    resultado *= i
print(f'o fatorial de {n} é {resultado}')