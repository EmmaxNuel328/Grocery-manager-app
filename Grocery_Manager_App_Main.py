from Grocery_Manager_App_Functions import *
Grocery_App_Homepage = """
	_________________________________________
       |      WELCOME TO EMMAX GROCERY APP       |
       |=========================================|
       |  	     1. ADD ITEM                 |
       |=========================================|
       |             2. REMOVE ITEM              |
       |=========================================|
       |      3. SHOW ALL ITEMS AVAILABLE        |
       |_________________________________________|
"""
print(Grocery_App_Homepage)
store = []
user_input = 1
while user_input != 0:
	user_input = input("Enter your choice: ")
	match user_input:
		case "1":
			add_item_input = 1
			while add_item_input != 0:
				add_item_input = input("Enter item you want to add: ")
				print(add_item(add_item_input))
