class Mokinys():
    def __init__(self, vardas, pavarde):
        self.V = vardas
        self.P = pavarde
        self.pazymiai = []
    def getVidurkis(self):
        vidurkis = sum(self.pazymiai)/len(self.pazymiai)
        return vidurkis
    
    def getMax(self):
        pazymysMax = max(self.pazymiai)
        return pazymysMax
    def getMin(self):
        pazymysMin = min(self.pazymiai)
        return pazymysMin
class Mokykla():
    def __init__(self):
        self.Mokiniai = []
    def addMokinys(self, mokinys):
        self.Mokiniai.append(mokinys)
    def removeMokinys(self, mokinys):
        self.Mokiniai.remove(mokinys)
    def VisuMokiniuVidurkis(self):
        VisuMokiniuPazymiai = []
        for mokinys in self.Mokiniai:
            VisuMokiniuPazymiai.extend(mokinys.pazymiai) # extend leidzia sujungti skirtingus sarasus, prisplecia sarasas, esantis pries extend metoda
        VisuMokiniuVidurkis = sum(VisuMokiniuPazymiai)/len(VisuMokiniuPazymiai)
        return VisuMokiniuVidurkis
class Abiturientas(Mokinys):
    def __init__(self, vardas , pavarde , pazymiai , egzaminas):
        super().__init__(vardas , pavarde , pazymiai)
        self.egzaminas = egzaminas
    def vidurkissuegzaminuf(self):
        pazymiaisuegazimu = self.pazymiai + self.egzaminas
        # self.pazymiaisuegzaminu = pazymiaisuegazimu
        vidurkissuegzaminu = sum(pazymiaisuegazimu) / len(pazymiaisuegazimu)
        return vidurkissuegzaminu