n = int(input())

zastavky = set()

for i in range(n):
    trasa = input()[1:].split('/')
    cesta = ""
    momentalna_trasa = []
    for zastavka in trasa:
        momentalna_trasa.append(zastavka)
        zastavky.add(tuple(momentalna_trasa))

print(len(zastavky))

