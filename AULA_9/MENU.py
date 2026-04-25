import datetime # Necessário para pegar a data e hora do sistema

while True:
    # Interface do Menu
    print("\n--- Menu Interativo ---")
    print("1 - Exibir mensagem 'Olá!'")
    print("2 - Exibir a data/hora atual")
    print("3 - Sair")

    escolha = input("Escolha uma opção (1-3): ")

    if escolha == '1':
        print("\n-> Olá! Como posso te ajudar hoje?")
        
    elif escolha == '2':
        agora = datetime.datetime.now() # Captura a data e hora de agora
        # Formata o objeto de tempo para um formato legível (Dia/Mês/Ano Hora:Minuto:Segundo)
        print("\n-> Data e hora atuais:", agora.strftime("%d/%m/%Y %H:%M:%S"))
        
    elif escolha == '3':
        print("\n-> Encerrando o sistema. Até logo!")
        break # Quebra o 'while True' e finaliza o script
        
    else:
        print("\n-> Opção inválida. Digite 1, 2 ou 3.")