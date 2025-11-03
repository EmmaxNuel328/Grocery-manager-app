def add_item(prompt,my_list = []):
	if type(prompt) == int:
		raise TypeError ("Invalid input")
	my_list.append(prompt)
	print(my_list)
	print(prompt,end = " ")
	return "added successfully"

def remove_item(prompt,my_list = []):
	my_list.remove(prompt)
	print(my_list)
	print(prompt,end = " ")
	return "removed successfully"