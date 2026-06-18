# Tag 10: Dictionaries - Key-Value-Paare verstehen

mitglieder = {
    "Marvin": {"status": "aktiv", "checkins": 0},
    "Lisa": {"status": "aktiv", "checkins": 0},
    "Tom": {"status": "inaktiv", "checkins": 0},
}

for name, daten in mitglieder.items():
    if daten["status"] == "aktiv":
        daten["checkins"] = daten["checkins"] + 1
        print(f"{name}: Check-in erfolgreich (Anzahl: {daten['checkins']})")
    else:
        print(f"{name}: Zutritt verweigert (Status: {daten['status']})")

print(mitglieder)			# Debug-Ausgabe für Entwickler
