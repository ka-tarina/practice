"""
Zadatak1.

inputfile.txt
Kasir: Milan Jovanovic
Racuni: 2000,3330,9999,1122.2
Kasir:Pera Peric
Racuni: 2999,3333,444,5555
Kasir:Joca Jovanovic
Racuni: 3939,333,44,55

Ucitati inputfile.txt, za svakog kasira sracunati koliko je ukupan promet ostvario (sabiraju se vrednosti is reda
Racuni). Za svakog kasira naprati fajl koji se zove ime_prezime_rb.txt i upisati sledece:
Ime Prezime : promet

Rb u nazivu output fajla odgovara njegovoj poziciji po velicini zarade (kasir sa najvecom zaradom ima broj 1)...

Primer output:

Milan_Jovanovic_1.txt:
	Milan Jovanovic: 16451.20
Pera_Peric_2.txt:
	Pera Peric: 12331.00
Joca_Jovanovic_3.txt:
	Joca Jovanovic: 4371.00

"""


def zarade_kasira(file):
    konacni = []
    with open(file, "r") as file:
        kasir_list = []
        trenutni_kasir = ""
        for line in file:
            kasir_dict = {}
            if line.startswith("Kasir:"):
                trenutni_kasir = line.split(":")[1].strip()
                kasir_dict[trenutni_kasir] = 0
            elif line.startswith("Racuni:"):
                racuni = line.split(":")[1].split(",")
                r = []
                for racun in racuni:
                    racun = float(racun.strip())
                    r.append(racun)
                racuni_sum = sum(r)
                kasir_dict[trenutni_kasir] = racuni_sum
                kasir_list.append(kasir_dict)
    for i in kasir_list:
        for key, value in i.items():
            temp = {}
            temp["ime"] = key
            temp["zarada"] = value
            konacni.append(temp)
    return konacni


def napravi_foldere(file):
    kasir_list = zarade_kasira(file)
    newlist = sorted(kasir_list, key=lambda d: d["zarada"], reverse=True)
    counter = 1
    for i in newlist:
        with open(i["ime"] + "_" + str(counter), "w") as f:
            f.write(f"{i['ime']}: {i['zarada']}")
        counter +=1
    return newlist

napravi_foldere("inputfile")
