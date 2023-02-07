frase1 = "O volume da esfera é:"
frase2 = "A área da esfera é:"

raio = float(input("Digite o raio da esfera:"))
pi = 3.14
condicional_volume = 4/3

volume = condicional_volume * pi * (raio ** 3)
area = 4 * pi * (raio ** 2)

print(frase1,volume)
print(frase2, area)