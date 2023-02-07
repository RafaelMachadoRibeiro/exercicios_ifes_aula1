numero_de_carros = float(input("Digite o número de carros vendido esse mês:"))
valor_total_vendas = float(input("Digite o valor total de vendas feitas esse mês:"))
salario_fixo = float(input("Digite o salário fixo do vendedor:"))

comissao_vendedor = valor_total_vendas * 0.05
salario_final = salario_fixo + comissao_vendedor * numero_de_carros + ((5 * valor_total_vendas) / 100)

frase1 = "O salário final do vendedor é R$:"

print(frase1,salario_final)