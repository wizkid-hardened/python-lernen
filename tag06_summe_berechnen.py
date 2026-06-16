# Tag 6: Summe berechnen

zahlen = [3, 8, 15, 22, 7, 10, 1]

def summe_gerader_zahlen(liste):
    summe = 0
    for zahl in liste:
        if zahl % 2 == 0:
            summe = summe + zahl
    return summe

ergebnis = summe_gerader_zahlen(zahlen)
print(ergebnis)
