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
        print(turinys)
        for x in turinys[1::]:
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
        pce= round((pmax/1000*100),2)
        return pce
    # def bonusas(self):
    #     j= 

#Bonus, kas atliko - pabandykite realizuoti radimą tokių verčių: j kai U = 0 (arba close to zero), 
#U, kai j =0 (arba close to zero), jie turi specialius žymėjimus jsc ir Uoc.
sarasas= failai('123.dat',';')
sarasas.read()
print(sarasas.getpce())
# nuskaitymas visų failų pvz: 

# import glob
# import os
# dir_path = f"{os.getcwd()}\\*"
# for file_path in glob.glob(dir_path):
#     if file_path.endswith(".dat"):
#         data = m.Duomenys(file_path)
#         print("P: ", data.P)