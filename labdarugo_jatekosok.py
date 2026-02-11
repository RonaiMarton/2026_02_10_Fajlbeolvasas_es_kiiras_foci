"""
Olvasd be a labdarugok.txt adatait, majd oldd meg az alábbi feladatokat!

1. Hány játékos szerepel a fájlban?
2. Melyik játékos szerezte a legkevesebb gólt?
3. Melyik játékos szerzett a legtöbb gólt?
4. Ki játszott a legtöbb mérkőzést?
5. Átlagosan hány gólt szerzett egy játékos?

***EXTRA - nehezebb feladat*** (nem kötelező, de érdemes megpróbálni):
6. Melyik csapat szerzett a legtöbb gólt? (feltételezve, hogy egy játékos csak egy csapatban játszott)


A megoldott feladatokat a kiirt_adatok nevű mappában hozd létre statisztika.txt néven!
"""


# print("A beolvasott fájlban összesen ____ játékos szerepel.")
# print("A legkevesebb gólt szerző játékos: ____")
# print("A legtöbb gólt szerző játékos: ____")
# print("A legtöbb mérkőzést játszó játékos: ____")
# print("Az átlagos gólszám: ____")
# print("***A legtöbb gólt szerző csapat: ____")

labdarugok = []
with open('beolvasando_adatok\labdarugok.txt', 'r', encoding='utf-8') as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        #Név; Csapat; Gólszám; Mérkőzések száma
        nev = adatok[0]
        csapat = adatok[1]
        golszam = int(adatok[2])
        merkozesek_szama = int(adatok[3])

        labdarugo = {'nev': nev, 'csapat': csapat, 'golszam': int(golszam), 'merkozesek_szama': int(merkozesek_szama)}
        labdarugok.append(labdarugo)

# print(f'{labdarugok=}')

print('1.feladat')
print(f" A beolvasott fájlban összesen {len(labdarugok)} játékos szerepel.")


print("2.feladat")
legkevesebb_gol = 100000
for i in labdarugok:
    if i['golszam'] < legkevesebb_gol:
        legkevesebb_gol = i['golszam']
        legkevesebb_gol_jatekos = i['nev']
print(f"A legkevesebb gólt szerző játékos: {legkevesebb_gol_jatekos}")


print("3. feladat")
legtobb_gol = 0
for i in labdarugok:
    if i['golszam'] > legtobb_gol:
        legtobb_gol = i['golszam']
        legtobb_gol_jatekos = i['nev']
print(f"A legtöbb gólt szerző játékos: {legtobb_gol_jatekos}")


print("4.feladat")
legtobb_merkozes = 0
for i in labdarugok:
    if i['merkozesek_szama'] > legtobb_merkozes:
        legtobb_merkozes = i['merkozesek_szama']
        legtobb_merkozes_nev = i['nev']

print(f"A legtöbb mérkőzést játszó játékos: {legtobb_merkozes_nev}")


print("5. feladat")
# atlag_golszam = sum(labdarugok['golszam']) / len(labdarugok)
# a lista elemei szótárak, ezért nem lehet rá így hivatkozni
# végik kell menni rajta 
atlag_golszam = sum(i['golszam'] for i in labdarugok) / len(labdarugok)

print(f"Az átlagos gólszám: {atlag_golszam}")
