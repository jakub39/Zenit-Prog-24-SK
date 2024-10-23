def otoč_a_skontroluj(cislo_str):
    otocna_map = {'0': '0', '1': '1', '2': '2', '5': '5', '6': '9', '8': '8', '9': '6'}
    
    otocene = []
    for cifra in reversed(cislo_str):
        if cifra not in otocna_map:
            return None
        otocene.append(otocna_map[cifra])
    
    return ''.join(otocene)

def pocitaj_platne_cisla(k):
    from itertools import product

    cifry = ['0', '1', '2', '5', '6', '8', '9']
    
    pocet = 0
    
    if k == 1:
        validne_cisla = ['0', '1', '2', '5', '6', '8', '9']
        for cislo in validne_cisla:
            if otoč_a_skontroluj(cislo) == cislo:
                pocet += 1
        return pocet
    
    for cislo_tupl in product(cifry, repeat=k):
        cislo_str = ''.join(cislo_tupl)
        
        if cislo_str[0] == '0':
            continue

        otocene_cislo = otoč_a_skontroluj(cislo_str)
        if otocene_cislo is not None and cislo_str == otocene_cislo:
            pocet += 1
            
    return pocet

k = int(input())
vysledok = pocitaj_platne_cisla(k)
print(vysledok)
