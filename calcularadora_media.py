P1 = float(input("Digite a nota da P1:"))
P2 = float(input("Digite a nota da P2:"))
Ativ = float(input("Digite a nota da atividade:"))

fator_med = (4 * P1) + (3 * P2) + (2 * Ativ)
media = fator_med / 9

frase1 = "A média do semestre:"
print(frase1, media)