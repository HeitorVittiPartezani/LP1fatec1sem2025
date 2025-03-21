nota = float(input("Digite a nota do aluno (0 a 10): "))

if 9 <= nota <= 10:
    conceito = "A"
elif 7 <= nota < 9:
    conceito = "B"
elif 5 <= nota < 7:
    conceito = "C"
elif 3 <= nota < 5:
    conceito = "D"
elif 0 <= nota < 3:
    conceito = "E"
else:
    conceito = "Nota inválida"

print(f"O conceito para a nota {nota} é: {conceito}")