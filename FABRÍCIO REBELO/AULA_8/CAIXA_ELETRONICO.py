valor = int(input("Qual valor deseja sacar? (Apenas notas de 50, 20, 10 e 5): R$ "))

# Validação das regras do enunciado
if valor < 10 or valor > 1000:
    print("Erro: O valor do saque deve estar entre R$ 10 e R$ 1000.")
elif valor % 5 != 0:
    print("Erro: O valor deve ser múltiplo de 5, pois não temos moedas.")
else:
    print(f"\n--- Processando o saque de R$ {valor} ---")
    
    # // Divisão Inteira (descobre a quantidade de notas)
    # %= Resto da divisão (descobre o que sobrou para as próximas notas)
    
    notas_50 = valor // 50
    valor = valor % 50 
    
    notas_20 = valor // 20
    valor %= 20 # Forma simplificada de escrever valor = valor % 20
    
    notas_10 = valor // 10
    valor %= 10
    
    notas_5 = valor // 5
    valor %= 5
    
    # Exibição dos resultados (só mostra as notas que foram usadas)
    if notas_50 > 0:
        print(f"{notas_50} nota(s) de R$ 50")
    if notas_20 > 0:
        print(f"{notas_20} nota(s) de R$ 20")
    if notas_10 > 0:
        print(f"{notas_10} nota(s) de R$ 10")
    if notas_5 > 0:
        print(f"{notas_5} nota(s) de R$ 5")