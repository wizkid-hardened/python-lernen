# Tag 10: Dictionaries - neues Mitglied hinzufuegen, aktive und inaktive zaehlen

mitglieder = {
    "Marvin": {"status": "aktiv", "checkins": 1},
    "Lisa": {"status": "aktiv", "checkins": 1},
    "Tom": {"status": "inaktiv", "checkins": 0},
}

# neues Mitglied hinzufuegen

mitglieder["Petra"] = {"status": "aktiv", "checkins": 0}

aktive = 0
inaktive = 0

for name, daten in mitglieder.items():
    if daten["status"] == "aktiv":
        aktive = aktive + 1
    else:
        inaktive = inaktive + 1

print(f"Aktive Mitglieder: {aktive}")
print(f"Inaktive Mitglieder: {inaktive}")

