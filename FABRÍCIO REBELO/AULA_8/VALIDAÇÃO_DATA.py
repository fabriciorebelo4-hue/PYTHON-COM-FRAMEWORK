dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês (1 a 12): "))
ano = int(input("Digite o ano: "))

data_valida = False

# Verifica se o mês está no intervalo correto
if 1 <= mes <= 12:
    # Mapeia os meses com 31 dias
    if mes in (1, 3, 5, 7, 8, 10, 12):
        if 1 <= dia <= 31:
            data_valida = True
            
    # Mapeia os meses com 30 dias
    elif mes in (4, 6, 9, 11):
        if 1 <= dia <= 30:
            data_valida = True
            
    # Mapeia Fevereiro (Mês 2) e a lógica do ano bissexto
    elif mes == 2:
        # Regra do ano bissexto: divisível por 400 OU (divisível por 4 E não por 100)
        bissexto = (ano % 400 == 0) or ((ano % 4 == 0) and (ano % 100 != 0))
        
        if bissexto and (1 <= dia <= 29):
            data_valida = True
        elif not bissexto and (1 <= dia <= 28):
            data_valida = True

if data_valida:
    # Formatação com zero à esquerda (ex: 05/09/2023)
    print(f"\nA data {dia:02d}/{mes:02d}/{ano} é VÁLIDA.")
else:
    print("\nA data informada é INVÁLIDA.")