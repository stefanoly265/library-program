#[]


class Knjiga:
    def __init__(self,naslov,autor,godina_izdanja,vrsta,kolona,polica,dostupnost_knjige=True):
        self.naslov=naslov
        self.autor=autor
        self.godina_izdanja=godina_izdanja
        self.vrsta=vrsta
        self.kolona=kolona
        self.polica=polica
        self.dostupnost_knjige=dostupnost_knjige

    def zaduziti_knjigu(self):
        if self.dostupnost_knjige==True:
            print(f"Knjiga {self.naslov} je upravo zaduzena.")
            self.dostupnost_knjige=False
        else:
            print(f"Knjiga '{self.naslov}' trenutno nije dostupna.")

    def vratiti_knjigu(self):
        if self.dostupnost_knjige==False:
            print(f"Knjiga {self.naslov} je upravo vracena.")
            self.dostupnost_knjige = True
        else:
            print(f"Knjiga {self.naslov} nije ni bila zaduzena!")

    def proveriti_dostupnost(self):
        if self.dostupnost_knjige==True:
            print(f"Knjiga {self.naslov} je dostpna.")
        else:
            print(f"Knjiga {self.naslov} nije dostupna.")







class Biblioteka:
    def __init__(self, naziv):
        self.naziv = naziv
        self.sve_knjige = []  

    def dodaj_knjigu(self, nova_knjiga):
        self.sve_knjige.append(nova_knjiga)
        print(f"Dodata knjiga '{nova_knjiga.naslov}' u biblioteku.")

    def nadji_po_polici(self, trazena_polica):
        print(f"\n--- Knjige na polici '{trazena_polica}' ---")
        for knjiga in self.sve_knjige:
            if knjiga.polica == trazena_polica:
                print(f"- {knjiga.naslov} (Kolona {knjiga.kolona})")

    def nadji_po_naslovu(self, trazen_naslov):
        pronadjena = False
        for knjiga in self.sve_knjige:
            if knjiga.naslov == trazen_naslov:
                print(f"-- Knjiga '{knjiga.naslov}' je {knjiga.vrsta} vrsta, {knjiga.kolona} kolona i {knjiga.polica} polica. Autor naslova je {knjiga.autor}")
                pronadjena = True
    

    def zaduzi_po_naslovu(self, trazen_naslov):
        pronadjena = False
        for knjiga in self.sve_knjige:
            if knjiga.naslov == trazen_naslov:
                knjiga.zaduziti_knjigu()
                pronadjena = True
                break
        if not pronadjena:
            print(f"Knjiga '{trazen_naslov}' se ne nalazi u biblioteci.")

    def vrati_po_naslovu(self, trazen_naslov):
        pronadjena = False
        for knjiga in self.sve_knjige:
            if knjiga.naslov == trazen_naslov:
                knjiga.vratiti_knjigu()
                pronadjena = True
                break
        if not pronadjena:
            print(f"Knjiga '{trazen_naslov}' se ne nalazi u biblioteci.")
        if not pronadjena:
            print(f"Knjiga sa naslovom '{trazen_naslov}' se ne nalazi u biblioteci.")



knjiga1 = Knjiga("Zlocin i kazna", "Dostojevski", 1866, vrsta=1, kolona=2, polica="leva")
knjiga2 = Knjiga("Na Drini cuprija", "Ivo Andric", 1945, vrsta=1, kolona=1, polica="leva")
knjiga3 = Knjiga("Tvrdjava", "Mesa Selimovic", 1970, vrsta=2, kolona=4, polica="desna")


gradska_biblioteka = Biblioteka("Gradska Biblioteka")
gradska_biblioteka.dodaj_knjigu(knjiga1)
gradska_biblioteka.dodaj_knjigu(knjiga2)
gradska_biblioteka.dodaj_knjigu(knjiga3)

gradska_biblioteka.nadji_po_polici("leva")
gradska_biblioteka.nadji_po_naslovu("Hari Poter")

gradska_biblioteka.zaduzi_po_naslovu("Zlocin i kazna")
knjiga1.proveriti_dostupnost()





    
    