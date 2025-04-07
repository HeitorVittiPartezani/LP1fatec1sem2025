l1 = []
l2 = []
for i in range(1,7):
    l1.append(int(input(f'Digite a primeira nota do aluno {i}: ')))
    l2.append(int(input(f'Digite a segunda nota do aluno {i}: ' )))
for c in range(1,7):
    media = (l1[c-1]+l2[c-1])/2
    if media <= 3:
        print(f'aluno {c} reprovado')
    elif media > 3 and media <= 7:
        print(f'aluno {c} encaminhado para exame')
    elif media > 7:
        print(f'aluno {c} aprovado')