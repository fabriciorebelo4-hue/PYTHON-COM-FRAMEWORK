# Leitura dos três lados
l1 = float(input("Digite o 1º lado do triângulo: "))
l2 = float(input("Digite o 2º lado do triângulo: "))
l3 = float(input("Digite o 3º lado do triângulo: "))

# Verifica a condição de existência de um triângulo
if (l1 < l2 + l3) and (l2 < l1 + l3) and (l3 < l1 + l2):
    print("\nOs lados formam um triângulo válido.")
    
    # Classificação do triângulo (Condicionais aninhadas)
    if l1 == l2 and l2 == l3:
        print("Classificação: Equilátero")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("Classificação: Isósceles")
    else:
        print("Classificação: Escaleno")
else:
    print("\nOs lados informados NÃO formam um triângulo.")