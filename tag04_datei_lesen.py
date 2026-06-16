# Tag 4: In Datei suchen

def suche_in_datei(suchbegriff):
    with open("test.txt", "r") as datei:
        for zeile in datei:
            if suchbegriff in zeile:
                print(zeile.strip())

suche_in_datei("Welt")

suche_in_datei("Python")
