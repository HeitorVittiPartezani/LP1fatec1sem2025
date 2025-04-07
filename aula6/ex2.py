dia = int(input("Digite o dia: ")) #
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

if 1 <= mes <= 12 and 1 <= dia <= 31:
    meses = {
        1: "janeiro",
        2: "fevereiro",
        3: "março",
        4: "abril",
        5: "maio",
        6: "junho",
        7: "julho",
        8: "agosto",
        9: "setembro",
        10: "outubro",
        11: "novembro",
        12: "dezembro"
    }
    nome_mes = meses.get(mes)
    print(f"{dia:02d} de {nome_mes} de {ano:04d}") #
else:
    print("Data inválida.")