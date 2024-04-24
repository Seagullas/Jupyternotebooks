def sudetis(a,b):
    return  a+b

def daugyba(a: int,b: int) -> int:
    return a*b

def rask_didziausia(a:int,b:int) ->int:
    return a if a>b else b

def pasisveikinimas(vardas):
    return f'Labas, {vardas}'

def pirmas_sarase(sarasas:list):
    return sarasas[0] if sarasas else None

def funkcija(kint):
    return kint[::-1]

# 2 užduotis
# parašykite funkciją, kuri kaip argumentą priima sąrašą ir grąžina to sąrašo narių sumą
# parašykite keletą testų šiai funkcijai

def suma(sarasas:list):
    return sum(sarasas)

# 3 užduotis
# parašykite funkciją, kuri kaip argumentą priima sąrašą ir grąžina jame esančius TEIGIAMUS skaičius
# parašykite keletą testų šiai funkcijai

def teigiami(lst):
    return [x for x in lst if x > 0] or None

# 4 užduotis
# Parašykite funkciją, kuri priima dvi sąrašų rūšiavimo funkcijas: 
# vieną didėjančiai rūšiavimui, kitą mažėjančiai rūšiavimui, ir sąrašą skaičių. 
# Funkcija turi grąžinti rūšiuotą sąrašą pagal pateiktas rūšiavimo funkcijas.
# parašykite keletą testų šiai funkcijai

def rusiavimas(funk, sara:list):
    if funk== 'did':
        sara.sort()
        return sara
    elif funk =='maz':
        sara.sort(reverse=True)
        return sara

def rikiuoti(rikiavimo_funkcija, sarasas):
    return rikiavimo_funkcija(sarasas)

def rikiuoti_mazejanciai(sarasas):
    return sorted(sarasas, reverse=True)

def rikiuoti_didejant(sarasas):
    return sorted(sarasas)

print(rikiuoti(rikiuoti_mazejanciai, [5,3,4,1,6,9]))
def kubo_turis(a, b, c):
    return a * b * c

# 1 Užduotis
# Sukurkite funkciją, kuri patikrintų ar skaičius dalinasi iš 3
# Parašykite keletą testų (naudojantis parametrize)
def pirminis(a):
    return a%3

# 2 užduotis 
# Parašykite funkciją rasti_pasikartojancias_raides, kuri priima sąrašą žodžių ir grąžina sąrašą tų žodžių
# kurie turi bent vieną pasikartojančią raidę.
# Parašykite keletą testų (naudojantis parametrize)

def pasikartojimas(sarasas:list):
    for i in sarasas:
        if sarasas.count(i) == 1:
            return True
        else:
            return False
# 3 užduotis 
# Parašykite funkciją, kuri priima skaičių ir patikrina, ar jis yra pirminis. 
# Grąžinkite True, jei skaičius yra pirminis, ir False, jei ne.
# Parašykite keletą testų (naudojantis parametrize)

def pirminis(a):
    if a<=0:
        return False
    elif a== 1 or a ==2:
        return True
    for i in range(2, a):
        if a% i==0:
            return False
    return True

#2
def raides(sarasas):
    atrinti_zodziai= []
    for zodis in sarasas:
        if len(set(zodis))<len(zodis):
            atrinti_zodziai.append(zodis)
        return atrinti_zodziai