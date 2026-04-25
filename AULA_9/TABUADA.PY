# Solicita um número ao usuário e converte o texto digitado para inteiro (int)
numero = int(input("Digite um número inteiro positivo: "))

print(f"\nTabuada do {numero}:")

# O loop 'for' vai iterar de 1 até 10. 
# Obs: O range(1, 11) para no 10, pois o último número é exclusivo.
for i in range(1, 11):
    resultado = numero * i
    # Exibe a linha da tabuada formatada (Ex: 7 x 1 = 7)
    print(f"{numero} x {i} = {resultado}")