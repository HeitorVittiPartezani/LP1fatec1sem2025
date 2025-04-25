# imprime os dias da semana em uma tupla
dias = ("segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo")
# converte a tupla em um conjunto (set) com o objetivo de não repetir um mesmo dia na tupla acima
dias_unicos = set(dias)
# imprime o conjunto de dias evitando as repetições indesejadas(se houver)
print(dias_unicos)