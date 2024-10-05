for i in range(1, 21):
    if i == 15:
        print("Número 15 encontrado, loop encerrado.")
        break
    elif i % 2 == 0:
        print(f"{i} é par.")
    else:
        print(f"{i} é ímpar.")
