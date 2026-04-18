n1 = float(input("Digite a nota N1: "))
n2 = float(input("Digite a nota N2: "))

media = (n1 + n2) / 2
print(f"Média Parcial: {media:.1f}")

if media >= 7:
    print("Situação: Aprovado direto!")
elif media < 4:
    print("Situação: Reprovado direto!")
else:
    print("Situação: Em Recuperação.")
    # Só solicita a nota de recuperação se for necessário
    nr = float(input("Digite a nota da Recuperação (NR): "))
    
    media_final = (media + nr) / 2
    print(f"Média Final: {media_final:.1f}")
    
    if media_final >= 5:
        print("Situação Final: Aprovado na recuperação!")
    else:
        print("Situação Final: Reprovado na recuperação.")