nota_lab = float(input("Digite a nota do trabalho de laboratório: ")) #
nota_sem = float(input("Digite a nota da avaliação semestral: "))
nota_exame = float(input("Digite a nota do exame final: "))

media_ponderada = (nota_lab * 2 + nota_sem * 3 + nota_exame * 5) / 10

if 8.0 <= media_ponderada <= 10.0:
    conceito = "A"
elif 7.0 <= media_ponderada < 8.0:
    conceito = "B"
elif 6.0 <= media_ponderada < 7.0:
    conceito = "C"
elif 5.0 <= media_ponderada < 6.0:
    conceito = "D"
else:
    conceito = "E"

print(f"Média Ponderada: {media_ponderada:.1f}") #
print(f"Conceito: {conceito}")