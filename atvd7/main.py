palavra = input("digite uma palavra:")
vogais = 0
for caractere in palavra:
    if caractere.lower() in "aeiou":
        vogais += 1
print(f"número de vogais: {vogais}")