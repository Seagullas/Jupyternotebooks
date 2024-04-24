from matematika import sudetis,daugyba, rask_didziausia, pasisveikinimas
import matematika
import pytest
def test_sudetis():
    assert sudetis(1,2) == 3


def test_sudetis_negiami():
    assert sudetis(-1,-5) == -6

def test_daugyba():
    assert daugyba(2, 7) == 14
    assert daugyba(5,5) >0
    assert daugyba(-5,-5)>0
    assert daugyba(-5,5)<0

def test_sudetis_2():
    num1, num2= 5, 3
    rezultatas = 8
    faktinis_rezultatas= sudetis(num1, num2)
    assert rezultatas ==faktinis_rezultatas, f'Sudeties testas nepavyko: {num1} ir {num2} turetu buti {rezultatas}, o gauta {faktinis_rezultatas}'

def test_rask_didziausia():
    num1, num2 = 10,15
    rezultatas= 15
    faktinisrez= rask_didziausia(num1,num2)
    assert faktinisrez == rezultatas

def test_rask_didziausia_2():
    assert rask_didziausia(10,5)
    assert rask_didziausia(5,10)
    assert rask_didziausia(10,10)

def test_pasisveikinimas():
    assert pasisveikinimas('Tomas') == 'Labas, Tomas'

def test_pasisveikinimas_2():
    assert matematika.pasisveikinimas('Romas')=='Labas, Romas'

def test_pirmas_sarase():
    skaiciai = [1,2,3,4,5]
    assert matematika.pirmas_sarase(skaiciai) ==1

def test_pirmas_sarase():
    raides=['a','b','c']
    assert matematika.pirmas_sarase(raides) =='a'

def test_pirmas_sarase_tuscias():
    skaicia=[]
    assert matematika.pirmas_sarase(skaicia)== None

import uzd1

def test_uzd():
    assert matematika.funkcija('alus')== 'sula'

def test_sum():
    sk= [1,5,9,6,7]
    assert matematika.suma(sk)== 28

def test_teigiami():
    sar= [1,-5,6,-10]
    assert matematika.teigiami(sar)==[1,6]

def test_rusiavimas():
    saras= [1,-5,6,-10]
    assert matematika.rusiavimas('did',saras) ==[-10,-5,1,6]

def test_rusiavimas_2():
    saras= [1,-5,6,-10]
    assert matematika.rusiavimas('maz',saras) ==[6,1,-5,-10]

from matematika import rikiuoti_mazejanciai, rikiuoti, rikiuoti_didejant

def test_rikiuoti_mazejanciai():
    assert rikiuoti(rikiuoti_mazejanciai, [4,5,1,3]) == [5,4,3,1]

def test_rikiuoti_didejant():
    assert rikiuoti(rikiuoti_didejant, [4,5,1,3]) == [1,3,4,5]

@pytest.mark.parametrize('sarasas, tiketinas_rezultatas', [
    ([1,2,3,4], 1),
    (['a', 'b', 'c'], 'a'),
    ([], None),
    ([[1,2],[3,4], [5,6]], [1,2])
])
def test_gauti_pirma_elementa(sarasas, tiketinas_rezultatas):
    assert matematika.pirmas_sarase(sarasas) == tiketinas_rezultatas

@pytest.mark.parametrize('a, b, c, turis', [
    (1,1,1,1),
    (2,3,2,12),
    (5,6,18,540)
])
def test_kubo_turis(a, b, c, turis):
    assert matematika.kubo_turis(a,b,c) == turis

# 1 Užduotis
# Sukurkite funkciją, kuri patikrintų ar skaičius dalinasi iš 3
# Parašykite keletą testų (naudojantis parametrize)
@pytest.mark.parametrize('a', [
    (8),
    (6),
    (12)
])


def test_pirmninis(a):
    assert matematika.pirminis(a) == 0

# 2 užduotis 
# Parašykite funkciją rasti_pasikartojancias_raides, kuri priima sąrašą žodžių ir grąžina sąrašą tų žodžių
# kurie turi bent vieną pasikartojančią raidę.
# Parašykite keletą testų (naudojantis parametrize)

@pytest.mark.parametrize('sarasas', [
    (['a','b','c','y']),
    (['a','b','c','a']),
])

def test_pasikartojimas(sarasas):
    assert matematika.pasikartojimas(sarasas) == True

@pytest.mark.parametrize('a',[
    (1),
    (3),
    (5),
    (12)
])