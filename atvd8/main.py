nota1= float(input("insira nota 1:"))
nota2= float(input("insira nota 2:"))
nota3= float(input("insira nota 3:"))
nota4= float(input("insira nota 4:"))
nota5= float(input("insira nota 5:"))

soma_notas = nota1 + nota2 + nota3 + nota4 + nota5
media = soma_notas / 5

print(f"A média das notas é: {media:.2f}")

if media >= 6:
    print("Classificação: Aprovado")
else:
    print("Classificação: Reprovado")