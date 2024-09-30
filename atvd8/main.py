soma_notas = 0

for i in range(5):
    nota = float(input(f"Digite a nota {i + 1}: "))
    soma_notas += nota
media = soma_notas / 5

print(f"A média das notas é: {media:.2f}")

if media >= 6:
    print("Classificação: Aprovado")
else:
    print("Classificação: Reprovado")