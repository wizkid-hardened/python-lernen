# Verdoppeln

def verdoppeln(zahl):
    return zahl * 2

ergebnis = verdoppeln(6)	# ergebnis = 12
print(ergebnis)			# gibt 12 aus

# Pruefeung: ist_gerade?

def ist_gerade(zahl):
	if zahl % 2 == 0:
		return True
	else:
		return False

print(ist_gerade(6))
print(ist_gerade(69))

# User friendly

def ist_gerade(zahl):
	if zahl % 2 == 0:
		return True
	else:
		return False

zahl = 7
ergebnis = ist_gerade(zahl)
print("Die Zahl", zahl, "ist gerade:", ergebnis)

# abgekuerzt

def ist_gerade(zahl):		# Funktion - eigener "Bauplan"
	return zahl % 2 == 0	# "zahl" existiert nur hier drin

zahl = 69			# eigene Variable im Hauptprogramm
ergebnis = ist_gerade(zahl)	# neue Variable "ergebnis" wird hier erstellt
print("Die Zahl", zahl, "ist gerade:", ergebnis)	#ergebnis wird hier abgerufen und geprueft
