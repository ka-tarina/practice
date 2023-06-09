"""
Zadatak 1. Napisati program koji će od ulaznog teksta(stringa) u sledećem obliku:

REG_OZNAKA  BOJA    TIP_VOZILA
NI-543-MM   siva    automobil
LE-345-KM   plava    kamion
BG-345-TT   bela    automobil
KG-365-KG   plava    automobil
SU-475-GM   bela    automobil
KG-845-YB   crna    autobus
NI-345-XD   bela    automobil
UE-134-NF   crna    automobil
AL-226-DF   bela    kamion

(Podaci su izlistani u zasebnim redovima, a u svakom redu su odvojeni tabom. Prvi red (REG_OZNAKA    BOJA    TIP_VOZILA)
 jeste deo input teksta)

Napraviti izlaz u obliku:

{
    tip_vozila: {
            "automobil": "66.67%",
            "kamion": "22.22%",
            "autobus": "11.11%"
    },
    gradovi: ["NI", "LE", "BG", "KG", "UE", "AL", "SU"],
    boja_po_tipu: {
        "automobil":{
            "siva": 1,
            "bela": 3,
            "plava": 1,
            "crna": 1,
       },
        "kamion":{
            "bela": 1,
            "plava": 1
    },
        "autobus":{
            "crna": 1
        }
    },
}

"""


import re

text = """REG_OZNAKA  BOJA    TIP_VOZILA
NI-543-MM   siva    automobil
LE-345-KM   plava    kamion
BG-345-TT   bela    automobil
KG-365-KG   plava    automobil
SU-475-GM   bela    automobil
KG-845-YB   crna    autobus
NI-345-XD   bela    automobil
UE-134-NF   crna    automobil
AL-226-DF   bela    kamion"""

text_list = text.split('\n')[1:]

tip_vozila = {}
gradovi = []
boja_po_tipu = {}

for line in text_list:
    reg_oznaka, boja, tip_vozila_ = line.split()
    grad = re.findall('[A-Z]{2}', reg_oznaka)[0]
    gradovi.append(grad)
    gradovi = list(set(gradovi))
    if tip_vozila_ not in tip_vozila:
        tip_vozila[tip_vozila_] = 1
    else:
        tip_vozila[tip_vozila_] += 1
    if tip_vozila_ not in boja_po_tipu:
        boja_po_tipu[tip_vozila_] = {boja: 1}
    elif boja not in boja_po_tipu[tip_vozila_]:
        boja_po_tipu[tip_vozila_][boja] = 1
    else:
        boja_po_tipu[tip_vozila_][boja] += 1

for tip in tip_vozila:
    tip_vozila[tip] = str(round(tip_vozila[tip]/len(text_list)*100, 2)) + '%'

result = {
    'tip_vozila': tip_vozila,
    'gradovi': gradovi,
    'boja_po_tipu': boja_po_tipu
}

print(result)
