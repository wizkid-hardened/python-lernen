# Tag 8: Fehlerbehandlung bei leerer Liste

zahlen = []

def durchschnitt_gerader_zahlen(liste):
    summe = 0
    anzahl = 0
    for zahl in liste:
        if zahl % 2 == 0:
            summe = summe + zahl
            anzahl = anzahl + 1
    
    if anzahl == 0:
        return 0
    
    durchschnitt = summe / anzahl
    return durchschnitt

ergebnis = durchschnitt_gerader_zahlen(zahlen)
print(ergebnis)
