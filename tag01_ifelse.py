# if/else - wenn das, dann das, sonst das Andere

alter = int(input("Wie alt bist Du? "))

if alter < 0:
	print("Das gibt's nicht!")
elif alter <18:
	print("Minderjährig!")
elif alter <65:
	print("Erwachsen!")
else:
	print("Senior!")
