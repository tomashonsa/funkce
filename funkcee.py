def deleni(delitel, jmenovatel):
    if jmenovatel !=0:
        vysledek = delitel/jmenovatel
        return vysledek
    else:
        print("nelze dělit nulou")

x = int(input("Zadejte proměnu a: "))
y = int(input("Zadejte proměnu b: "))

print("výsledek je: ", deleni(x,y))