frase1 = "Olá, esse programa foi feito com objetivo de calcular quantos azulejos são necessários para colocar na parede."
frase2 = "São necessários:"
frase3 = "azulejos para completar a parede."

print(frase1)

altura_parede = float(input("Digite a altura da parede:"))
largura_parede = float(input("Digite a largura da parede:"))

altura_azulejo = float(input("Digite a altura do azulejo:"))
largura_azulejo = float(input("Digite a largura do azulejo:"))

area_parede = altura_parede * largura_parede
area_azulejo = altura_azulejo * largura_azulejo

quantidade_azulejo = area_parede // area_azulejo

print(frase2,quantidade_azulejo,frase3)