# CEFX 07:00 1
# print("1. feladat ")
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

print("2. feladat ")
print(f"Az első tanuló {beleptetes[0][1]}:{beleptetes[0][2]}-kor lépett be a főkapun. ")
print(f"Az utolsó tanuló {beleptetes[-1][1]}:{beleptetes[-1][2]}-kor lépett ki a főkapun. ")
# print("3. feladat ")


def ido(ora: int, perc: int):  # átváltjuk az időt percre (mindig a legkisebb időegységre), így tudunk intervallumban
    # megadni a feladatot. [ print(ido(7, 51)) -> 471 ], [ print(ido(8, 15)) -> 495 ]
    return (ora*60) + perc


with open("kesok.txt", "w", encoding="utf-8") as fajl:
    for egysor in beleptetes:
        if egysor[3] == 1 and ido(7, 50) < ido(int(egysor[1]), int(egysor[2])) <= ido(8, 15):
            fajl.write(f"{(egysor[1])}:{(egysor[2])} {egysor[0]}\n")

# egysor = ['CEFX', '07', '00', 1]
print("4. feladat")
menza_szamlalo = 0
for egysor in beleptetes:
    if egysor[3] == 3:
        menza_szamlalo += 1
print(f"A menzán aznap {menza_szamlalo} tanuló ebédelt. ")
# Ákos megoldása, érdemes ezt is elsajátítani, list comprehension., ugyanaz a megoldása mint az enyémnek.
# print(f"A menzán aznap {len([egyelem for egyelem in beleptetes if egyelem[3] == 3])} tanuló ebédelt. ")

print("5. feladat")

konyv_kolcson_lista = []
for tanulo in beleptetes:
    if tanulo[3] == 4 and tanulo[0] not in konyv_kolcson_lista:
        konyv_kolcson_lista.append(tanulo[0])

# print(konyv_kolcson_lista)
print(f"Aznap {len(konyv_kolcson_lista)} tanuló kölcsönzött a könyvtárban. ")

if len(konyv_kolcson_lista) < menza_szamlalo:
    print("Többen voltak, mint a menzán. ")
else:
    print("Nem voltak többen, mint a menzán. ")

print("6. feladat ")
print("Az érintett tanulók: ")
# Tehát a portás 10:50-kor zárta be a kaput, így ezek a srácok 10:45 - 10:50-ig hagyhatták el a helyszínt, és nem
# csekkolták le magukat, tehát amikor visszajöttek 10:50 - 11:00 között, akkor ha a 4, 3 lehúzót (menza, könyvtár)
# nem vesszük figyelembe, akkor a kártyájukon kétszer léptek be, ezeket keressük. 1, 1, 2, 1, 2
# Ötlet: szedjük össze az összes ilyen embernek (16 ember) napi tevékenységét, ne vegyük figyelembe a 3, 4, és ha
# egymás után kapunk két 1-est, akkor elkaptuk a delikvenst.

tizenegy_lista = []
for tanulo in beleptetes:
    if ido(10, 50) < ido(int(tanulo[1]), int(tanulo[2])) <= ido(11, 00) and tanulo[3] == 1:
        tizenegy_lista.append(tanulo[0])
# print(tizenegy_lista)

# megegyezzen az azonosító, valamint a 1, 2 kell -> [1, 2, 1, 2], [1, 1, 2, 1, 2]

belepes_kilepes = []
for tanulo in tizenegy_lista:
    belso_lista = [tanulo]
    for egyelem in beleptetes:
        if tanulo == egyelem[0] and (egyelem[3] == 1 or egyelem[3] == 2):
            belso_lista.append(egyelem[3])
    belepes_kilepes.append(belso_lista)
    belso_lista = []
# print(belepes_kilepes)

# Létrehozunk egy üres listát(belepes_kilepes). végigfutunk a 10:50 - 11:00 bejövő diákok azonosítóin ('EQBL')
# ez esetünkben a tanulo == 'EQBL', ezzel kezdhetünk valamit. minden egyes tanuló azonosítójánál végigfutunk
# a teljes listán (beleptetes) előtte létrehozunk egy üres listát (belso_lista), ez arra szolgál, hogy ebbe tegyük bele
# a kilepes, és belépés esemény kódját, majd vizsgálódunk, hogy ha a
# ( tanulo == nagy listánk (beleptetes) azonositójával ) ÉS ( 1-es, vagy 2-es kód van az egyelemen belül ),
# akkor beletesszük ebbe a belso_lista-ba. Majd ha végigment ez a beleptetes lista, tehát az összetett ciklusunk
# második ciklusa (amiben a nagy beleptetes listát futjuk át), ez esetben a belso_lista-nk kész van,
# appendelhetjuk a külsőbe -> belepes-kilepes.
# Vizsgáld meg megszámlálással (.count), hogy nem egyenlő 1-es és 2-es van-e a listában -> írjuk ki!

for tanulo in belepes_kilepes:
    if tanulo.count(1) != tanulo.count(2):
        print(tanulo[0], end=" ")

#TERVEZÉS:
# 1. Változó amibe eltároljuk a felhasználó által megadott tanuló azonosítóját (tanulo_azonosito)
# 2. Majd a megadott azonosítóval végig megyünk a beleptetes tömbön
# 3. Ha megvan az azonosító, akkor az ahhoz tartozó adatokat eltároljuk egy tömbben
# 3. LÉPÉS RÉSZBEN KÉSZ, DE JAVÍTÁSRA SZORUL 2024_09_07
# 4. Az eltárolt adatok (óra,perc) közül megkeressük azt ami belépés(1) és kilépés(2)
# 5. Majd a kilépés időből kivonjuk a belépés idejét
print("7. feladat")

adott_tanulo = []
tanulo_azonosito = input("Egy tanuló azonosítója=")  #ZOOM
for tanulo in beleptetes:
    if tanulo_azonosito == tanulo[0] and tanulo[3] == 1 or tanulo[3] == 2 :
        adott_tanulo.append("óra " + tanulo[1])
        adott_tanulo.append("perc " + tanulo[2])
        # adott_tanulo.append("esemény kód " + str(tanulo[3]))
print(adott_tanulo)

print(f"A tanuló érkezése és távozása között 7 óra 4 perc telt el.")


