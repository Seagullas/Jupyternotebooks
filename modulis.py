A= 7

def printA():
    print('as esu funkcija')

class vechile():
    def __init__(self, P, R):
        self.P= P
        self.R= R
class Car(vechile):
    def __init__(self, P, R, S):
        super(). __init__ (P, R)
        self.S=S
    def getSeats(self):
        txt= self.P + 'turi ' + str(self.S) + ' sed vietu'
        return txt
    
test = Car( P='pavadinimas', R=5000, S= 200)

print(test.getSeats())

class Train(vechile):
    def __init__(self, P, R, S):
        super(). __init__ (P, R)
        self.S=S
    def getSeats(self):
        txt= self.P + 'turi ' + str(self.S) + ' sed vietu'
        return txt
    
test = Train( P='pavadinimas', R=5000, S= 200)

print(test.getSeats())

class Bus(vechile):
    def __init__(self, P, R, S):
        super(). __init__ (P, R)
        self.S=S
    def getSeats(self):
        txt= self.P + 'turi ' + str(self.S) + ' sed vietu'
        return txt
    
test = Bus( P='pavadinimas', R=5000, S= 200)

print(test.getSeats())

#sukurkite failus nuskaitančią klasę, ji turi būti aprašyta jūsų kuriamame modulyje;
#ta klasė turi nuskaityti pateiktą failą, ir suskaidyti stulpelius į sąrašus:
#sąrašai I, U, j, P, duomenys iš juos iš atitinkamų taip pat pavadintų stulpelių
#realizuokite tai, jog klasė rastų tokį dydį - maksimalų P, suskaičiuotų tokį dydį pce = Pmax / 1000 * 100%;
#šie dydžiai turi būti pasiekiamį arba kaip atributas, arba galite įdėti metodą jam gauti
import numpy as np
class failai():
    def __init__(self,pav, skirtukas):
        self.pav= pav
        self.skirtukas=skirtukas
        self.i=[]
        self.u=[]
        self.j=[]
        self.p=[]
    def read(self):
        fname= self.pav
        f=open(fname, mode='r',encoding='utf-8')
        turinys=f.readlines()
        f.close()
        for x in turinys[1:]:
            self.i.append(float(x.split(self.skirtukas)[0]))
            self.u.append(float(x.split(self.skirtukas)[1]))
            self.j.append(float(x.split(self.skirtukas)[2]))
            self.p.append(float(x.split(self.skirtukas)[3].replace('\n','')))
        # print(self.i)
        # print(self.u)
        # print(self.j)
        print(self.p)
    def maxp(self):
        pmax=(max(self.p))
        return pmax
    def getpce(self):
        pmax=self.maxp()
        pce= pmax/1000*100
        return pce
sarasas= failai('123.dat',';')
sarasas.read()
print(sarasas.getpce())



class keturiolika_failu():
    def __init__(self, Pavadinimas, Skirtukas):
        self.Pavadinimas = Pavadinimas
        self.Skirtukas = Skirtukas
        self.I = []
        self.U = []
        self.j = []
    def dataReader(self):
        fname = self.Pavadinimas
        file = open(fname, mode='r', encoding= 'utf-8')
        sarasas = file.readlines() # suformuoja teksta kaip eiluciu sarasa
        file.close()
        print(sarasas) # pasitikrinam ar veikia
        for eilute in sarasas[1::]:
            self.I.append(float(eilute.split(self.Skirtukas)[0]))
            self.U.append(float(eilute.split(self.Skirtukas)[1]))           
            self.j.append(float(eilute.split(self.Skirtukas)[2]))
            self.p.append(float(eilute.split(self.Skirtukas)[3].replace('\n', '')))
        print(self.I)
        print(self.U) 
        print(self.j) 
        print(self.p) 
    def getPmax(self):
        Pmax = (max(self.p))
        return Pmax
    
    def getPCE(self):
        Pmax= self.getPmax()
        PCE = round((Pmax / 1000 * 100),2)
        return PCE
    def bonusas(self):
        
    
sarasas = keturiolika_failu('REF_D_5k_FW_2.03.dat', ';') #pasitikrinam ar nuskaito info is failo
sarasas.dataReader()
print(sarasas.getPCE())