
#ulesanne 1

print("Tere, maailm!")
nimi = input("Sisesta oma nimi: ")
vanus = int(input("Sisesta oma vanus: "))
print(f"Tere, maailm! Tervitan sind {nimi}! Sa oled {vanus} aastat vana.")

#ulesanne 2

vanus = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_käib_koolis = True

# Типы переменных
print(type(vanus))          # int
print(type(eesnimi))        # str
print(type(pikkus))         # float
print(type(kas_käib_koolis))  # bool


kas_käib_koolis = False
print(type(kas_käib_koolis))

#ulesanne 3

kommide_arv = int(input("Mitu kommi on laual? "))
võetud_kommid = int(input("Mitu kommi soovid ära võtta? "))

kommide_arv -= võetud_kommid
print(f"Laual on nüüd {kommide_arv} kommi.")

#ulesanne 4

import math

ümbermõõt = float(input("Sisesta puu ümbermõõt (meetrites): "))
läbimõõt = ümbermõõt / math.pi
print(f"Puu läbimõõt on {läbimõõt:.2f} meetrit.")

#ulesanne 5

import math

N = float(input("Sisesta maatüki laius (m): "))
M = float(input("Sisesta maatüki pikkus (m): "))
diagonaal = math.sqrt(N**2 + M**2)
print(f"Maatüki diagonaal on {diagonaal:.2f} meetrit.")

#ulesanne 6


aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus / aeg

print(f"Sinu kiirus oli {kiirus:.2f} km/h")

#ulesanne 7

arvud = []
for i in range(5):
    arv = int(input(f"Sisesta {i+1}. täisarv: "))
    arvud.append(arv)

aritmeetiline_keskmine = sum(arvud) / len(arvud)
print(f"Aritmeetiline keskmine on {aritmeetiline_keskmine:.2f}")

#ulesanne 8


print("   @..@")
print("  (----)")
print(" ( \\__/ )")
print("^^ \"\" ^^")

#ulesanne 9

a = int(input("Sisesta esimene külg (a): "))
b = int(input("Sisesta teine külg (b): "))
c = int(input("Sisesta kolmas külg (c): "))

P = a + b + c
print(f"Kolmnurga ümbermõõt on {P}")

#ulesanne 10

hind = 12.90
jootraha_protsent = 0.10
sõprade_arv = int(input("Mitu sõpra on pitsa jagamisel kokku? "))

kogusumma = hind + hind * jootraha_protsent
jagatav_summa = kogusumma / sõprade_arv
print(f"Igaüks peab maksma {jagatav_summa:.2f} €")


