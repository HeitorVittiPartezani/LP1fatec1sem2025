li = [0]
ls = [0]
homens = 0
idadehomens = 0
mulheres = 0
idademulheres = 0
for i in range(1,11):
    li.append(int(input(f'Digite a idade do(a) aluno(a) {i}: ')))
    ls.append(str(input(f'Digite o sexo do aluno(a) {i}(M/F): ').upper()))
for c in range(1,11):
    if ls[c] == 'M':
        homens += 1
        idadehomens += li[c]
    else:
        mulheres += 1
        idademulheres += li[c]
mediamulheres = idademulheres/ mulheres
mediahomens = idadehomens / homens
print(f'temos {homens} homens e {mulheres} mulheres')
print(f'as médias de idade são respectivamente {mediahomens} e {mediamulheres} anos')

    
