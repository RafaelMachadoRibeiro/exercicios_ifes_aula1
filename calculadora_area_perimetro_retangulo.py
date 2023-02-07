frase1 = "A área do retângulo é:"
frase2 = "O perímetro do retângulo é:"
frase3 = "m2"

altura_retangulo = float(input("Digite a altura do retângulo:"))
base_retangulo = float(input("Digite a base do retângulo:"))

area_retangulo = base_retangulo * altura_retangulo
perimetro_retangulo = (2 * base_retangulo) + (2 * altura_retangulo)

print(frase1,area_retangulo,frase3)
print(frase2,perimetro_retangulo,frase3)