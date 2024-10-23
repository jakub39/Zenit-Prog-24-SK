def min_shifts(n, lights):
    shifts = 0  # Počet šícht, ktoré sú potrebné
    for x in range(1, n + 1):
        if lights[x - 1] > 0:
            # Kontrola, či existujú vozy 2x a 2x+1
            if 2 * x <= n and 2 * x + 1 <= n:
                # Vykonáme potrebný počet šícht
                count = min(lights[x - 1], lights[2 * x - 1], lights[2 * x])  # Minimálny počet šícht
                shifts += count
                # Znížime počet svetielok v jednotlivých vozňoch
                lights[x - 1] -= count
                lights[2 * x - 1] -= count
                lights[2 * x] -= count
            else:
                return -1  # Ak nie je možné vykonať operáciu, vrátime -1
    return shifts

# Načítame vstup
n = int(input())
lights = list(map(int, input().split()))

# Výpis výsledku
print(min_shifts(n, lights))
