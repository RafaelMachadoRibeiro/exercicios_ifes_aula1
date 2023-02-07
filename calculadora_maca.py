maca = float(input("Digite a quantidade de maças que foi comprada:"))
banana = float(input("Digite quantos quilos de banana foi comprado:"))

preco_maca = 1.3 #Preço Unitário
preco_banana = 5 #Preço KG

valor_gasto_maca = 1.3 * maca
valor_gasto_banana = 5 * banana
valor_total = valor_gasto_maca + valor_gasto_banana

frase1 = "O custo total da compra é R$:"

print(frase1, valor_total)