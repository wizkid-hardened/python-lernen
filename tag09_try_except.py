# Tag 9: try/except - Fehler abfangen statt verhindern

zahlen = []

def durchschnitt_gerader_zahlen(liste):
    summe = 0
    anzahl = 0
    for zahl in liste:
        if zahl % 2 == 0:
            summe = summe + zahl
            anzahl = anzahl + 1

    try:
        durchschnitt = summe / anzahl
        return durchschnitt
    except ZeroDivisionError:
        print("Keine geraden Zahlen gefunden, kann keinen Durchschnitt berechnen.")
        return 0

ergebnis = durchschnitt_gerader_zahlen(zahlen)
print(ergebnis)
