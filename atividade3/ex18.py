usuario_correto = "usuario"
senha_correta = "senha123"
tentativas_maximas = 3
tentativas_realizadas = 0

while tentativas_realizadas < tentativas_maximas:
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")
    tentativas_realizadas += 1

    if usuario == usuario_correto and senha == senha_correta:
        print("Login bem-sucedido")
        break
    else:
        print("Usuário ou senha incorretos")
        if tentativas_realizadas < tentativas_maximas:
            print(f"Você tem mais {tentativas_maximas - tentativas_realizadas} tentativas.")
        else:
            print("Acesso bloqueado após 3 tentativas.")