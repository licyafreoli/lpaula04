positivos= 0
negativos= 0

for i in range(10):
    numero = float(input(f"digite o {i+1}° número:"))
    if numero >0:
     positivos +=1
    elif numero <0:
     negativos +=1
print(f"números positivos: {positivos}")
print(f"números negativos: {negativos}")