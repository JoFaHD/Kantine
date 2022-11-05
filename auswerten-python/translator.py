# Lutscht sich alle neuen Teile des Monats/Woche und übersetzt alle erstmal auf Deutsch und Englisch

import json
from googletrans import Translator
translator = Translator()

# Nimmt sich das neueste Menü
with open("outputs/output.json", "r", encoding="utf-8") as file:
    originaledatei = json.loads(file.read())
    

# Erstellt die Listen der ganzen teile des Menüs
Suppen   = []
Suppen_de = {}
Hauptspeisenteile   = []
Hauptspeisenteile_de = {}

# Füllt die Listen der ganzen teile des Menüs
for day in originaledatei:
    Suppen.append(originaledatei[day][1])
    Hauptspeisenteile.append(originaledatei[day][2])
    Hauptspeisenteile.append(originaledatei[day][3])
    Hauptspeisenteile.append(originaledatei[day][4])

# String zum übersetzen, ginge auch mit for loop, als EIN string ists aber weniger packages ig
Suppenstr = ""
for thing in Suppen:
    Suppenstr += thing + ";"

# Hier wird der String übersetzt | Deutsch
try: Suppenstr_de = translator.translate(Suppenstr, src="fr", dest="de").text
except AttributeError: print(" Funzt iwie nicht, ausser mit der Version hier: pip install googletrans==4.0.0-rc1")
# Überstetzter String wird wieder auseinander gezogen und zur Liste gemacht
Suppenlist_de = Suppenstr_de.split(";")
# Muss, weil leeres Element am ende der Liste wegen dem loop Z.27/28
Suppenlist_de.pop()

# Checkt ob Suppen ordentlich übersetzt wurden, passiert iwie manchmal
if len(Suppenlist_de) != len(Suppen):
    # Nimmt den fehlenden Teil
    fehlend = len(Suppen) - len(Suppenlist_de)
    neuesuppenliste = Suppen[-fehlend:len(Suppen)]
    # Gleicher übersetztungsprozess wie oben
    Suppenstr = ""
    for thing in neuesuppenliste:
        Suppenstr += thing + ";"
    Suppenstr_de = translator.translate(Suppenstr, src="fr", dest="de").text
    Suppenlist_de += Suppenstr_de.split(";")
    Suppenlist_de.pop()
    

# Geht durch alle Teile und packt sie ins Wörterbuch
for x in range(len(Suppen)):
    Suppen_de[Suppen[x]] = Suppenlist_de[x]

# String zum übersetzen, ginge auch mit for loop, als EIN string ists aber weniger packages ig
Hauptspeisenteilestr = ""
for thing in Hauptspeisenteile:
    # Checkt ob Teil None ist, wegen Übersetzungsproblemen
    if thing == None:
        Hauptspeisenteilestr += "german; "
    # Ersetzt alle / wegen Übersetzungsproblemen
    elif thing.__contains__("/"):
        Hauptspeisenteilestr += thing.replace("/", ",") + "; "
    else:
        Hauptspeisenteilestr += thing + "; "

# Hier wird der String übersetzt | Deutsch
Hauptspeisenteilestr_de = translator.translate(Hauptspeisenteilestr, src="fr", dest="de").text
# Überstetzter String wird wieder auseinander gezogen und zur Liste gemacht
Hauptspeisenteilelist_de = Hauptspeisenteilestr_de.split(";")
# Muss, weil leeres Element am ende der Liste wegen dem loop Z.27/28
Hauptspeisenteilelist_de.pop()

# Geht durch alle Teile und packt sie ins Wörterbuch
for x in range(len(Hauptspeisenteile)):
        Hauptspeisenteile_de[Hauptspeisenteile[x]] = Hauptspeisenteilelist_de[x]

# Entfernt die Übersetzung für null/none
Hauptspeisenteile_de[None] = "     "
Hauptspeisenteile_de.pop(None, 1)
    
#print(Suppen_de)
#print("\n")
#print(Hauptspeisenteile_de)

with open("dictionary_fr/suppen_deutsch.json", "r") as file:
    altersuppendict = json.loads(file.read())

for neuesuppe in Suppen_de:
    if neuesuppe in altersuppendict:
        continue
    else:
        altersuppendict[neuesuppe] = Suppen_de[neuesuppe]

with open("dictionary_fr/suppen_deutsch.json", "w") as file:
    file.write(json.dumps(altersuppendict))


with open("dictionary_fr/haupt_deutsch.json", "r") as file:
    alterhauptdict = json.loads(file.read())

for neuesteil in Hauptspeisenteile_de:
    if neuesteil in alterhauptdict:
        continue
    else:
        alterhauptdict[neuesteil] = Hauptspeisenteile_de[neuesteil]

alterhauptdict.pop("none", 1)
with open("dictionary_fr/haupt_deutsch.json", "w") as file:
    file.write(json.dumps(alterhauptdict))

"""Englisch"""


Suppen   = []
Suppen_en = {}
Hauptspeisenteile   = []
Hauptspeisenteile_en = {}

for day in originaledatei:
    Suppen.append(originaledatei[day][1])
    Hauptspeisenteile.append(originaledatei[day][2])
    Hauptspeisenteile.append(originaledatei[day][3])
    Hauptspeisenteile.append(originaledatei[day][4])

Suppenstr = ""

for thing in Suppen:
    Suppenstr += thing + ","

Suppenstr_en = translator.translate(Suppenstr, src="fr", dest="en").text
Suppenlist_en = Suppenstr_en.split(",")
Suppenlist_en.pop()


for x in range(len(Suppenlist_en)):
    Suppen_en[Suppen[x]] = Suppenlist_en[x]




Hauptspeisenteilestr = ""

for thing in Hauptspeisenteile:
    if thing == None:
        Hauptspeisenteilestr += "german; "
    elif thing.__contains__("/"):
        Hauptspeisenteilestr += thing.replace("/", ",") + "; "
    else:
        Hauptspeisenteilestr += thing + "; "

Hauptspeisenteilestr_en = translator.translate(Hauptspeisenteilestr, src="fr", dest="en").text
Hauptspeisenteilelist_en = Hauptspeisenteilestr_en.split(";")
Hauptspeisenteilelist_en.pop()

lenmin1 = len(Hauptspeisenteilelist_en) - 1
for x in range(len(Hauptspeisenteile)):
    # print(x)
    if Hauptspeisenteilelist_en[x] == "vertaalen":
        Hauptspeisenteile_en[Hauptspeisenteile[x]] = "_______"
    else:
        Hauptspeisenteile_en[Hauptspeisenteile[x]] = Hauptspeisenteilelist_en[x]

Hauptspeisenteile_en[None] = "     "
Hauptspeisenteile_en.pop(None, 1)
    
#print(Suppen_en)
#print("\n")
#print(Hauptspeisenteile_en)

with open("dictionary_fr/suppen_englisch.json", "r") as file:
    altersuppendict = json.loads(file.read())

for neuesuppe in Suppen_en:
    if neuesuppe in altersuppendict:
        continue
    else:
        altersuppendict[neuesuppe] = Suppen_en[neuesuppe]

with open("dictionary_fr/suppen_englisch.json", "w") as file:
    file.write(json.dumps(altersuppendict))


with open("dictionary_fr/haupt_englisch.json", "r") as file:
    alterhauptdict = json.loads(file.read())

for neuesteil in Hauptspeisenteile_en:
    if neuesteil in alterhauptdict:
        continue
    else:
        alterhauptdict[neuesteil] = Hauptspeisenteile_en[neuesteil]

with open("dictionary_fr/haupt_englisch.json", "w") as file:
    file.write(json.dumps(alterhauptdict))


exit("Erfolgreich")