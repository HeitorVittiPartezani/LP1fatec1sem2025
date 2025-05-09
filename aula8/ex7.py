#ex7
frase = str(input('Digite uma frase: ').lower())
inverso = frase[::-1]
print(inverso)
if frase == inverso:
  print('A frase é um palíndromo')
else:
  print('A frase não é um palíndromo')