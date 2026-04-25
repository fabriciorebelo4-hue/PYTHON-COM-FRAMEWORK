import random 

contagem = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

for _ in range(100):

    face_sorteada = random.randint(1, 6)
    
    contagem[face_sorteada] += 1

print("Resultado após 100 lançamentos:")

for face, quantidade in contagem.items():
    print(f"Face {face} caiu {quantidade} vezes")