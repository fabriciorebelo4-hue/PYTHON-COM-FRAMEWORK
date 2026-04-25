numero = int(input("Digite um número inteiro positivo: "))

# Números menores ou iguais a 1 não são primos por definição
if numero <= 1:
    print(f"{numero} não é primo.")
else:
    eh_primo = True
    
    # Testamos se o número divide por qualquer valor entre 2 e a metade dele
    for i in range(2, (numero // 2) + 1):
        if numero % i == 0: # O resto da divisão por 'i' é zero?
            eh_primo = False
            break # Encontramos um divisor! Não precisa continuar testando

    if eh_primo:
        print(f"{numero} é um número primo!")
    else:
        print(f"{numero} não é primo.")