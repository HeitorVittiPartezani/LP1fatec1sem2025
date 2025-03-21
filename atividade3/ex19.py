idade_atleta = int(input("Digite a idade do atleta: "))

if idade_atleta <= 12:
    categoria = "Infantil"
elif 13 <= idade_atleta <= 17:
    categoria = "Juvenil"
elif 18 <= idade_atleta <= 40:
    categoria = "Adulto"
else:
    categoria = "Veterano"

print(f"O atleta se classifica na categoria: {categoria}")