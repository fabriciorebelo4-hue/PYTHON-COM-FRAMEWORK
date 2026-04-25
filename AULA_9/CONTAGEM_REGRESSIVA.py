import time # Importa a biblioteca de tempo para criar a pausa

contador = int(input("Digite um número inteiro para iniciar a contagem: "))

# O loop 'while' continua rodando enquanto a condição for Verdadeira
while contador >= 0:
    print(contador)
    time.sleep(1) # Pausa a execução do programa por 1 segundo
    contador -= 1 # Reduz 1 do valor do contador (equivalente a contador = contador - 1)

# Quando o contador chegar a -1, o loop acaba e o código segue para cá
print("Fogo!")