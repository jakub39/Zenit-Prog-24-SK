n = int(input())

vysledok = []

for _ in range(n):
    x = int(input())
    
    nasiel = False
    for i in range(x // 5 + 1):
        for j in range((x - 5 * i) // 7 + 1):
            if (x - 5 * i - 7 * j) % 13 == 0:
                nasiel = True
                break
        if nasiel:
            break

    vysledok.append("ANO" if nasiel else "NIE")

for i in vysledok:
    print(i)
