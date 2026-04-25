numero = int(input("Digite um número inteiro positivo: "))
soma_digitos = 0

temp = numero

while temp > 0:
    ultimo_digito = temp % 10     
    soma_digitos += ultimo_digito 
    temp = temp // 10             
lista = [soma_digitos]
print(f"A soma dos dígitos de {numero}  {lista} é {soma_digitos}.")