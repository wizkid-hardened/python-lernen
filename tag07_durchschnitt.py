# Tag 7: Durchschnitt berechnen

zahlen = [3, 8, 15, 22, 7, 10, 1]

def durchschnitt_gerader_zahlen(liste):
    summe = 0
    anzahl = 0
    for zahl in liste:
        if zahl % 2 == 0:
            summe = summe + zahl
            anzahl = anzahl + 1
    durchschnitt = summe // anzahl
    return durchschnitt

ergebnis = durchschnitt_gerader_zahlen(zahlen)
print(ergebnis)
