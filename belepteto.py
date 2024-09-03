# CEFX 07:00 1
# print("1. feladat ")
beleptetes = []
with open("bedat.txt", "r", encoding="utf-8") as file:
    for egysor in file:
        egysor = egysor.strip().split()
        ora_perc = ''.join(egysor[1]).split(":") # ''.join == hozzáfűzés, azaz, egy üres listát létrehoz, és amit te megadsz a zárójelbe, azt hozzá is teszi azonnyomban, tehát ez egy gyorsított append quasi.
        beleptetes.append([str(egysor[0]), str(ora_perc[0]), str(ora_perc[1]), int(egysor[2])])  # ora_perc átalakítás nincs kihatással az egysorra
        # egysor = ['CEFX', '07', '00', 1]
print(beleptetes)

print("2. feladat ")
print(f"Az első tanuló {beleptetes[0][1]}:{beleptetes[0][2]}-kor lépett be a főkapun. ")
print(f"Az utolsó tanuló {beleptetes[-1][1]}:{beleptetes[-1][2]}-kor lépett ki a főkapun. ")

# print("3. feladat ")
def ido(ora:int, perc:int):  #átváltjuk az időt percre (mindig a legkisebb időegységre), így tudunk intervallumban megadni a feladatot. [ print(ido(7, 51)) -> 471 ], [ print(ido(8, 15)) -> 495 ]
    return (ora*60) + perc

# egysor = ['CEFX', '07', '00', 1]

with open("kesok.txt", "w", encoding="utf-8") as fajl:
    for egysor in beleptetes:
        if egysor[3] == 1 and ido(7, 50) < ido(int(egysor[1]), int(egysor[2])) <= ido(8, 15):
            fajl.write(f"{(egysor[1])}:{(egysor[2])} {egysor[0]}\n")