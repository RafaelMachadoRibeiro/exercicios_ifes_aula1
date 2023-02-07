valor_carro = float(input("Digite o valor de fábrica do carro:"))
percentual_distribuidor = valor_carro * 0.28
percentual_imposto = valor_carro * 0.45

valor_final_carro = percentual_distribuidor + percentual_imposto + valor_carro

frase1 = "O preço do carro vendido ao consumidor é:"

print(frase1, valor_final_carro)