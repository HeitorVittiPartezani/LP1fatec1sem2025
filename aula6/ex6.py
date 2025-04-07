idade_escoteiro = int(input("Digite a idade do escoteiro: ")) #

if idade_escoteiro < 6:
    print("Idade inválida.")
else:
    if 6 <= idade_escoteiro <= 10:
        categoria = "Lobinho"
    elif 11 <= idade_escoteiro <= 14:
        categoria = "Escoteiro"
    elif 15 <= idade_escoteiro <= 17:
        categoria = "Sênior"
    elif 18 <= idade_escoteiro <= 21:
        categoria = "Pioneiro"
    else:
        categoria = "Líder"

    print(f"Categoria: {categoria}") #