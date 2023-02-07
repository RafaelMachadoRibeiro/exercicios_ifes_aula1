frase1 = "O seu IMC é: "

peso = float(input("Digite seu peso:"))
altura = float(input("Digite sua altura em metros:"))

imc = peso / (altura ** 2)

print(frase1, imc)