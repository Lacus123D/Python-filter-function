
# Csináltam egy egyszerű listát amiben nevek vannak.
nevek = ["Laci", "Márk", "Magdi", "József"]


# Na most nézzük hogyan kell használni.

bemutatás = list(filter(lambda m: len(m) == 4, nevek))

# Ilyenkor az m egyenlő lesz a listában lévő dolgokkal.

#Kifogja nekünk most listázni azokat az elemeket a listából amire ez igaz, tehát amelyik elemnek a a hossza egyenlő 4-gyel.

print(bemutatás)

#Ahogy látjátok visszakaptuk a Lacit és a Márkot mivel ennek a kettőnek a hossza egyenlő négy karakterrel, a többi lista elemnek nem.

#Csináltam egy listát amiben számok vannak.


számok = [12, 23, 80, 90, 34]

bemutatás2 = list(filter(lambda s: s % 2 == 0, számok))

#Ez vissza fogja nekünk adni azokat a számokat amelyeket elosztunk kettővel és 0-át kapunk. (Tehát visszakapjuk a páros számokat)

print(bemutatás2)

# Igen visszakaptuk mind a négy számot a listából kivéve egyet. Azt az egyet azért nem kaptuk vissza mert nem osztható kettővel maradék nélkül. (Tehát nem páros.)

# Összegzés: Tehát a filter függvény egy olyan beépített függvény amely kiszűri az igazak amire igaz azt visszaadja amire nem azt nem.
# De a lambda függvényen kivűl nem sok helyen találkozól vele.

