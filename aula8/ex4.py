#ex4
frase = str(input('Digite uma frase: ').lower())
if 'bobo' in frase:
  frase2 = frase.replace('bobo', '***')
  print(frase2)
else:
  print(frase)