senha_correta = "python123"
tentativas_restantes = 3

# O loop roda enquanto o usuário tiver tentativas disponíveis
while tentativas_restantes > 0:
    senha_digitada = input("Digite a senha: ")

    if senha_digitada == senha_correta:
        print("Acesso liberado")
        break # Senha correta: sai do loop e ignora o resto
    else:
        tentativas_restantes -= 1
        print(f"Senha incorreta. Tentativas restantes: {tentativas_restantes}")

# Se o loop terminar porque a condição 'tentativas_restantes > 0' virou Falsa
if tentativas_restantes == 0:
    print("Conta bloqueada")