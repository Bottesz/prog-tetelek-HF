'''
1-	Számold meg, hogy hány darab 7-tel osztható szám van 1-1000 között!
'''

def elsofeladat(szam):
    szam = 0

for i in range(1, 1001):
    if i % 7 == 0:
        szam += 1

print("Az 1 és 1000 közötti 7-tel osztható számok darabszáma:", {szam})






'''
2-	Számold meg, hogy hány darab 12-vel osztható szám van 2000-20000 között!
'''

def masodikfeladat(szam):
    szam = 0

for i in range(2000, 20001):
    if i % 12 == 0:
        
        szam += 1

print("A 2000 és 20000 közötti 12-tel osztható számok darabszáma:", {szam})





'''
3-	Írd ki az első 20 3-mal osztható szám négyzetének összegét!
'''
def harmadikfeladat():
    osszeg = 0
    szam = 0
    harommaloszthato_szam = 1

    while szam < 20:
        if harommaloszthato_szam % 3 == 0:
            osszeg += harommaloszthato_szam ** 2
        szam += 1
    harommaloszthato_szam += 1

print("Az első 20 darab 3-mal osztható szám négyzetének összege:", {osszeg})







'''
4-	Keresd meg egy szám egész osztóit!
'''
def negyedikfeladat(szam,egesz_osztok,adott_szam,osztok_listaja ):
    adott_szam = 24
    osztok_listaja = egesz_osztok(adott_szam)
    
    osztok = [i]
    for i in range(1, szam + 1):
        if szam % i == 0:
            osztok.append(i)
    return osztok
print(f"{adott_szam} egész osztói: {osztok_listaja}")