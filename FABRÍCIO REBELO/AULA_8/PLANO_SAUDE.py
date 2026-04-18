idade = int(input("Digite a idade do cliente: "))
print("\nOpções de Plano:\n- basico\n- standard\n- premium")
tipo_plano = input("Digite o tipo de plano escolhido: ").strip().lower()

valor_base = 0.0
plano_valido = True

# Definição do valor base dependendo do plano escolhido
if tipo_plano == "basico":
    valor_base = 100 + (idade * 2)
elif tipo_plano == "standard":
    valor_base = 150 + (idade * 3)
elif tipo_plano == "premium":
    valor_base = 200 + (idade * 5)
else:
    plano_valido = False
    print("\nPlano inválido! Tente novamente.")

# Só calcula e mostra o total se o plano digitado existir
if plano_valido:
    # Regra de acréscimo para idosos
    if idade > 60:
        print("\nAcréscimo de 10% aplicado (maior de 60 anos).")
        valor_total = valor_base * 1.10 # Multiplicar por 1.10 é o mesmo que somar 10%
    else:
        valor_total = valor_base
        
    print(f"Valor mensal do plano {tipo_plano.capitalize()}: R$ {valor_total:.2f}")