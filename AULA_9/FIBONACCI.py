n = int(input("Quantos termos da sequência de Fibonacci você quer gerar? "))
t1 = 0
t2 = 1

print("\nSequência de Fibonacci:")
if n == 1:
    print(t1)
elif n >= 2:
    print(t1)
    print(t2)

    for _ in range(3, n + 1):
        proximo_termo = t1 + t2
        print(proximo_termo)

        t1 = t2
        t2 = proximo_termo