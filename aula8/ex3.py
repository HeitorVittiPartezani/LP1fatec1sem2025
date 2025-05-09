#ex3
frase = str(input('Digite uma frase: ').lower())
procura = str(input('Digite a palavra  que deseja procurar: ').lower())
if procura in frase:
    print(f'A palavra {procura} está na frase, na posição {frase.find(procura)}')
else:
    print(f'A palavra {procura} não está na frase')