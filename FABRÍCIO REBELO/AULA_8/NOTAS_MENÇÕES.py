# Solicita a nota ao usuário e converte para número decimal (float)
nota = float(input("Digite a nota do aluno (0 a 10): "))

# Estrutura condicional para verificar as faixas de notas
if nota >= 9 and nota <= 10:
    print("Menção: Excelente")
elif nota >= 7 and nota < 9:
    print("Menção: Bom")
elif nota >= 5 and nota < 7:
    print("Menção: Regular")
elif nota >= 0 and nota < 5:
    print("Menção: Insuficiente")
else:
    print("Nota inválida! Por favor, insira um valor entre 0 e 10.")