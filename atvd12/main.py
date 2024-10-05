total = 0

for i in range(5):
    preco = float(input(f"Digite o preço do produto {i + 1}: "))
    total += preco

if total > 100:
    total *= 0.9  

print(f"O total a pagar é: R$ {total:.2f}")


