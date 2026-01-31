import random
from getpass import getpass
class Racun:
    """
    Klasa koja predstavlja bankovni racun.
    Čuva stanje, žiro račun i prati dnevni limit za isplate.
    """
     
    def __init__(self,ime_preime):
        self.ime_prezime=ime_preime
        self.__ziro_racun=None
        self.__stanje=0.0
        self.__dnevni_dizanje = 0.0  
        self.__dnevni_limit = 1000.0 #maksimalni limit za podici na dnevnom nivou 

    def Otvaranje(self):

        """Generira i dodjeljuje random 16-cifreni broj računa"""

        self.__ziro_racun = ''.join(str(random.randint(0, 9)) for _ in range(16))
        print(f"Racun za {self.ime_prezime} je otvoren!")

    def Prikaz(self):
        if self.__ziro_racun:
            return f"Ziro racun za {self.ime_prezime},je otvoren i on je:{self.__ziro_racun}"
        else:
            return "Ziro racun nije otvoren"
    

    """Vraća broj žiro računa."""
    def get_ziro(self):
        return self.__ziro_racun
    
    """Dodaje iznos na racun"""
    def uplata(self, iznos):
        if iznos <= 0:
            print("Nevalidan iznos")
            return
        self.__stanje += iznos
        print(f"Uplatili ste {iznos} KM. Stanje je sada {self.__stanje} KM.")

        """Skida/podize iznos s racuna, provjerava dostupnost sredstava, kao i dnevno limit"""
    def isplata(self, iznos):
        if iznos <= 0:
            print("Nevalidan iznos")
            return
        if iznos > self.__stanje:
            print(f"Nedovoljno sredstava. Trenutno stanje: {self.__stanje} KM.")
            return
        if self.__dnevni_dizanje + iznos > self.__dnevni_limit:
            dozvoljeno = self.__dnevni_limit - self.__dnevni_dizanje
            print(f"Dnevni limit od {self.__dnevni_limit} KM je dostignut. Možete podići još {dozvoljeno} KM danas.")
            return
        self.__stanje -= iznos
        self.__dnevni_dizanje += iznos
        print(f"Podigli ste {iznos} KM. Stanje je sada {self.__stanje} KM. Dnevno podignuto: {self.__dnevni_dizanje} KM.")


    """Vraća string sa imenom vlasnika i trenutnim stanjem."""
    def Prikaz_Stanja(self):
        return f"{self.ime_prezime}| {self.__stanje} KM"



    """
    Klasa koja predstavlja bankovnu karticu.
    Kartica je povezana sa racunom i ima PIN za provjeru.
    """
class Kartica:
    def __init__(self,pin,racun:Racun):
        if not pin.isdigit() or len(pin) != 4:
            raise ValueError("PIN mora imati 4 cifre")
        self.__pin=pin
        if racun.get_ziro() is None:
            raise ValueError("Racun nije otvoren")
        self.broj_kartice = ''.join(str(random.randint(0, 9)) for _ in range(16))
        self.ziro_racun = racun.get_ziro() 

        
    def provjeri_pin(self, uneseni_pin):
        """Provjerava da li je uneseni PIN ispravan."""
        return self.__pin == uneseni_pin
    


class Banka:
    """
    Klasa koja predstavlja banku.
    Čuva sve račune i kartice.
    """
    def __init__(self):
        self.racuni = {}    # ziro_racun : Racun
        self.kartice = {}   # broj_kartice : Kartica

    def dodaj_racun(self, racun):
        """Dodaje račun u banku."""
        self.racuni[racun.get_ziro()] = racun

    def dodaj_karticu(self, kartica):
        """Dodaje karticu u banku."""
        self.kartice[kartica.broj_kartice] = kartica

    def provjeri_karticu(self, broj_kartice):
        """Provjerava da li kartica postoji u banci."""
        return self.kartice.get(broj_kartice)

    
def provjera_pina(kartica):
    """
    Funkcija koja traži od korisnika unos PIN-a.
    Dozvoljena su 3 pokušaja.
    """
    pokusaji = 3

    while pokusaji > 0:
        uneseni_pin = getpass("Unesite PIN (4 cifre): ")

        if kartica.provjeri_pin(uneseni_pin):
            print("PIN ispravan. Dobrodošli!")
            return True
        else:
            pokusaji -= 1
            print("Pogrešan PIN. Preostalo pokušaja:", pokusaji)

    print("Kartica je blokirana!")
    return False



        