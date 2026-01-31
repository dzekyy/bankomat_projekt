from bankomat_modul import *

print("=== KREIRANJE OSOBE ===")
ime = input("Unesite ime vlasnika racuna: ")

# 1 Racun
racun = Racun(ime)
racun.Otvaranje()

print("\nRacun otvoren!")
print("Ziro racun:", racun.get_ziro())

# 2 Kartica
print("\n=== KREIRANJE KARTICE ===")
pin = input("Postavite PIN (4 cifre): ")

kartica = Kartica(pin, racun)   

print("Kartica uspjesno kreirana!")
print("Broj kartice:", kartica.broj_kartice)


# 3 Bankomat
banka = Banka()
banka.dodaj_karticu(kartica)
print("\n=== BANKOMAT ===")
unesena_kartica = input("Unesite broj kartice: ")

kartica = banka.provjeri_karticu(unesena_kartica)

if kartica is None:
    print("Kartica nije prepoznata.")
else:
 if provjera_pina(kartica):  
  while True:
    print("====================================================")
    print(f"Pozdrav {racun.ime_prezime} Izaberite sta zelite:")
    print("1.Pregledati stanje na racunu")
    print("2.Uplatiti novac na racun")
    print("3.Podici novac s racuna.")
    print("4.Zavrsiti transakcije")
    x=int(input("Unesite broj zeljenje transakcije:"))
    if x==1:
        print(racun.Prikaz_Stanja())
        print("Da li zelite drugu transakciju?(Molim koristite samo velika slova DA/NE)")
        potvrda=input("Da li zelite novu transakciju DA/NE:\n")
        if potvrda=="DA":
            continue
        else:
            break

    elif x==2:
         iznos = float(input("Unesite iznos za uplatu: "))
         racun.uplata(iznos)
         print("Da li zelite drugu transakciju?(Molim koristite samo velika slova DA/NE)")
         potvrda=input("Da li zelite novu transakciju DA/NE:")
         if potvrda=="DA":
            continue
         else:
            break
    elif x==3:
         iznos = float(input("Unesite iznos koji zelite podici: "))
         racun.isplata(iznos)
         print("Da li zelite drugu transakciju?(Molim koristite samo velika slova DA/NE)")
         potvrda=input("Da li zelite novu transakciju DA/NE")
         if potvrda=="DA":
            continue
         else:
            break
    elif x==4:
        break   
