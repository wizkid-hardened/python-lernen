# Tag 5: Listen und Funktionen kombinieren

zahlen = [3, 8, 15, 22, 7, 10, 1]

def gerade_zahlen_finden(liste):
    ergebnis = []
    for zahl in liste:
        if zahl % 2 == 0:
            ergebnis.append(zahl)
    return ergebnis

gefundene = gerade_zahlen_finden(zahlen)
print(gefundene)
