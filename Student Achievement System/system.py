"""
Potreban nam je program pomoću kojeg ćemo pratiti uspeh studenata na ispitima. Za
svakog studenta pamtimo ime, prezime, broj indeksa, šifru smera i sve predmete koje
treba da položi ili je položio sa ocenom od 6 do 10. Za svaki predmet koji je dodeljen
studentu znamo naziv i jedinstvenu šifru predmeta.
Na osnovu unetih podataka, potrebno je da program omogući prikaz (ima sledeće
funkcionalnosti):
a. svih položenih ispita određenog studenta
b. srednje ocene određenog studenta
c. podataka studenta/studenata sa navećom prosečnom ocenom
d. podataka studenta/studenata sa najmanje položenih ispita
e. svih studenta koji su položili sve ispite na predmetima koji su im dodeljeni
f. raspodele studenata po smerovima, u procentima
g. sve studente na odabranom smeru
h. najboljeg studenta na odabranom smeru
Kada se program pokrene, prikazati korisniku glavni meni sa opcijama a - j (koje može
da unese sa tastature). Nakon odabira opcije, ukoliko je potrebno, od korisnika
zahtevati unos podataka i prikazati željene rezultate. Potom, ponovo prikazati glavni
meni.
Korisnik prekida program odabirom opcije “Kraj programa”
(Bonus) Dodati opcije za unos ocene studentu nakon položenog ispita
(Bonus) Dodati opciju za dodavanje novog studenta
(Bonus) Dodati opciju za dodeljivanje novog predmeta postojećem studentu
(Bonus) Dodati opciju za uklanjenje predmeta postojećem studentu, pod uslovom da
nije položen
(Bonus) Dodati opciju za brisanje studenta, pod uslovom da nije položio niti jedan ispit
"""

studenti = {
    "FS22001":
        {
            "ime": "Dragana",
            "prezime": "Mirković",
            "sifra_smera": "FS",
            "predmeti": [
                {"ocena": 8, "šifra": "FSx101", "naziv": "Istorija filozofije"},
                {"ocena": 8, "šifra": "FSx102", "naziv": "Logika"},
                {"ocena": 0, "šifra": "FSx103", "naziv": "Filozofija religije"}
            ]
        },
    "FS22002":
        {
            "ime": "Šemsa",
            "prezime": "Suljaković",
            "sifra_smera": "FS",
            "predmeti": [
                {"ocena": 0, "šifra": "FSx101", "naziv": "Istorija filozofije"},
                {"ocena": 7, "šifra": "FSx102", "naziv": "Logika"},
                {"ocena": 0, "šifra": "FSx103", "naziv": "Filozofija religije"}
            ]
        },
    "FS22003":
        {
            "ime": "Marta",
            "prezime": "Savić",
            "sifra_smera": "FS",
            "predmeti": [
                {"ocena": 10, "šifra": "FSx101", "naziv": "Istorija filozofije"},
                {"ocena": 10, "šifra": "FSx102", "naziv": "Logika"},
                {"ocena": 0, "šifra": "FSx103", "naziv": "Filozofija religije"}
            ]
        },
    "SC22001":
        {
            "ime": "Mile",
            "prezime": "Kitić",
            "sifra_smera": "SC",
            "predmeti": [
                {"ocena": 8, "šifra": "SCx101", "naziv": "Socijalna demografija"},
                {"ocena": 9, "šifra": "SCx102", "naziv": "Uvod u sociologiju"},
                {"ocena": 7, "šifra": "SCx103", "naziv": "Osnovi ekonomije"}
            ]
        },
    "SC22002":
        {
            "ime": "Kemal",
            "prezime": "Malovčić",
            "sifra_smera": "SC",
            "predmeti": [
                {"ocena": 8, "šifra": "SCx101", "naziv": "Socijalna demografija"},
                {"ocena": 7, "šifra": "SCx102", "naziv": "Uvod u sociologiju"},
                {"ocena": 0, "šifra": "SCx103", "naziv": "Osnovi ekonomije"}
            ]
        },
    "SC22003":
        {
            "ime": "Jašar",
            "prezime": "Ahmedovski",
            "sifra_smera": "SC",
            "predmeti": [
                {"ocena": 10, "šifra": "SCx101", "naziv": "Socijalna demografija"},
                {"ocena": 9, "šifra": "SCx102", "naziv": "Uvod u sociologiju"},
                {"ocena": 8, "šifra": "SCx103", "naziv": "Osnovi ekonomije"}
            ]
        }
}


def prikaz_polozenih(index, studenti):
    student = studenti[index]
    for ispiti in student["predmeti"]:
        if ispiti["ocena"] > 0:
            print(f"Student sa indexom {index} je položio ispit {ispiti['šifra']} sa ocenom {ispiti['ocena']}")


def racunanje_proseka(index, studenti):
    student = studenti[index]
    suma_ocena = 0
    broj_polozenih = 0
    for ispiti in student["predmeti"]:
        if ispiti["ocena"] > 0:
            suma_ocena += ispiti["ocena"]
            broj_polozenih += 1
    prosek = round(suma_ocena / broj_polozenih, 2)
    return index, prosek


def prikaz_studenta_sa_najvisim_prosekom():
    max_prosek = 0
    max_index = ""
    for student in list(studenti.items()):
        index, trenutni_prosek = racunanje_proseka(student[0], studenti)
        if trenutni_prosek > max_prosek:
            max_prosek = trenutni_prosek
            max_index = index
    return max_index


def broj_polozenih(index, studenti):
    student = studenti[index]
    broj_p = 0
    for ispiti in student["predmeti"]:
        if ispiti["ocena"] != 0:
            broj_p += 1
    return index, broj_p


def prikaz_studenta_sa_najmanje_polozenih():
    min_polozenih = 100
    min_index = ""
    for student in list(studenti.items()):
        index, broj_p = broj_polozenih(student[0], studenti)
        if broj_p <= min_polozenih:
            min_polozenih = broj_p
            min_index = index
    print(
        f"Student sa najmanje položenih ispita, koji iznosi {min_polozenih}, je student sa oznakom indexa {min_index}")


def prikaz_studenata_koji_su_polozili_sve():
    broj_ispita = 3
    polozili_sve = []
    for student in list(studenti.items()):
        index, broj_p = broj_polozenih(student[0], studenti)
        if broj_p == broj_ispita:
            polozili_sve.append(index)
    return polozili_sve


def studenti_po_smerovima():
    filozofija = []
    sociologija = []
    for id, info in studenti.items():
        for k in info:
            if info[k] == "FS":
                filozofija.append(id)
            elif info[k] == "SC":
                sociologija.append(id)
    return sociologija, filozofija


def najbolji_na_smeru():
    smer = input("Uneti smer: ")
    if smer == "filozofija":
        filozofija = studenti_po_smerovima()[1]
        for index in filozofija:
            prosek_f = 0
            najbolji_f = ""
            if index in prikaz_studenata_koji_su_polozili_sve():
                if racunanje_proseka(index, studenti)[1] > prosek_f:
                    najbolji_f = index
            else:
                if racunanje_proseka(index, studenti)[1] > prosek_f:
                    najbolji_f = index
        print(f"Najbolji student na smeru filozofija je {najbolji_f}")
    elif smer == "sociologija":
        sociologija = studenti_po_smerovima()[0]
        for index_ in sociologija:
            prosek_s = 0
            najbolji_s = ""
            if index_ in prikaz_studenata_koji_su_polozili_sve():
                if racunanje_proseka(index_, studenti)[1] > prosek_s:
                    najbolji_s = index_
            else:
                if racunanje_proseka(index_, studenti)[1] > prosek_s:
                    najbolji_s = index_
        print(f"Najbolji student na smeru sociologija je {najbolji_s}")
    else:
        print("Nepravilan unos")


ans = True

while ans:
    print("""
    a. svih položenih ispita određenog studenta
    b. srednje ocene određenog studenta
    c. podataka studenta/studenata sa navećom prosečnom ocenom
    d. podataka studenta/studenata sa najmanje položenih ispita
    e. svih studenta koji su položili sve ispite na predmetima koji su im dodeljeni
    f. raspodele studenata po smerovima, u procentima
    g. sve studente na odabranom smeru
    h. najboljeg studenta na odabranom smeru
    x. kraj programa

    """)
    ans = input("Izabrati opciju iz menija: ")
    if ans == "a":
        index_1 = input("Uneti broj indexa studenta: ")
        if index_1 in studenti:
            prikaz_polozenih(index_1, studenti)
        else:
            print("Nepravilan unos.")
    elif ans == "b":
        index_2 = input("Uneti broj indexa studenta: ")
        if index_2 in studenti:
            print(f"Student sa indexom {index_2} ima srednju ocenu {racunanje_proseka(index_2, studenti)[1]}")
        else:
            print("Nepravilan unos.")
    elif ans == "c":
        print(f"Student sa najvišim prosekom je student sa oznakom indexa {prikaz_studenta_sa_najvisim_prosekom()}")
    elif ans == "d":
        prikaz_studenta_sa_najmanje_polozenih()
    elif ans == "e":
        print(
            f"Studenti koji su položili sve ispite su studenti sa oznakama indexa "
            f"{prikaz_studenata_koji_su_polozili_sve()}")
        prikaz_studenata_koji_su_polozili_sve()
    elif ans == "f":
        print(
            f"Procenat studenata na smeru filozofija je {(len(studenti_po_smerovima()[1]) / len(list(studenti)) * 100)}"
            f"%, a na smeru sociologija {len(studenti_po_smerovima()[0]) / len(list(studenti)) * 100}%.")
    elif ans == "g":
        stud = input("Uneti smer: ")
        if stud == "filozofija":
            print(f"Svi studenti na smeru filozofija su: {studenti_po_smerovima()[1]}")
        elif stud == "sociologija":
            print(f"Svi studenti na smeru sociologija su: {studenti_po_smerovima()[0]}")
        else:
            print("Nepravilan unos.")
    elif ans == "h":
        najbolji_na_smeru()
    elif ans == "x":
        print("Kraj programa.")
        ans = False
    else:
        print("Nepravilan unos.")
