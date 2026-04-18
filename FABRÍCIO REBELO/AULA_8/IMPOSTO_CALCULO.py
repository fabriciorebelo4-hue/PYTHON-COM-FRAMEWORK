salario_bruto = float(input("Digite o salário bruto (R$): "))

# 1. Cálculo do INSS (11% limitado a R$ 1.500,00)
# A função min() pega o menor valor entre o desconto real e o teto.
inss = min(salario_bruto * 0.11, 1500.00)

# 2. Cálculo do IRRF (Progressivo conforme as faixas do enunciado)
irrf = 0.0

if salario_bruto <= 2500:
    irrf = 0.0
elif salario_bruto <= 3500:
    irrf = (salario_bruto - 2500) * 0.075
elif salario_bruto <= 5000:
    # Máximo da faixa anterior + excedente desta faixa
    irrf = (1000 * 0.075) + ((salario_bruto - 3500) * 0.15)
else:
    # Máximo da 1ª faixa + máximo da 2ª faixa + excedente final
    irrf = (1000 * 0.075) + (1500 * 0.15) + ((salario_bruto - 5000) * 0.275)

# 3. Cálculo final
salario_liquido = salario_bruto - inss - irrf

print("\n--- RESUMO DO CONTRACHEQUE ---")
print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"Desconto INSS: R$ {inss:.2f}")
print(f"Desconto IRRF: R$ {irrf:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")