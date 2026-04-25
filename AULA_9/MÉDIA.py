soma_notas = 0
quantidade_notas = 0

# Inicia um loop infinito, que só será interrompido pelo 'break'
while True:
    nota = float(input("Digite uma nota de 0 a 10 (ou -1 para sair): "))

    # Condição de saída principal
    if nota == -1:
        break 

    # Verifica se a nota é inválida
    if nota < 0 or nota > 10:
        print("Nota inválida. Ignorando...")
        continue # O 'continue' pula tudo que está abaixo e volta ao início do 'while'

    # Se a nota passou pela validação acima, ela é registrada
    soma_notas += nota
    quantidade_notas += 1

# Exibe o resultado, mas primeiro garante que não haverá divisão por zero
if quantidade_notas > 0:
    media = soma_notas / quantidade_notas
    print(f"\nA média das {quantidade_notas} notas válidas é: {media:.2f}")
else:
    print("\nNenhuma nota válida foi inserida.")