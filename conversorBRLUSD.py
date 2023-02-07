frase1 = "Olá, quantos reais você deseja converter para dolar?"
frase2 = "R$:"
frase3 = "convertido para o dolar é igual a US$:"

valor_real = float(input("Digite o valor:"))
valor_dolar = 3.12
resultado = valor_real / valor_dolar

print(frase1)
print(frase2,valor_real,frase3,resultado)