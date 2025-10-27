def add_item(prompt,my_list = []):
	if type(prompt) == int:
		raise TypeError ("Invalid input")
	my_list.append(prompt)
	print(my_list)
	print(prompt,end = " ")
	return "added successfully"

#defs