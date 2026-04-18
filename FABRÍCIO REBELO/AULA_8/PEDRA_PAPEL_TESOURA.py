# strip() remove espaços em branco acidentais, lower() deixa tudo minúsculo
j1 = input("Jogador 1 (pedra, papel ou tesoura): ").strip().lower()
j2 = input("Jogador 2 (pedra, papel ou tesoura): ").strip().lower()

opcoes_validas = ["pedra", "papel", "tesoura"]

if j1 not in opcoes_validas or j2 not in opcoes_validas:
    print("Jogada inválida! Escolha apenas pedra, papel ou tesoura.")
else:
    if j1 == j2:
        print("Resultado: Empate!")
    elif j1 == "pedra":
        if j2 == "tesoura":
            print("Resultado: Jogador 1 venceu (Pedra quebra Tesoura)")
        else:
            print("Resultado: Jogador 2 venceu (Papel cobre Pedra)")
    elif j1 == "papel":
        if j2 == "pedra":
            print("Resultado: Jogador 1 venceu (Papel cobre Pedra)")
        else:
            print("Resultado: Jogador 2 venceu (Tesoura corta Papel)")
    elif j1 == "tesoura":
        if j2 == "papel":
            print("Resultado: Jogador 1 venceu (Tesoura corta Papel)")
        else:
            print("Resultado: Jogador 2 venceu (Pedra quebra Tesoura)")