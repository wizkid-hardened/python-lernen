# Unbekannte Variable überschreiben
try:
	punkte = int(input("Wie viele punkte hast Du? "))
	punkte += 50
	print("Mit Bonus:", punkte)
except ValueError:
	print("Bitte nur Zahlen eigeben!")
