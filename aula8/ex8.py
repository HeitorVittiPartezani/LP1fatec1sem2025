#ex8
senha = str(input('Digite sua senha: '))
if len(senha) >= 8 and senha.isalnum() == False:
  print('Senha aceita')
elif len(senha) >= 8 and senha.isalnum() == True:
  print('Senha inválida,é necessário pelo menos um caractere especial')
elif  senha.isalnum() == False:
  print('Senha inválida, é necessário pelo menos 8 caracteres')
else:
  print('Senha inválida, é necessário pelo menos 8 caracteres e um caractere especial')