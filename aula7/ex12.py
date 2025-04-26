# Exercício 12: Compara dois conjuntos de alunos e identifica quais são exclusivos de cada curso,
# quais são comuns a ambos e quais são exclusivos de cada curso.
# Através do método difference() podemos identificar os elementos que estão presentes em um
# conjunto e ausentes em outro. O método intersection() retorna um conjunto com os elementos
# comuns a ambos os conjuntos.
#
# Primeiramente, vamos definir os conjuntos de alunos de cada curso
curso_a = {("Ana", 101), ("Carlos", 102), ("João", 103)}
curso_b = {("João", 103), ("Marina", 104), ("Carlos", 102)}
# Em seguida, vamos identificar os alunos exclusivos de cada curso
# Conjunto de alunos exclusivos do curso A
# Os alunos exclusivos do curso A são aqueles que estão presentes no conjunto curso_a e
# ausentes no conjunto curso_b
exclusivos_a = curso_a.difference(curso_b)
# Conjunto de alunos exclusivos do curso B
# Os alunos exclusivos do curso B são aqueles que estão presentes no conjunto curso_b e
# ausentes no conjunto curso_a
exclusivos_b = curso_b.difference(curso_a)
# Conjunto de alunos comuns a ambos os cursos
# Os alunos comuns a ambos os cursos são aqueles que estão presentes em ambos os conjuntos
ambos_os_cursos = curso_a.intersection(curso_b)
# Imprime os alunos exclusivos de cada curso
print('Alunos apenas no curso A')
# Vamos imprimir os alunos exclusivos do curso A
for  pessoa,matricula in exclusivos_a:
    print(f'{pessoa} ({matricula})')
print()
print('Alunos apenas no curso b')
# Vamos imprimir os alunos exclusivos do curso B
for  pessoa,matricula in exclusivos_b:
    print(f'{pessoa} ({matricula})')
print()
print('Alunos em ambos os cursos')
# Vamos imprimir os alunos comuns a ambos os cursos
for  pessoa,matricula in ambos_os_cursos:
    print(f'{pessoa} ({matricula})')
