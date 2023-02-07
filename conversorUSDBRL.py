frase1 = "Olá, quantos dolares você deseja converter para real?"
frase2 = "US$:"
frase3 = "convertido para real, é igual a R$:"

usd = float(input("Digite o valor em US$:"))
valor_brl = 3.12
resultado = usd * valor_brl

print(frase1)
print(frase2,usd,frase3,resultado)