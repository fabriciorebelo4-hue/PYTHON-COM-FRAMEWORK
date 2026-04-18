peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# Cálculo do IMC: Peso dividido pela altura ao quadrado
imc = peso / (altura ** 2)

print(f"\nSeu IMC é: {imc:.2f}")

# Classificação
if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Classificação: Peso normal")
elif 25 <= imc < 30:
    print("Classificação: Sobrepeso")
else: # Qualquer valor >= 30 cai aqui
    print("Classificação: Obesidade")