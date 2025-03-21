import random

numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    tentativa = int(input("Tente adivinhar o número secreto (entre 1 e 100): "))
    tentativas += 1

    if tentativa > numero_secreto:
        print("Muito alto!")
    elif tentativa < numero_secreto:
        print("Muito baixo!")
    else:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break