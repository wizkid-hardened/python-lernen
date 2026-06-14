# eine Liste erstellen

hobbys = ["IT", "Fitness", "Gaming"]

print(hobbys)
print(hobbys[0])
print(hobbys[1])
print(hobbys[2])

# Liste mit for-Schleife kombinieren

hobbys = ["IT", "Fitness", "Gaming"]

for hobby in hobbys:
	print("Mein Hobby:", hobby)

# Liste (oder "List") – ist quasi ein eigener Datentyp:

hobbys = ["IT", "Fitness", "Gaming"]		# Liste von Strings
zahlen = [1, 2, 3, 4, 5]			# Liste von Integers
gemischt = ["Text", 69, True]			# Liste kann auch mischen!

# mit type() checken:

print(type(hobbys))				# <class 'list'>
print(type(hobbys[0]))				# <class 'str'>


hobbys = ["IT", "Fitness", "Gaming"]

# Element hinzufügen
hobbys.append("Lesen")
print(hobbys)

# Wie viele Elemente?
print("Anzahl:", len(hobbys))

# Element entfernen
hobbys.remove("Gaming")
print(hobbys)
