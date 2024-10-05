positivos = 0
negativos = 0

for i in range(10):
    numero = float(input(f"Digite o {i+1}º número: ")) 
    if numero == 0:
        print("Número 0 inserido, encerrando o loop.")
        break  
    elif numero > 0:
        positivos += 1  
    else:
        negativos += 1 
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")
