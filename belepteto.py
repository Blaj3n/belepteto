# CEFX 07:00 1

beleptetes = []

with open("bedat.txt", "r", encoding="utf-8") as file:
    for egysor in file:
        egysor = egysor.strip().split()
        ora_perc = ''.join(egysor[1]).split(":") # ''.join == hozzáfűzés, azaz, egy üres listát létrehoz, és amit te megadsz a zárójelbe, azt hozzá is teszi azonnyomban, tehát ez egy gyorsított append quasi.
        beleptetes.append([str(egysor[0]), str(ora_perc[0]), str(ora_perc[1]), int(egysor[2])])  # ora_perc átalakítás nincs kihatással az egysorra
        # egysor = ['CEFX', '07', '00', 1]
print(beleptetes)

