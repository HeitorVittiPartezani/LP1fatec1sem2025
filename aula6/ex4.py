idade = int(input("Digite a idade do usuário: ")) #

if idade < 14:
    condicao_festa = "Não pode entrar"
    condicao_beber = "Não Pode Beber"
elif idade < 18:
    condicao_festa = "Pode com acompanhamento dos pais"
    condicao_beber = "Não Pode Beber"
else:
    condicao_festa = "Pode Entrar"
    condicao_beber = "Pode Beber"

print(f"Condição para entrar na festa: {condicao_festa}") #
print(f"Condição para beber: {condicao_beber}") #