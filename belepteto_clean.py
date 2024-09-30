beleptetes = []
with open("bedat.txt", "r", encoding="utf-8") as file:
    for egysor in file:
        egysor = egysor.strip().split()
        ora_perc = ''.join(egysor[1]).split(":")    # ''.join == hozzáfűzés, azaz, egy üres listát létrehoz, és amit te
        # megadsz a zárójelbe, azt hozzá is teszi azonnyomban, tehát ez egy gyorsított append quasi.
        beleptetes.append([str(egysor[0]), str(ora_perc[0]), str(ora_perc[1]), int(egysor[2])])
        # ora_perc átalakítás nincs kihatással az egysorra
        # egysor = ['CEFX', '07', '00', 1]
print(beleptetes)

print("7. feladat ")

adott_tanulo = []
tanulo_azonosito = input("Egy tanuló azonosítója=")
for tanulo in beleptetes:
    if tanulo_azonosito != tanulo[0]:
        print("Ilyen azonosítójú tanuló aznap nem volt az iskolában.")
    elif tanulo_azonosito == tanulo[0] and tanulo[3] == 1 or tanulo[3] == 2:
        adott_tanulo.append("óra " + tanulo[1])
        adott_tanulo.append("perc " + tanulo[2])
        adott_tanulo.append("esemény kód " + str(tanulo[3]))
    print(adott_tanulo)
    # print(f"A tanuló érkezése és távozása között 7 óra 4 perc telt el.")