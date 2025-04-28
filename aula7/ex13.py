def media(n1,n2):
    """
    Calcula a média entre duas notas.
    """
    media = (n1+n2)/2
    return media

# Dicionário com os alunos e suas notas
boletim = {
 "Ana": (8.0, 7.5),
 "Carlos": (5.0, 6.0),
 "Beatriz": (9.0, 8.5),
 "Daniel": (6.0, 6.5)
}
# Listas para armazenar os alunos aprovados e reprovados
aprovados = []
reprovados = []

print('Média dos alunos:')
for pessoa in boletim:
    # Desempacota as notas do dicionário
    n1,n2 = boletim[pessoa]
    # Calcula a média final
    mediafinal = media(n1,n2)
    # Verifica se o aluno foi aprovado ou reprovado
    if mediafinal >= 7:
        # Adiciona o aluno na lista de aprovados
        aprovados.append([pessoa, mediafinal])
    else:
        # Adiciona o aluno na lista de reprovados
        reprovados.append([pessoa, mediafinal])
    # Imprime a média do aluno
    print(f'{pessoa}: {mediafinal}')
# Ordena as listas de aprovados e reprovados em ordem alfabética
aprovados = sorted(aprovados)
reprovados = sorted(reprovados)
# Imprime os alunos aprovados e reprovados
print()
print('Alunos aprovados:')
for pessoa, nota in aprovados:
    print(pessoa)
print()
print('Alunos reprovados:')
for pessoa, nota in reprovados:
    print(pessoa)
