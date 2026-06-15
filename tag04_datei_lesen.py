# Tag 4: Dateien öffnen und durchsuchen

# 1. Wir erstellen uns erst mal eine künstliche Logdatei, damit wir was zum Testen haben.
# Das "w" steht für "write" (schreiben).
with open("test_log.txt", "w") as datei:
    datei.write("INFO: System gestartet\n")
    datei.write("WARNING: Festplatte zu 80% voll\n")
    datei.write("ERROR: Verbindung zur Datenbank verloren!\n")
    datei.write("INFO: User 'wizkid' hat sich eingeloggt\n")


# 2. Jetzt schreiben wir eine Funktion, die die Datei durchsucht
def log_durchsuchen(suchbegriff):
    print("--- Suche nach:", suchbegriff, "---")
    
    # "r" steht für "read" (lesen)
    with open("test_log.txt", "r") as datei:
        # Die for-schleife geht die Datei automatisch Zeile für Zeile durch
        for zeile in datei:
            # Prüfen, ob unser Suchwort in der aktuellen Zeile steckt
            if suchbegriff in zeile:
                # .strip() macht die unsichtbaren Zeilenumbrüche am Ende weg
                print(zeile.strip())

# 3. Funktion testen
log_durchsuchen("ERROR")
log_durchsuchen("INFO")
