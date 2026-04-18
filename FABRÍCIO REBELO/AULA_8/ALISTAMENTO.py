ano_nascimento = int(input("Digite o seu ano de nascimento (ex: 2008): "))
sexo = input("Digite o sexo biológico (M para Masculino, F para Feminino): ").strip().upper()
deficiencia = input("Possui alguma deficiência impeditiva? (sim/não): ").strip().lower()

# O ano atual considerado é 2026
ano_atual = 2026
idade = ano_atual - ano_nascimento

print(f"\nSua idade em {ano_atual}: {idade} anos.")

# Prioridade máxima: Deficiência
if deficiencia == "sim":
    print("Situação: Dispensado por condição de saúde.")
# Prioridade 2: Sexo Feminino
elif sexo == "F":
    print("Situação: Alistamento não obrigatório.")
# Se não é deficiente, nem sexo feminino (e assume-se M), vamos para a idade
elif sexo == "M":
    if idade < 18:
        tempo_restante = 18 - idade
        print(f"Situação: Ainda não tem 18 anos. Faltam {tempo_restante} ano(s) para o alistamento.")
    elif idade == 18:
        print("Situação: Aliste-se imediatamente!")
    elif 18 < idade <= 45:
        print("Situação: Já passou do prazo. Regularize sua situação.")
    else:
        print("Situação: Dispensado por idade.")
else:
    print("Dados inválidos. Por favor, reinicie o programa.")